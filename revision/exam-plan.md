# COMP611 exam plan

Source: `A Assignments/COMP611_Final_Exam_Information_2026.pdf` (course export, release `course-export`).

- **Exam:** Friday 6 November 2026, 2 hours (+5 min reading). 45 MCQs, 2 or 3 marks each, 100 marks, one correct answer, no negative marking. Canvas quiz on campus.
- **Cheatsheet rules:** ONE A4 sheet, **single sided**, handwritten or printed. Handed in with student ID written on it.
- Also allowed: non-programmable calculator, one blank A4 scrap sheet.

## Sections (taught week by week, at Misty's request)

Page budget = share of one A4 side, by marks.

| # | Week | Section | Qs | Marks | Sheet share | Status |
|---|---|---|---|---|---|---|
| 01 | 1 | Algorithm fundamentals & asymptotic analysis | 5 | 12 | ~12% | in progress (trial) |
| 02 | 2 | Divide and conquer & recurrences (Master Theorem) | 4 | 10 | ~10% | in progress (sheet v1) |
| 03 | 3 | Graph representation, BFS, Dijkstra | 5 | 10 | ~10% | in progress (sheet v1) |
| 04 | 4 | Bellman-Ford, Floyd-Warshall | 3 | 6 | ~6% | |
| 05 | 5 | DP, LIS, edit distance | 5 | 12 | ~12% | |
| 06 | 7 | Greedy (interval scheduling, Prim, Kruskal) | 4 | 8 | ~8% | |
| 07 | 8 | Flow networks & max flow | 4 | 10 | ~10% | |
| 08 | 9 | Binary search trees | 3 | 6 | ~6% | |
| 09 | 9 | Red-black trees | 4 | 9 | ~9% | |
| 10 | 10 | Interval trees (augmenting DS) | 3 | 6 | ~6% | |
| 11 | 11 | B-trees | 3 | 6 | ~6% | |
| 12 | 11 | Disjoint set forests (union-find) | 2 | 5 | ~5% | |

Question styles (from the exam info): definitions/properties, small calculations, tracing on a small input, reading pseudocode/graphs/trees, recurrences & Master Theorem, time/space best/worst case.

## Week 2 sections (2026-11-02)

Practice-quiz questions for week 2: Q26 (base case), Q36 (recurrence from pseudocode), Q40 and Q44 (Master Theorem). Held back for the final check.

| Section | Topics | Sheet | Lesson | Practice Qs |
|---|---|---|---|---|
| 1 | D&C idea (divide/conquer/combine, base case); binary search, MERGE and fast exponentiation traces | [DC-0] to [DC-4] | practice/week2-s1-dc-algorithms-lesson.html | 1.1–1.5 |
| 2 | Recurrence from pseudocode; recursion trees; substitution / tree / Master methods | [DC-5] to [DC-7] | practice/week2-s2-recurrences-lesson.html | 2.1–2.5, 3.1–3.5 |
| 3 | Master Theorem (3 cases, regularity, when it doesn't apply); Karatsuba | [DC-8] to [DC-10] | practice/week2-s3-master-theorem-lesson.html | 4.1–4.5 |

Note: the lecture and class solutions say 2T(n/2) + n log n is "Master Theorem does not apply"; the lab answer also gives extended Case 2 → Θ(n log² n). The sheet [DC-9] teaches both.

## Week 3 sections (2026-11-02)

| Section | Topics | Sheet | Lesson | Practice Qs |
|---|---|---|---|---|
| 1 | Graph words; adjacency matrix and list; storage counts; speed of edge checks; dense and sparse; counting edges | [GR-0] to [GR-3] | practice/week3-s1-graphs-lesson.html | 1.1–1.5 |
| 2 | BFS queue trace; dist, prev and the path back; BFS ignores weights; O(V + E) | [GR-4] to [GR-6] | practice/week3-s2-bfs-lesson.html | 2.1–2.5 |
| 3 | Relaxation; Dijkstra trace with lazy deletion (stale pairs); path and cost; running time (array vs heap); negative edges; which algorithm | [GR-7] to [GR-10] | practice/week3-s3-dijkstra-lesson.html | 3.1–3.5, 4.1–4.5 |

Note: the Week 3 lab solution's step 3 note mentions an edge from A to B that is not in its own code or trace. The lesson follows the code (A to C 2, A to D 3).
