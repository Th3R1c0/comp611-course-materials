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

## Suggested SKILL.md edits (draft)
- Teach step: "Assume the student knows no mathematical notation unless they say otherwise. Introduce each symbol in plain words with a numeric example, and add a symbol-key entry at the top of each sheet."
- Cheatsheet step: "Write the study sheet as `revision/cheatsheets/<NN>-<slug>.html`. Each sheet line is a `<details>` row: the summary is the exact line for the printed sheet, the body is a plain-English explanation from first principles."
- Final assembly: "Build `cheatsheet-final.pdf` from the summary lines only (no explanations), within the one-A4-single-sided limit."
- Sections: "Order sections by course week unless the student asks otherwise."

| 6 | 2026-11-02 | **Practice questions as a bank: 5 questions per topic inside each week**, covering all of that week, from course content (not one question at a time). | applied in trial (Week 1: 30 Qs) |
