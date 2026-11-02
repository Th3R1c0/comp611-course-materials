# Cheatsheet coach: requested changes log

Misty's feedback from testing the `cheatsheet-coach` skill, to use when improving it.
Status: **applied in trial** = done by hand in the test thread, not yet written into SKILL.md.

| # | Date | Change requested | Status |
|---|---|---|---|
| 1 | 2026-11-02 | **Assume no maths notation. Teach from zero / first principles.** Explain every symbol (n, f(n), ≤, log, n², O/Ω/Θ…) in plain English before using it, with small worked numbers. | applied in trial |
| 2 | 2026-11-02 | **Cheatsheet is HTML while studying.** Every line on the sheet is expandable and reveals a simple plain-English explanation of everything in that line. | applied in trial (Week 1) |
| 3 | 2026-11-02 | **Final cheatsheet is a PDF with no expanders**, just the lines. The expand view is only a study aid to keep reminding what things mean. | noted for final assembly |
| 4 | 2026-11-02 | **Keep a log of requested skill changes** (this file) whenever Misty says so. | applied |
| 5 | 2026-11-02 | **Teach week by week** following the course schedule (Week 1, 2, 3…) instead of grouping by quiz topic. | applied in trial |
| 6 | 2026-11-02 | **Practice questions as a bank: 5 questions per topic inside each week**, covering all of that week, from course content (not one question at a time). | applied in trial (Week 1: 30 Qs) |
| 7 | 2026-11-02 | **Full plain-English sentences on every sheet line**, with an example, not shorthand. | applied in trial (Week 1 v3) |
| 8 | 2026-11-02 | **Every rule includes the "why"** (e.g. why we count steps, not seconds). | applied in trial (Week 1 v3) |
| 9 | 2026-11-02 | **Define every term before it's used**: a glossary of every word the questions use (step count, worst case, auxiliary space…). | applied in trial (Week 1 v3, [AA-0]) |
| 10 | 2026-11-02 | **Findable headings named the way exam questions name things**; no burying ideas inside other entries (e.g. "Properties of an algorithm" gets its own entry). | applied in trial (Week 1 v3) |
| 11 | 2026-11-02 | **Coverage check before questions**: every practice question must be answerable from the sheet alone; tag each question with its entry and fix the sheet if it isn't. | applied in trial (all 30 Week 1 Qs re-tagged) |
| 12 | 2026-11-02 | **Explanations shown open by default** in the study version (button to hide them). | applied in trial (Week 1 v3) |
| 13 | 2026-11-02 | **Stop and fix when the sheet fails**: pause the questions, fix the sheet, re-teach, then resume. | applied in trial |
| 14 | 2026-11-02 | **Keep every previous version of each cheatsheet** so the student can go back (revision/cheatsheets/versions/, older HTML versions published separately). | applied in trial (v1, v2 kept) |
| 15 | 2026-11-02 | **Three view modes built into the study sheet**: Paper (just the lines, like the printed exam sheet, to get used to no toggles), Everything shown (lines + explanations, no tapping), Tap to explain (toggles). Default: Paper. | applied in trial (Week 1 v3) |
| 16 | 2026-11-02 | **Cumulative recap after every topic (mini spaced repetition)**: after finishing topic k, give new questions covering every question type from topics 1..k; student answers out loud, Claude corrects all, then move on. After the last topic, recap everything, then do everything once more to finish. | applied in trial (recap 1–3) |
| 17 | 2026-11-02 | **Fast lesson page per topic (or group of topics)**: plain English → fast steps per question type → worked examples → "your turn" pointing to the exact questions. Misty's favourite format. | applied in trial (topic 3, topics 4–6 pages) |
| 18 | 2026-11-02 | **Teach by question type**: list every kind of question a topic can ask (Case A/B/C…), give a short numbered recipe for each; steps first, the "why" optional underneath. | applied in trial |
| 19 | 2026-11-02 | **Translate notation into English before solving** (O = at most, Ω = at least, Θ = exactly; "=" means "fits the description"; c goes on the right). Include how to say it out loud. | applied in trial (sheet v4) |
| 20 | 2026-11-02 | **Use a picture when an idea is abstract** (e.g. the ceiling/floor graph for c and n₀). | applied in trial |
| 21 | 2026-11-02 | **Worked examples show every number**, use numbers doable without a calculator; for bounds, check at n₀ and at a big n like 100. | applied in trial |
| 22 | 2026-11-02 | **Correction style**: ✓/✗ each answer, name exactly what was misread (e.g. "you divided the n's, not the times"), give the right step, then a quick redo of only the missed ones. | applied in trial |
| 23 | 2026-11-02 | **New cheatsheet version after every round of mistakes**: rewrite only the failed entries, keep every old version linked at the top, log which mistake each edit fixes (progress.md). | applied in trial (v4, v5) |
| 24 | 2026-11-02 | **Glossary covers every word**, including ones that tripped the student up: term, constant, how to read `for i = 1 to n`. | applied in trial (sheet v4/v5) |
| 25 | 2026-11-02 | **Key tables live in the sheet lines themselves** so they show in Paper view, and must fit a phone without sideways scrolling. | applied in trial (sheet v5) |
| 26 | 2026-11-02 | **Handle speech-to-text**: interpret garbled words ("circle" → ceiling, "0" → O, "4 in 2" → 4n²) and correct gently without losing the answer. | applied in trial |
| 27 | 2026-11-02 | **Let the student group topics**: if they ask for several topics at once, make one combined lesson page. | applied in trial (topics 4–6) |
| 28 | 2026-11-02 | **Propose before logging**: when the student gives feedback, suggest improvements and log only the ones they pick. | applied |

## Suggested SKILL.md edits (draft)
- Teach step: "Assume the student knows no mathematical notation unless they say otherwise. Introduce each symbol in plain words with a numeric example, and add a symbol-key entry at the top of each sheet."
- Cheatsheet step: "Write the study sheet as `revision/cheatsheets/<NN>-<slug>.html`. Each sheet line is a `<details>` row: the summary is the exact line for the printed sheet, the body is a plain-English explanation from first principles."
- Final assembly: "Build `cheatsheet-final.pdf` from the summary lines only (no explanations), within the one-A4-single-sided limit."
- Sections: "Order sections by course week unless the student asks otherwise."

## Open question
- Full sentences make the study sheet long. The final PDF must fit Week 1 into about 1/8 of one A4 side, so the final version will need shortened lines. Decide how to shorten when building the final PDF.
