# Revision progress log

Practice-quiz question numbers used so far: none.

## 01 Algorithm analysis (trial round, 2026-11-02)

Question bank: revision/practice/week1-questions.html (30 Qs, 6 topics x 5). Answer key: revision/practice/week1-answer-key.json.

| # | Question | Type | Result | Cause | Sheet edits |
|---|---|---|---|---|---|
| 1.1–1.5 | Topic 1 attempt | definitions | stopped | sheet unclear/gap (terse, undefined terms) | rebuilt sheet v3 |
| 2.1–2.5 | Topic 2 | O/Ω/Θ true-false | taught, then 2.1 correct out loud | concept gap: "=" read as equal; term definition | none (Misty asked not to edit) |
| 3.1 | c, n₀ options | calculation | correct (A) | n₀ confused with a multiplier, fixed | none |
| 3.2 | Ω recipe | calculation | correct (B) | – | none |
| 3.3 | impossible bound | concept | taught (C) | "constant" and the hidden c×n ceiling | none |
| 3.4 | minus sign, smallest n₀ | calculation | method correct, answer B | wording: "first that passes" | none |
| 3.5 | which does NOT prove | calculation | correct (C) | – | none |

## Recap 1–3 (2026-11-02), 9/13
| Q | Result | Cause |
|---|---|---|
| R1.1–R1.4 | 4/4 | – |
| R2.1, R2.3, R2.4 | correct | – |
| R2.2 | wrong (picked Ω(n²) as true, rejected 10n=Θ(n)) | concept: same/slower/faster comparison reversed |
| R3.1 | blank: forgot "add the numbers" recipe | recall slip |
| R3.2 | correct | – |
| R3.3 | wrong (guessed n₀ must be 0) | didn't unpack O(1) into c×1 |
| R3.4 | not attempted (unsure) | recall of "smallest first" |
| R3.5 | correct letter, wrong reason (said n₀ too big) | c too small is the reason |
Weakest: topic 3 recall. Redo R2.2, R3.1, R3.3, R3.4 before topic 4.

### Sheet edits after recap 1–3 → version 4
- [AA-0] added "term" and "constant".
- [AA-6] rewritten in English (O = at most, Ω = at least, Θ = exactly; "=" means "fits the description"). Fixes R2.2.
- [AA-7] step-by-step to find the fastest term. [AA-8] new fast steps for judging any O/Ω/Θ statement (same / slower / faster). Fixes R2.2.
- [AA-9] split into "what c and n₀ mean" (c always on the right, n₀ replaces n, why c exists, ceiling picture) and [AA-9b] fast steps per question type (incl. O(1) hiding c × 1, smallest-first for minus sign, check n = 100). Fixes R3.1, R3.3, R3.4, R3.5 reason.
- v3 kept at revision/cheatsheets/versions/01-algorithm-analysis-v3.html.

## Topics 4–5 practice (2026-11-02)
| Q | Result | Cause |
|---|---|---|
| 4.2 | wrong: divided the n values, not the times | concept: ratio of times |
| 4.3 | wrong: 3 s (×k instead of ×k² for n²) | forgot to use the growth in brackets |
| 4.4 | correct (log n) | – |
| 4.5 | didn't know | apply "drop numbers, compare growth" |
| 5.2 | unsure | pattern-table lookup |
| 5.3 | correct (log n) | – |
| 5.5 | didn't know how to count lines | concept: inside loop = n, outside = 1, header = n+1 |
| 5.1, 5.4 | skipped | – |

### Sheet edits after topics 4–5 practice → version 5
- [AA-10] added "which is faster for very large n" steps (fixes 4.5).
- [AA-11] rewritten: divide the TIMES not the n values (fixes 4.2); "n gets k times bigger" uses the growth in the brackets: ×k, ×k², ×k³ (fixes 4.3).
- [AA-12] rewritten: what "for i = 1 to n" means; outside = 1, inside = n, for line = n + 1 (fixes 5.5); nested multiply / sequential add; pattern table on the sheet line itself (fixes 5.2).
- [AA-13] added insertion sort shifts = pairs in the wrong order.
- v4 kept at revision/cheatsheets/versions/01-algorithm-analysis-v4.html.

## 02 Divide and conquer (started 2026-11-02)

Sheet v1: revision/cheatsheets/02-divide-and-conquer.html (condensed from the three section lessons). Question bank: revision/practice/week2-questions.html (20 Qs), key week2-answer-key.json. Coverage check done: every question is tagged with the [DC-…] entry that answers it.
Practice-quiz Qs reserved for week 2 final check: 26, 36, 40, 44 (not used yet).

### Week 2 answers (2026-11-02)
| Q | Result | Cause | Sheet edits |
|---|---|---|---|
| 1.4, 1.5 | blank, asked for powers explained | concept gap: what a power is; [DC-4] had no "build back up" shortcut (sheet unclear) | explained in chat (halve-to-0 list, then work up from 1: even square, odd square × x); consider adding to [DC-4] |
| 2.1 | correct (D) | read 2T(n/2) as "2n": T notation (concept gap) | none yet; [DC-0] defines T |
| 2.4 | correct (C) | wording: "n grows over n²" → loop in loop = n × n | none |
| 3.1 | stuck: didn't know how to draw a recursion tree | lesson/sheet gap: [DC-6] assumes you can draw the tree; needs "jobs handing out jobs" story + concrete-number picture | taught in chat with figure w2-tree-2T-n3.png; fix [DC-6] in next sheet version |
| 3.1 | correct after teaching (9 nodes, n/16) | – | – |

### Sheet edits → version 2 (2026-11-02)
- Misty asked for a worked example under the lines, so they can copy the method. Added example lines (shown on Paper view) to [DC-2], [DC-3], [DC-4] (plus the POWER shortcut: halve to 0, then work up from 1), [DC-5], [DC-6] (Misty's own 3T(n/4)+n² level-2 example), [DC-8]. Fixes 1.4/1.5 blank and 3.1 stuck.
- [DC-6] new first line "Draw it" (1 box on top, a boxes under each, ÷ b each level). Fixes 3.1.
- [DC-6] shortcut a ÷ bᵏ for same/shrink/grow.
- v1 kept at revision/cheatsheets/versions/02-divide-and-conquer-v1.html.
