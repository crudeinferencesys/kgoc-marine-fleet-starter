# MVP Specification — Theme 4: Marine Fleet Utilization & Optimization

> **Status:** Kickoff Draft — finalize Section 2 & Section 3 right after running
> `python manage.py inspect_dataset <path>` at 11:00 AM, then run **one** focused
> Goldfish review (`/egm:egm-review-loop` with `design_critic` + `implementation_readiness`).

---

## 1. Problem & Target User
- **Target User:** KGOC / KJO Offshore Marine Fleet Dispatchers & Marine Operations Supervisors managing crew boats (16–22 pax), utility boats (7–9 tons cargo), multipurpose vessels, and standby vessels between marine bases and offshore platforms.
- **Core Pain Point:** Frequent under-utilized / half-empty sailings, unflagged fuel-burn anomalies, and manual scheduling that misses safe consolidation opportunities across overlapping platform runs.

---

## 2. Organizer Dataset Inspection (Fill at 11:00 AM)
- **Expected Source:** Organizer-provided Theme 4 mock dataset (8 vessels, 976 trips over 90 days) or synthetic fallback if unavailable.
- **Actual Columns Observed:** *(paste `inspect_dataset` output summary here)*
- **Key Edge Cases Observed:** *(e.g. cancellations, zero-cargo/pax positioning runs, missing timestamps, extreme fuel outliers)*

---

## 3. Frozen Core Data Model (`apps/core/models.py`)
*(Define exact shared models here after inspecting the dataset, implement once in `apps/core/models.py`, commit `0001_initial.py` + `seed_fleet` command to `main`, and freeze.)*
- `Vessel` (name, vessel_type, pax_capacity, cargo_capacity_tons, hourly_fuel_rate, daily_charter_kwd, status)
- `Trip` (vessel, origin, destination, departure_time, pax_count, cargo_tons, fuel_liters, weather_state, status, is_consolidated)
- `DispatchPlan` / `SafetyOverride` (persisted optimization batches & supervisor weather/safety overrides)

---

## 4. The 3 Working Core Features (+1 Bonus AI)

### Feature 1 — Trips & Utilization Ledger (`apps/trips/`, Teammate A)
- **Goal:** View fleet utilization KPIs across all 976 historical trips + log new trip requests directly into PostgreSQL.
- **Standalone & Testable:** Judges submit a new crew/cargo trip request via HTMX form -> persisted to DB -> utilization rate & half-empty flag appear immediately.

### Feature 2 — Python Dispatch Consolidation Optimizer (`apps/optimizer/`, Teammate B)
- **Goal:** Group compatible pending/under-utilized trips within safe passenger (16–22), cargo (7–9t), time-window, and weather constraints.
- **Standalone & Testable:** Judges click "Run Consolidation Solver" -> view before/after trip count, fuel liters saved, and KWD saved -> click "Approve & Save Plan" to persist consolidated schedule to DB.

### Feature 3 — Safety & Fuel Anomaly Guard (`apps/safety/`, Shared)
- **Goal:** Detect abnormal fuel-burn trips (statistical z-score / IQR per vessel class) and enforce weather/standby safety constraints (preventing unsafe merges).
- **Standalone & Testable:** Judges inspect flagged anomalous trips, log a weather hold or vessel maintenance override to DB, and verify the optimizer respects the safety block.

### Bonus AI Feature — Gemini Dispatch Co-Pilot (`apps/core/ai.py` + `apps/optimizer/`)
- **Embedded AI Work:** Sends structured fleet utilization + proposed consolidation metrics + active safety/weather holds to Gemini (`DispatchBriefing` Pydantic schema).
- **Live Output:** Explains *why* specific trips should consolidate, highlights operational/safety risks, and drafts a concise shift handover brief (with deterministic fallback if API times out).

---

## 5. Quantified Impact Formulas (Pillar 4 — Label Assumptions Clearly)
- **Trips Eliminated:** `baseline_trips - optimized_trips`
- **Fuel Saved (Liters):** `sum(eliminated_trip_expected_fuel) - consolidation_detour_penalty`
- **Cost Saved (KWD):** `(fuel_liters_saved * assumed_diesel_kwd_per_liter) + (vessel_hours_saved * assumed_hourly_operating_kwd)`
- **Dispatcher Time Saved:** Estimated minutes saved per shift vs manual spreadsheet matching.

---

## 6. Judging Live Test Script (End-to-End < 3 Minutes)
1. Open live Cloud Run URL `/` (confirm zero login prompt and populated KPIs).
2. Open `/trips/` -> submit a half-empty trip request -> verify DB persistence on reload.
3. Open `/safety/` -> toggle a weather/standby constraint -> verify it saves to DB.
4. Open `/optimizer/` -> run solver -> inspect KWD & fuel savings -> generate AI Dispatch Co-Pilot briefing -> approve & save plan.
