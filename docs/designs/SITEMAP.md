# Design Sitemap (EGM Lite)

Index of active specifications, frozen boundaries, and team ownership.

## Documents
| Document | Purpose | Status |
|---|---|---|
| [hackathon_brief.md](../hackathon_brief.md) | Official KGOC + CODED workshop rules & Theme 4 summary | Reference |
| [architecture.md](architecture.md) | Stack, GCP Cloud Run + Cloud SQL, HTMX, Gemini AI wrapper | Locked |
| [mvp-spec.md](mvp-spec.md) | Theme 4 dataset schema, 3 core features, Bonus AI, KWD math | Draft — finalize at 11:00 AM |

## Vertical Slice Ownership
| Slice | Paths | Owner |
|---|---|---|
| Core Shell & Frozen Schema | `apps/core/`, `templates/base.html`, `config/` | Shared (Frozen after 11:45 AM) |
| Feature 1: Trips & Utilization | `apps/trips/`, `templates/trips/` | Teammate A |
| Feature 2: Dispatch Optimizer + AI | `apps/optimizer/`, `templates/optimizer/` | Teammate B |
| Feature 3: Safety & Fuel Guard | `apps/safety/`, `templates/safety/` | Shared / Coordinate |
