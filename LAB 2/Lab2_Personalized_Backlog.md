# Lab 2 - Pharmacy Inventory Management Backlog

Prepared from the Lab 1 requirements table. Scope: pharmacy batch/expiry tracking, FEFO dispensing, automatic purchase orders and supplier order visibility.

> **Status:** Jira-ready backlog design. The connected Jira workspace has no empty Scrum project for this scenario. The existing Scrum project is already used for Personalized News Emailer, so no pharmacy work was added to it. Create a dedicated company-managed Scrum project before entering these issues.

## Requirement traceability

| Lab 1 ID | Requirement summary | Priority | Story |
|---|---|---:|---|
| FR-001 | Select the valid batch with the nearest expiry at checkout (FEFO). | High | US-02 |
| FR-002 | Track batch expiry dates and visually flag those expiring within 30 days. | High | US-01 |
| FR-003 | Generate a clerk dispensing list sorted by nearest valid expiry first. | High | US-03 |
| FR-004 | Create a draft PO immediately when stock drops below its minimum threshold. | Medium | US-04 |
| FR-005 | Let suppliers view dispatched POs. | Medium | US-06 |
| NFR-001 | Auto-generate/dispatch supplier PO requests at the safety threshold; validate latency and security under peak load. | High | US-05 |
| NFR-002 | Maintain 99.9% uptime during pharmacy operating hours; under 43 minutes downtime/month. | High | US-07 |

## Epics

### EPIC 1 - FEFO Inventory Control
Maintain batch expiry visibility and ensure the correct batches are selected and presented for dispensing.

### EPIC 2 - Automated Replenishment and Supplier Orders
Create purchase orders at configured thresholds, dispatch requests and provide supplier visibility.

### EPIC 3 - Operational Reliability
Keep the stock-management engine available during pharmacy operating hours.

## User Stories

### US-01 - Expiry tracking and near-expiry warnings
**As a** pharmacy inventory clerk, **I want** to view batch expiry dates and see a warning for batches expiring within 30 days, **so that** I can act on at-risk medicine stock before it expires.

- Priority: High | Proposed Story Points: 3 | Source: FR-002
- Each medicine batch has an expiry date available to the stock-management system.
- A visual warning indicator appears next to batches whose expiry is within 30 days.
- The warning is visible to the staff member viewing the relevant batch list.

### US-02 - FEFO batch selection at checkout
**As a** pharmacy clerk, **I want** the system to select the valid batch with the nearest expiry date during sales checkout, **so that** medicines are dispensed in First-Expired-First-Out order.

- Priority: High | Proposed Story Points: 5 | Source: FR-001 | Dependency: US-01
- When a medicine is sold, the system compares the expiry dates of valid available batches.
- The batch with the nearest valid expiry date is selected first.
- A newer batch is not selected while an older unexpired batch is available.

### US-03 - FEFO dispensing list for the clerk
**As a** pharmacy clerk, **I want** to generate a dispensing list sorted by batch expiry date, **so that** I can retrieve stock in the correct FEFO order.

- Priority: High | Proposed Story Points: 3 | Source: FR-003 | Dependency: US-01
- The system generates a dispensing list for the pharmacy clerk.
- Batches with the nearest valid expiry dates appear at the top.
- The displayed order is expiry-date ascending.

### US-04 - Automatic draft purchase order creation
**As an** inventory manager, **I want** the system to create a draft purchase order when an item reaches its predefined minimum stock threshold, **so that** replenishment work begins before a medicine shortage occurs.

- Priority: Medium | Proposed Story Points: 5 | Source: FR-004
- A minimum stock threshold can be defined for an item.
- When stock falls below the configured minimum, the system creates a draft purchase order immediately.
- The draft contains the item and the stock-trigger context needed for staff review.

### US-05 - Secure and timely supplier purchase-order dispatch
**As a** purchasing manager, **I want** the system to generate and dispatch a supplier purchase-order request when stock dips below the safety threshold, **so that** replenishment requests are sent reliably and securely.

- Priority: High | Proposed Story Points: 8 | Source: NFR-001 | Dependency: US-04
- The system automatically generates and dispatches a supplier purchase-order request when the safety threshold is crossed.
- Benchmarking is performed under simulated peak load.
- Benchmark evidence is checked against latency and security targets agreed by the team/instructor. Lab 1 does not specify numeric target values; do not invent them.

### US-06 - Supplier view of dispatched purchase orders
**As an** inventory supplier, **I want** to view purchase orders dispatched to me, **so that** I can see the orders that require supplier action.

- Priority: Medium | Proposed Story Points: 3 | Source: FR-005 | Dependency: US-05
- The supplier-facing view displays dispatched purchase orders.
- All system-dispatched purchase orders are visible in the supplier interface.
- The supplier can distinguish dispatched orders in the list.

### US-07 - Pharmacy-hours service availability
**As a** pharmacy administrator, **I want** the stock-management engine to remain available for 99.9% of pharmacy operating hours, **so that** pharmacy stock operations can continue reliably.

- Priority: High | Proposed Story Points: 8 | Source: NFR-002
- Availability is monitored or logged during pharmacy operating hours.
- Availability evidence demonstrates 99.9% uptime.
- Downtime remains below 43 minutes per month, as stated in Lab 1.

## Proposed estimate and order

| Order | Story | Priority | Points |
|---:|---|---:|---:|
| 1 | US-01 Expiry tracking | High | 3 |
| 2 | US-02 FEFO checkout | High | 5 |
| 3 | US-03 FEFO dispensing list | High | 3 |
| 4 | US-05 Secure dispatch | High | 8 |
| 5 | US-07 Availability | High | 8 |
| 6 | US-04 Draft purchase order | Medium | 5 |
| 7 | US-06 Supplier view | Medium | 3 |
| | **Total** | | **35** |

Points are proposed starting estimates on the handout's scale. They must be validated by the team through Planning Poker. They are not actual votes.

## Proposed Sprint 1 - FEFO Core

- Duration: one week; proposed dates 2-9 November 2026, subject to instructor/team confirmation.
- Goal: track batch expiry dates, warn on batches expiring within 30 days, select the nearest valid batch at checkout and produce the clerk FEFO list.
- Selected Stories: US-01 (3) + US-02 (5) + US-03 (3) = **11 points**.
- Reason: all three are High priority and form one dependent workflow. US-01 establishes expiry-date data required by US-02 and US-03.
- Remaining Stories stay in the backlog for later sprint planning.

## After Jira setup

Create the three Epics first, then the seven Stories; link each Story to its Epic; enter priorities and agreed Story Points; create Sprint 1 for one week; add US-01, US-02 and US-03; start the sprint; simulate To Do -> In Progress -> Done; and capture the actual Burndown Chart from Jira Reports.