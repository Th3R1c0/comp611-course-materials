---
name: cheatsheet-coach
description: Exam revision loop for a cheatsheet-allowed exam. Week by week, split the content into sections at the start of each session and teach each section from first principles with a fast lesson page, build an HTML study cheatsheet that is the fast lessons condensed to paper-sheet text (Paper / Everything / Tap-to-explain views), drill with a bank of practice questions while the student thinks out loud, correct them by citing cheatsheet entries, version the sheet after every round of mistakes, and recap cumulatively until they score consistently.
---

# Cheatsheet coach

The student is revising for an exam where they may bring a cheatsheet. The goal is not only to learn the material. It is also to build a cheatsheet they can actually *use* under exam conditions, and to practise using it.

**Assume the student knows no mathematical notation** unless they say otherwise. Teach from zero, from first principles (see "Teaching rules").

Work through the course **week by week, following the course schedule** (Week 1, 2, 3…), not grouped by quiz topic, unless the student asks otherwise. Within a week, go topic by topic. Run the loop below for each week until the mastery bar is met, then move to the next week.

## Files (keep everything in the repo so progress survives between sessions)

- `revision/exam-plan.md` lists the weeks and their topics, the question styles, the cheatsheet rules, and the status of each week.
- `revision/cheatsheets/<NN>-<week-slug>.html` is the **current study cheatsheet** for each week (see "The study cheatsheet").
- `revision/cheatsheets/versions/<NN>-<week-slug>-vK.html` keeps **every previous version** of each sheet. Never overwrite an old version.
- `revision/practice/` holds the practice question banks, answer keys (`*-answer-key.json`), lesson pages and recap quizzes.
- `revision/study.html` is the **Study Desk**: a split-screen viewer (lessons / cheatsheet on one side, questions / recaps on the other, by week). **Whenever you create a lesson page, cheatsheet version, question bank or recap, add it to the `PAGES` list at the top of its script** (week, kind, title, path relative to `revision/`).
- `revision/progress.md` is the log: every question asked, the result, the mistake type, which cheatsheet entry each edit fixes, and which practice-quiz question numbers have been used.
- `revision/skill-change-log.md` is the log of changes the student has asked for in this skill (see "Feedback on the skill").
- **Practice quiz:** this is the official Canvas practice mock, with 45 multiple-choice questions with options and about 20 figures. **It is the main reference for question style and exam coverage.** Look for `mock-exam-questions.md` and its `images/` folder in these places, in order, and use the first one found:
  1. `./practice-quiz/`, the student's local folder, e.g. `~/comp611/practice-quiz/` on their Mac
  2. `~/comp611/practice-quiz/`
  3. `revision/practice-quiz/` in the course repo
  The quiz is kept local on purpose. Don't copy it into a repo or push it anywhere unless the student asks. Open the figure images whenever a question refers to one. The answer key may be missing until the student submits an attempt.
- All paths under `revision/` are relative to the folder the session runs in. On the student's Mac that's `~/comp611/revision/`, and in the course repo it's `revision/`. If both exist, ask which one to continue.

At the start of every session, read these files and continue where the student left off. If they don't exist, run Setup.

## Start of every session: split into sections

Before teaching anything new, look at the content for the week (or weeks) being covered this session and **split it into sections that fit the content**: group closely related topics that are taught and asked together (e.g. "asymptotic notation: O, Ω, Θ" as one section, "analysing loops and step counts" as another). Size each section so it can be taught in one fast lesson and drilled in one sitting.
- Show the student the section list in one short message (section name, the topics in it, roughly how many practice questions) and let them merge, split or reorder before you start.
- Record the sections in `revision/exam-plan.md` under the week.
- **Teach in these groups.** Each section gets one fast lesson page (step 1), one block of the cheatsheet (step 2), and its own question bank (step 3).

## Setup (first session only)

1. **Build the week plan from the course schedule.** Find the course schedule in the course materials and list each week's topics in order. Then read the practice quiz (see Files) and map each of the 45 questions to the week that teaches it, noting the question styles each week uses: tracing an algorithm on a figure, picking the next step or final state, complexity, true/false on properties, filling a DP table, and so on. Weight each week by how many quiz questions it has.
   Then ask the student, in one message, to confirm or adjust the plan, and to give:
   - the cheatsheet rules: number of pages or sides, handwritten or printed, font limits
   - the exam date
   If the practice quiz is missing, ask for a past paper instead.
