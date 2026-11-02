# Reusable Jira Lab 2 Manual

A step-by-step guide for converting **any student's Lab 1 scenario** into a Jira Agile backlog and two one-week sprints.

## 1. Gather your Lab 1 source material

Keep these open while working:

- Functional requirements table, including IDs, priorities and acceptance criteria.
- Non-functional requirements such as performance, security, reliability and usability.
- Use-case diagram, especially actors and their goals.
- Use-case flow / descriptions, including normal and alternative flows.
- Business rules and measurable thresholds.

Create a source inventory. Each Epic and Story should trace to at least one Lab 1 requirement or use case. Do not add features that cannot be traced to the assigned scenario.

## 2. Convert requirements to Epics

An Epic is a large body of related work divided into smaller Stories. Group requirements by user-visible outcome or functional theme, not by programming language, team member or screen.

1. Cluster related requirements serving one business goal.
2. Give each Epic a short outcome-oriented name (for example, Inventory Control or Report Generation).
3. Write a 1-3 sentence description of the capability and user value.
4. Keep the Epic count manageable (often 2-5 for a small lab scenario, depending on scope).
5. Map each major functional requirement to at least one Epic. Attach NFRs to relevant Stories or a quality/reliability Epic where appropriate.

| Epic name | Description / outcome | Lab 1 IDs / use cases |
|---|---|---|
| [EPIC 1] | [Outcome this Epic enables] | [FR/NFR/UC IDs] |
| [EPIC 2] | [Outcome this Epic enables] | [FR/NFR/UC IDs] |
| [EPIC 3] | [Outcome this Epic enables] | [FR/NFR/UC IDs] |

## 3. Write User Stories

Use the exact format required by the handout:

> As a **[user role]**, I want **[goal / capability]**, so that **[benefit / value]**.

- User role: choose a real actor from your Lab 1 use-case diagram (customer, admin, clerk, student, supplier, etc.).
- Goal: state what the actor needs the system to do, not the developer's implementation task.
- Benefit: explain why that goal matters.

Add observable acceptance criteria. Prefer Given / When / Then or clear pass conditions. Copy numeric thresholds from Lab 1; never invent missing values.

| Story field | Template |
|---|---|
| Title | [Actor goal] |
| User story | As a [role], I want [goal], so that [benefit]. |
| Acceptance criteria | Given [precondition], when [action], then [observable result]. |
| Traceability | [FR/NFR/UC IDs] |
| Dependency | [Story that must come first, or None] |

## 4. Prioritise the backlog

The handout asks for High, Medium and Low priority based on user impact.

| Priority | Meaning |
|---|---|
| High | Core user journey, critical business process, safety/security, or high user impact. |
| Medium | Important function that improves completeness or supports the main process but is not the first blocker. |
| Low | Convenience, polish or lower-impact enhancement that can wait. |

Give every Story a priority, order the backlog from highest to lowest, and use dependency order as a tie-breaker. Priority is importance, not effort.

## 5. Estimate Story Points using Planning Poker

The Lab 2 handout lists the values 0, 1, 2, 3, 5, 8, 13, 20, 40 and 100. Story Points represent relative effort, complexity and uncertainty—not hours or days.

1. Read one Story and its acceptance criteria.
2. Each team member privately chooses a point value.
3. Reveal estimates together.
4. If estimates differ, ask the highest and lowest estimators to explain their reasoning.
5. Clarify assumptions, split oversized Stories, and vote again until the team agrees.
6. Enter the agreed value in Jira Story Points and record it in your notes.

If doing the lab individually, call it an individual estimate, not a team Planning Poker consensus.

## 6. Create a company-managed Scrum project in Jira

Follow current UI labels if they differ slightly from the handout screenshots.

1. Log in to Jira and open Projects / Create project.
2. Choose Software Development / Jira Software.
3. Select the Scrum template. The lab requires Sprint planning and a Burndown Chart, so do not choose Kanban.
4. Choose Company-managed project type, as the handout specifies.
5. Enter a project name and unique short key for your own Lab 1 scenario.
6. Create the project and open its Backlog / Scrum board.

Reuse an existing project only if it belongs to this assignment and supports a Scrum backlog, Epic, Story and Story Points. Do not put a new unrelated scenario into a project already used by another application/team.

## 7. Create Epics and Stories

