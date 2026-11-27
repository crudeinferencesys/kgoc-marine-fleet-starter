# KGOC AI Hackathon for the Oil & Gas Industry (CODED) — Workshop Summary

## 1. Overview & Context
* **Organizers:** Kuwait Gulf Oil Company (KGOC - established 2002, subsidiary of KPC) & CODED.
* **Industry Context:** KGOC manages Kuwait's share of oil and gas in the Divided Zone with Saudi Arabia through joint operations:
  * **WJO (Wafra Joint Operations):** Onshore fields operated with Chevron Saudi Arabia.
  * **KJO (Khafji Joint Operations):** Offshore fields operated with AGOC (Aramco Gulf Operations Company).
* **Goal:** Build a functional Minimum Viable Product (MVP) in one day that solves a specific, real-world problem in the oil and gas industry. Ideas are not restricted to a single field.

---

## 2. The 4 Hackathon Themes
Teams must pick **one** primary theme and identify a specific pain point within it:

1. **Oilfield Operations & Maintenance (عمليات الحقول والصيانة)**
   * **Focus:** Monitoring and managing well performance, pipeline integrity, equipment inspections, and preventive maintenance to prevent unexpected downtime.
   * **Sample Ideas:** Unified well-monitoring dashboards, AI-powered early fault detection, marine weather window trackers for offshore shifts, subsea pipeline risk dashboards.
2. **Environment & Resource Management (البيئة وإدارة الموارد)**
   * **Focus:** Tracking and reducing environmental impact—specifically industrial waste, water management, emissions, and HSE compliance reporting.
   * **Sample Ideas:** Emissions trackers by site/month, waste disposal tracking apps, water balance forecasting dashboards, unified environmental audit portals that flag missing logs early.
3. **Business Processes & Automation (إجراءات العمل والأتمتة)**
   * **Focus:** Streamlining internal workflows, procurement, contracts, cost estimations, and inter-departmental approvals to eliminate email bottlenecks.
   * **Sample Ideas:** Request/approval status trackers that validate missing fields upfront, AI contract risk reviewers, internal RAG/document Q&A chatbots, automated anomaly reporting engines.
4. **Marine Fleet Utilization & Optimization (تشغيل الأسطول البحري وتحسينه)**
   * **Focus:** Optimizing crew boats (16–22 passengers), utility boats (7–9 tons cargo), multipurpose vessels, and standby vessels operating between marine bases and offshore platforms without compromising safety.
   * **Sample Ideas:** Trip ticketing/booking systems, fuel efficiency trackers, AI vessel dispatchers that prevent half-empty trips and factor in weather/safety constraints. *(Note: Organizers can provide optional mock data of 8 vessels, 976 trips over 90 days upon request).*

---

## 3. Project & Feature Requirements (The Rules)

### The 4 Core Project Pillars
1. **Improve Operations/Performance:** Solves a real problem in one of the 4 themes.
2. **Simplify Work:** Clean, intuitive UI that helps users finish tasks faster.
3. **Collect & Document Data:** Users can input readings, notes, or files, and the app saves them to a **database**.
4. **Responsible Resource Use:** Saves time, resources, or reduces waste (quantified with an estimated metric, e.g., *"saves 1 hour of supervisor time daily"*).

### The "Max 3 Features" Rule
Your MVP must have **at most 3 working core features** (3 working features > 6 half-broken ones). To count as a valid feature for judging, it must pass **all 5 criteria**:
1. **Functional:** Actually performs an action (not static text).
2. **Meaningful:** Solves a specific user pain point.
3. **High Value:** Directly advances the core solution.
4. **Standalone:** Has an independent goal (not a sub-step of another feature).
5. **Testable:** Judges can interact with it live and verify it works.

* **What DOES NOT count as a standalone feature:** Search/filter/sort bars, page navigation, static info pages, dark mode/theme toggles, basic login/signup screens, or standalone PDF exports.

### Bonus AI Feature Qualification (Optional — Extra Points)
Using AI to *build* the app does not count. To earn bonus points, an AI feature must meet **all 5 conditions**:
1. Embedded **inside** the app (e.g., data analysis, personalized recommendations, forecasting, content summarization).
2. Directly addresses the core problem.
3. Performs meaningful AI work (not a generic unrelated chatbot).
4. Works live during judging with visible outputs used by the app.
5. Clearly documented/explained (inputs, AI logic, and how judges can test it).

---

## 4. Building with AI ("Vibe Coding" on Replit)
* **Build Loop:** **Describe** (user + need) $\rightarrow$ **Generate** (AI Agent writes code) $\rightarrow$ **Test** (click through as a real user) $\rightarrow$ **Refine** (one small change at a time).
* **5 Prompting Best Practices:**
  1. Describe the *user and their needs*, not technical code.
  2. Request **one change at a time**.
  3. Test in the Preview pane after every single step.
  4. Never just say *"it's broken."* Use the **4-part Bug Fix Prompt**:
     * **Action:** What you clicked/did.
     * **Actual Result:** What happened instead.
     * **Expected Result:** What should have happened.
     * **Constraint:** What *not* to change.
  5. Use **Replit Checkpoints** to roll back if 2–3 fix attempts fail, rather than stacking broken fixes.
* **Synthetic / Mock Data Guidelines:**
  * Generate realistic mock data using the AI Agent tailored to your Idea Canvas (include realistic categories, edge cases like full/empty capacities, and messy states like cancellations).
  * Always label it clearly as **mock/synthetic data** in your `README` under a `Data Used` section—never present it as real company data.

---

## 5. Team Formation & Logistics

### Team Rules (Deadline: Friday, Nov 27 at 11:00 PM)
* **Team Size:** **2 to 4 members** (mixed teams combining oil-sector professionals and public participants are encouraged).
* **Portal Registration:** Scan the CODED Hackathon Portal QR code, sign in with your registered email + OTP, create/join a team, and invite teammates via email, Participant ID, or invite link before **11:00 PM tonight**.

### Competition Day Schedule — Saturday, November 28, 2026
* **Location:** Al Shaheed Park (Phase 2) — Multipurpose Hall 2 *(Free Replit access provided on-site)*.
* **09:30 – 10:15:** Check-in (punctual arrival required)
* **10:15 – 11:00:** Orientation
* **11:00:** Competition Starts
* **17:00:** Competition Ends (Submission Deadline)
* **19:00:** Closing Ceremony & Winners Announcement

### Prizes (Total: 2,500 KWD)
* **1st Place:** 1,200 KWD
* **2nd Place:** 800 KWD
* **3rd Place:** 500 KWD

### Final Submission Checklist
1. **Published App:** A live, publicly accessible URL that opens without requiring judges to log in.
2. **Source Code:** Submitted via the hackathon portal.
3. **README File:** Documents the problem, target user, solution, the 3 core features, instructions on how to test, mock data assumptions, AI feature details (if applicable), and limitations.