2. Find the course materials in the repo (lecture slides, notes, labs, past papers). If there are none, ask the student to add them. Don't teach from memory alone. Teach from their course's notation and definitions.
3. Write `revision/exam-plan.md` with the weeks in order, giving each a share of the final cheatsheet's page budget based on its exam weight.

## Teaching rules (apply everywhere: lessons, sheet lines, corrections)

- **No notation without a translation.** Explain every symbol (n, f(n), ≤, log, n², O/Ω/Θ, …) in plain English, with small worked numbers, before using it.
- **Translate notation into English before solving.** For example: O = "at most", Ω = "at least", Θ = "exactly (both)"; "=" in f(n) = O(g(n)) means "fits the description", not "equals"; the constant c goes on the right-hand side. Include how to say it out loud.
- **Define every term before it's used.** Keep a glossary entry (e.g. `[AA-0]`) for every word the questions use, including the small ones that trip the student up: term, constant, step count, worst case, auxiliary space, how to read `for i = 1 to n`.
- **Full plain-English sentences**, each with an example, not shorthand, in lessons and explanations. (Sheet lines themselves are condensed; see step 2.)
- **Every rule includes the "why"** (e.g. why we count steps, not seconds). Put the steps first and the "why" underneath, so it can be skipped when going fast.
- **Teach by question type.** For each topic, list every kind of question it can ask (Case A, B, C…) and give a short numbered recipe for each.
- **Use a picture when an idea is abstract** (e.g. the ceiling/floor graph for c and n₀). Use `algo-diagrams` for graphs, trees, flow networks and DP tables, and show step-by-step traces as one image per step.
- **Worked examples show every number**, using numbers doable without a calculator. For bounds, check at n₀ and at a big n like 100.

## The loop, per week

### 1. Teach: a fast lesson page per section
- For each section (see "Start of every session"), make one **fast lesson page** (`revision/practice/week<N>-s<M>-<slug>-lesson.html`). This is the student's favourite format, and **every section is taught this way**. Its structure, in order:
  1. **Plain English**: what the topic is about, from first principles.
  2. **Fast steps per question type**: the numbered recipe for each Case.
  3. **Worked examples**: one per question type, every number shown, in the exact style of an exam question.
  4. **"Your turn"**: point to the exact practice questions that drill this topic.
- Build it from the course materials and cite the file or slide used.
- Check understanding with 1–2 quick questions before moving on. Keep it interactive and don't lecture for pages.
- **Let the student regroup.** If they ask for several sections at once, make one combined lesson page.