1. Open Backlog. Enable the Epic panel if it is hidden (the handout notes the E shortcut or Epic panel control).
2. Click Create and choose work type **Epic**. Enter its name/summary and description. Create all Epics first.
3. For each Epic, choose Create work item / Create issue and select work type **Story**.
4. Enter the Story title as Summary. Put the full user-story text and acceptance criteria in Description.
5. Link the Story to the correct Epic using Parent / Epic Link (the label varies by Jira version).
6. Verify that the Story appears under the correct Epic in Backlog. Repeat for all Stories.

## 8. Set priority and Story Points

1. Open each Story and set Priority to High, Medium or Low.
2. Find Story Points in issue details or More fields (some Jira layouts place it in the right-side detail panel).
3. Enter the value agreed through Planning Poker.
4. Return to Backlog and verify that priorities and estimates appear correctly.
5. Open each Epic and check its Stories and point totals. Reorder Stories so higher-priority work appears first, respecting dependencies.

## 9. Plan and run Sprint 1

The handout specifies a one-week Sprint. Select only a realistic subset based on priority, dependencies and team capacity.

1. In Backlog, click Create sprint and name it Sprint 1.
2. Drag/select the Stories the team commits to. Record the planned Story Point total.
3. Write one Sprint Goal describing the user outcome.
4. Click Start sprint; set the one-week start and end dates; confirm.
5. Open Active Sprints. Selected Stories should appear in To Do.
6. Simulate progress by moving each selected Story through **To Do -> In Progress -> Done**. The handout says to wait a few minutes between stages.
7. Mark an issue Done only after the simulation/acceptance is complete. Do not change unrelated backlog issues.
8. Click Complete sprint to end Sprint 1. The Lab 2 handout explicitly says to finish two sprints.
9. Create Sprint 2, choose the next coherent group of prioritised Stories, set a one-week duration and Sprint Goal, start it, simulate To Do -> In Progress -> Done, then complete it. Do not force all remaining backlog work into Sprint 2 if it exceeds realistic capacity.

## 10. View the Burndown Chart

1. Open Reports from the board.
2. Choose Burndown Chart.
3. Confirm it is the intended Sprint 1; select Story Points as the estimation statistic if available.
4. The remaining-work line shows work left; the guideline shows approximate linear progress.
5. The red line represents remaining estimated work; the grey guideline approximates linear progress. A red line below the guideline means the team is ahead of that guideline; above it may mean the team is behind.
6. Observe flat periods, sharp drops, scope changes or early/late completion. A sharp drop can indicate late completion or that work was not broken down/estimated well.
7. Review the chart for the completed sprint(s) and capture genuine Jira screenshots showing the chart and sprint timeline.

**Evidence must be real.** Do not submit an illustrative chart as Jira evidence. Use the report from the sprint you actually ran.

## 11. Answer the four reflection questions

| Handout question | What to cover |
|---|---|
| Did your estimations reflect the actual effort? | Compare estimated points with what happened; identify over/under-estimated Stories. |
| Was your backlog well-prioritized? | Explain High/Medium/Low ordering, user impact and dependencies. |
| How did your simulated sprint align with your plan? | Compare Sprint Goal/planned points with Stories moved to Done and any scope changes. |
| What insights did the burndown chart give about your team's capacity? | Describe the remaining-work line, flat sections or sharp drops and what they suggest about pace/capacity. |

Use ticket names, points and observations from your Jira board. Do not make claims unsupported by the chart.

## 12. Submission checklist

- [ ] Backlog screenshot showing Epics and their Stories.
- [ ] Story Point / priority evidence.
- [ ] Active Sprint screenshot with To Do, In Progress and Done columns.
- [ ] Burndown Chart screenshot(s) from Jira Reports after the sprint run(s).
- [ ] Brief reflection document answering all four questions.
- [ ] Organise the evidence under LAB 2 in the course repository, if required by your instructor.
- [ ] Demonstrate the Jira workspace to the instructor (the handout explicitly requires this).

## 13. Common mistakes

- Writing implementation tasks as Stories without a user role or benefit.
- Creating too many tiny Epics instead of grouping functional themes.
- Missing acceptance criteria or Epic links.
- Confusing priority with Story Points.
- Calling guessed estimates Planning Poker consensus.
- Putting the entire backlog into Sprint 1.
- Marking Stories Done without simulating the workflow.
- Submitting an illustrative chart instead of a real Jira Burndown Chart.