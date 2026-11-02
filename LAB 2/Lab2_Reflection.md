# Lab 2 - Sprint Reflection

**Scenario:** Pharmacy Inventory Management  
**Jira board:** [Pharmacy Lab 2 - Scrum Board](https://aiml-team-se-5c.atlassian.net/jira/software/c/projects/SL/boards/36)  
**Jira issue prefix:** `SL-15` to `SL-24`  
**Execution date:** 2 November 2026  
**Execution type:** Jira sprint simulation. Both sprint records were closed on the execution date; the planned one-week periods did not elapse.

## 1. Did your estimations reflect the actual effort?

The seven Stories were assigned estimates totalling 35 points: 3, 5, 3, 5, 8, 3 and 8. These estimates were successfully saved in Jira's Story point estimate field. In the first simulation, 3 of 11 planned points were in Done, 5 points remained In Progress and 3 points remained To Do when Sprint 1 was closed. In the second simulation, 5 of 16 planned points were in Done, 8 points remained In Progress and 3 points remained To Do when Sprint 2 was closed. These status results show that the planned work was not fully completed in either simulation. They do not, by themselves, prove whether an individual Story was over- or under-estimated, because actual time/effort was not measured and the team did not conduct a recorded Planning Poker vote.

## 2. Was your backlog well-prioritized?

The backlog places the FEFO workflow first because expiry tracking is a dependency for correct batch selection and the clerk's dispensing list. Secure purchase-order dispatch and operational availability were also marked High because they affect replenishment reliability and continuity of pharmacy operations. Draft purchase-order creation and supplier visibility were marked Medium. The actual Jira priority values were saved on all seven Stories. This is a defensible initial ordering from the Lab 1 requirements; a team Planning Poker / backlog refinement session could still change it.

## 3. How did your simulated sprint align with your plan?

Sprint 1 was planned with US-01, US-02 and US-03 for 11 points. At closure, US-01 (3 points) was Done, US-02 (5 points) was In Progress and US-03 (3 points) was To Do. Sprint 2 was planned with US-04, US-05 and US-06 for 16 points. At closure, US-04 (5 points) was Done, US-05 (8 points) was In Progress and US-06 (3 points) was To Do. Both Jira sprint records were closed on 2 November 2026, shortly after they were started. Therefore this was a status-transition simulation, not a full week of elapsed team work. The sprint goals and issue allocations were entered in Jira, but the planned work was only partially marked Done.

## 4. What insights did the burndown chart give about your team's capacity?

A genuine Jira Burndown Chart screenshot was not captured, and the connector did not return the chart report itself. Therefore no reliable conclusion about team capacity or the burndown trend can be made. The status outcomes show partial completion in both simulations, but they are not a substitute for the chart. The final submission still needs screenshots of the actual Jira Burndown Chart for each sprint, captured from Jira Reports.

---

## Jira issue register

| Key | Story | Estimate | Priority | Status at simulation close |
|---|---|---:|---|---|
| [SL-18](https://aiml-team-se-5c.atlassian.net/browse/SL-18) | Expiry tracking and near-expiry warnings | 3 | High | Done |
| [SL-19](https://aiml-team-se-5c.atlassian.net/browse/SL-19) | FEFO batch selection at checkout | 5 | High | In Progress |
| [SL-20](https://aiml-team-se-5c.atlassian.net/browse/SL-20) | FEFO dispensing list for the clerk | 3 | High | To Do |
| [SL-21](https://aiml-team-se-5c.atlassian.net/browse/SL-21) | Automatic draft purchase order creation | 5 | Medium | Done |
| [SL-22](https://aiml-team-se-5c.atlassian.net/browse/SL-22) | Secure and timely supplier PO dispatch | 8 | High | In Progress |
| [SL-23](https://aiml-team-se-5c.atlassian.net/browse/SL-23) | Supplier view of dispatched POs | 3 | Medium | To Do |
| [SL-24](https://aiml-team-se-5c.atlassian.net/browse/SL-24) | Pharmacy-hours service availability | 8 | High | To Do (backlog) |

## Submission evidence status

The Jira Epics, Stories, priorities, estimates and two sprint simulations are present. The required PNG screenshots are **not yet in the repository**. The board is filed under the existing company-managed `SE-Labwork (SL)` project because a separate Jira project could not be provisioned through the connected Jira operations. Its current board filter is the project-wide filter, so unrelated `SL` issues may also appear. Do not present it as an isolated pharmacy project or submit fabricated screenshots.