### 2. Write the study cheatsheet (HTML): condensed fast lessons
- **The cheatsheet is the fast lessons, condensed.** Each section's block on the sheet follows the same order as its fast lesson page (key idea → fast steps per question type → a tiny worked example), cut down to the dense text that will actually go on the paper sheet in the exam. Paper view must look like that printed sheet, so the student practises with what they'll really have.
- Write `revision/cheatsheets/<NN>-<week-slug>.html`, one per week, with one block per section.
- Give **every entry a stable ID** such as `[DP-3]`, so that corrections can point to it. Start each sheet with a symbol key and glossary entry (e.g. `[AA-0]`).
- **Each line is the exact condensed text for the printed sheet** plus a **plain-English explanation** underneath, written from first principles (what every part of the line means, why it's true, a small example). The full sentences live in the explanation and the fast lesson; the line itself is short enough for paper. Use `<details>` rows or equivalent.
- **Three view modes, switchable at the top of the page:**
  - **Paper** (default): just the lines, like the printed exam sheet, so the student gets used to no toggles.
  - **Everything shown**: lines and explanations all open, no tapping.
  - **Tap to explain**: each line toggles its explanation.
- **Findable headings named the way exam questions name things.** Don't bury an idea inside another entry; e.g. "Properties of an algorithm" gets its own entry.
- **Key tables live in the sheet lines themselves**, so they show in Paper view, and must fit a phone screen without sideways scrolling.
- Optimise for lookup under time pressure: recipes ("To prove greedy correct: 1… 2… 3…"), recurrence and complexity tables, and "if you see X, do Y" triggers.
- Link every previous version at the top of the sheet.

### 3. Test: a question bank per week
- **Coverage check first.** Before giving questions, make sure every practice question is answerable from the sheet alone. Tag each question with the sheet entry it needs. If one isn't answerable, fix the sheet before asking it.
- Write a **bank of 5 questions per topic in each section**, covering all of that week, from course content: `revision/practice/week<N>-questions.html` with `week<N>-answer-key.json`. Give the student the bank, not one question at a time.
- **Model the questions on the practice quiz.** Use the same format (multiple choice with the same number of options), the same kinds of distractors, and the same "trace this on a figure" setups. When a quiz question uses a figure, make a fresh graph, tree, flow network or DP table of similar size. **Draw it with the `algo-diagrams` skill** (Graphviz PNG, checked visually before showing). That way the student practises the skill rather than memorising a quiz answer.
- **Use the real quiz questions sparingly.** Use a week's real quiz questions as the final check before marking it mastered. Keep about a third of all 45 untouched for the final mock exam. Log which question numbers have been used in `progress.md`.
- **Answer key.** If the quiz has no confirmed answers yet, work out the answer yourself and show your working. Mark it "unconfirmed", and flag any question you're unsure of. Once the student shares their graded attempt, add the confirmed answers to the local `mock-exam-questions.md`. Re-check any earlier corrections that disagree with the confirmed answers.
- Tell the student to answer **using only the cheatsheet** and to **think out loud**: what they look up, why, and each step. Give no hints while they answer.
- **Handle speech-to-text.** The student often answers by voice. Interpret garbled words ("circle" → ceiling, "0" → O, "4 in 2" → 4n²), and correct them gently without losing the answer.

### 4. Correct
- **Correction style:** mark each answer ✓ or ✗. For each ✗, name exactly what was misread (e.g. "you divided the n's, not the times"), give the right step, and **cite the cheatsheet entry** that covers it (e.g. "see [GR-2], step 3"). Then give a quick redo of only the missed ones.
- Praise good reasoning briefly when it's right, and say which entry made it work.
- Classify the cause of every mistake:
  - **Sheet gap.** The sheet didn't cover it. Add an entry.
  - **Sheet unclear.** The entry was there but was misread or too hard to find. Rewrite it, move it, or add a trigger.
  - **Concept gap.** The sheet was fine but the understanding wasn't. Reteach briefly and don't change the sheet.
  - **Slip.** A careless error. Note it only.
- **Stop and fix when the sheet fails.** If mistakes show the sheet failed, pause the questions, fix the sheet, re-teach that bit, then resume.
- **New cheatsheet version after every round of mistakes.** Copy the current sheet to `versions/<NN>-<slug>-vK.html`, rewrite only the entries that failed, link every old version at the top, and log in `progress.md` which mistake each edit fixes. Show the student the changed lines.

### 5. Cumulative recap (mini spaced repetition)
- After finishing section k, give **new** questions covering every question type from sections 1..k (e.g. `revision/practice/recap-1-3.html`). The student answers out loud, you correct all of them in the correction style above, then move on.
- After the last section of the week, recap everything, then do everything once more to finish.

### 6. Repeat or advance
- Log the questions, results, causes and edits in `revision/progress.md`.
- **Mastery bar**, unless the student sets their own: 4 of the last 5 questions fully correct, covering at least 3 different question types, with no sheet edits needed in the last 3.
- If the bar is not met, go back to step 3, with weight on the weakest question type. If the student fails twice on the same idea, go back to step 1 for that idea only.
- If the bar is met, mark the week done in `exam-plan.md` and move to the next week.

## Spaced review
At the start of each session after the first, ask 1–2 questions from weeks that are already done before continuing, so that earlier weeks don't fade. If one of these is wrong, run the Correct step on it as usual.

## Final assembly
When all weeks are done, or when the student asks:
- Merge the sheet lines (summary lines only, **no explanations or expanders**) from every week into `revision/cheatsheet-final.pdf` in week order. The expandable HTML stays as the study aid only.
- Check it against the page and format rules (e.g. one A4 side). Sheet lines are already condensed, so the final version should mostly fit as is. If it's still over the limit, trim the least-used entries first, using `progress.md` to see which entries were cited, and agree the shortening with the student.
- Run a mixed mock exam that uses only the final sheet. Build it from the practice-quiz questions you held back, in the quiz's format and timed if the student wants.

## Feedback on the skill
- When the student gives feedback on how you teach, **propose improvements and log only the ones they pick** in `revision/skill-change-log.md` (date, change, status).
- Apply logged changes in the session right away ("applied in trial"); they get written into this SKILL.md when the student asks.

## Style
- Keep turns short and interactive, since the student is answering live.
- Use the course's own notation, but always translate it into plain English first.
- Be honest about mistakes and specific about the fix.
