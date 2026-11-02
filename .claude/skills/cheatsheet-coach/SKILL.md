---
name: cheatsheet-coach
description: Exam revision loop for a cheatsheet-allowed exam. For each exam section, teach the topic, write a cheatsheet, quiz the student while they think out loud, correct them by citing cheatsheet entries, fix the sheet, and repeat until they score consistently.
---

# Cheatsheet coach

The student is revising for an exam where they may bring a cheatsheet. The goal is not only to learn the material. It is also to build a cheatsheet they can actually *use* under exam conditions, and to practise using it.

Work through the exam **one section at a time**. Run the loop below for each section until the mastery bar is met, then move to the next section.

## Files (keep everything in the repo so progress survives between sessions)

- `revision/exam-plan.md` lists the exam sections, the question styles, the cheatsheet rules, and the status of each section.
- `revision/cheatsheets/<NN>-<section-slug>.md` holds one cheatsheet per section.
- `revision/progress.md` is the log: every question asked, the result, the mistake type, and any cheatsheet edits.

At the start of every session, read these files and continue where the student left off. If they don't exist, run Setup.

## Setup (first session only)

1. Ask the student, in one message:
   - What are the exam sections, or the topics and question types? Ask for a past paper if they have one.
   - What are the cheatsheet rules: number of pages or sides, handwritten or printed, font limits?
   - When is the exam?
2. Find the course materials in the repo (lecture slides, notes, labs, past papers). If there are none, ask the student to add them. Don't teach from memory alone. Teach from their course's notation and definitions.
3. Write `revision/exam-plan.md` with the sections in order, giving each a share of the cheatsheet's page budget based on its exam weight.

## The loop, per section

### 1. Teach
- Give a short, focused lesson on the section, built from the course materials. Cite the file or slide you used.
- Cover the definitions, the key algorithms or methods, the standard proof or analysis patterns, the common traps, and one worked example in the exact style of an exam question.
- Check understanding with 1–2 quick questions before moving on. Keep it interactive and don't lecture for pages.

### 2. Write the cheatsheet
- Write `revision/cheatsheets/<NN>-<slug>.md`.
- Give **every entry a stable ID** such as `[DP-3]`, so that corrections can point to it.
- Optimise for lookup under time pressure. Use dense bullets, templates and step-by-step recipes ("To prove greedy correct: 1… 2… 3…"), recurrence and complexity tables, and "if you see X, do Y" triggers.
- Respect the page budget for the section. Prefer recipes and traps over prose the student already knows.

### 3. Test
- Give **one exam-style question at a time**, in the style and difficulty of the real exam (use past papers when they exist). Vary the question types within the section.
- Tell the student to answer **using only the cheatsheet** and to **think out loud**: what they look up, why, and each step.
- Give no hints while they answer.

### 4. Correct
- Grade the final answer as correct, partly correct or wrong. If you know the mark scheme, give marks.
- Go through their reasoning step by step. For every mistake or wobble:
  - Say what went wrong and what the correct step is.
  - **Cite the cheatsheet entry** that covers it, e.g. "see [GR-2], step 3".
  - Classify the cause:
    - **Sheet gap.** The sheet didn't cover it. Add an entry.
    - **Sheet unclear.** The entry was there but was misread or too hard to find. Rewrite it, move it, or add a trigger.
    - **Concept gap.** The sheet was fine but the understanding wasn't. Reteach briefly and don't change the sheet.
    - **Slip.** A careless error. Note it only.
- Edit the cheatsheet file for any gap or unclear entry. Show the student the diff in a few lines and log it in `progress.md`.
- Praise good reasoning briefly when it's right, and say which entry made it work.

### 5. Repeat or advance
- Log the question, result, cause and edits in `revision/progress.md`.
- **Mastery bar**, unless the student sets their own: 4 of the last 5 questions fully correct, covering at least 3 different question types, with no sheet edits needed in the last 3.
- If the bar is not met, go back to step 3, with weight on the weakest question type. If the student fails twice on the same idea, go back to step 1 for that idea only.
- If the bar is met, mark the section done in `exam-plan.md` and move to the next section.

## Spaced review
At the start of each session after the first, ask 1–2 questions from sections that are already done before continuing, so that earlier sections don't fade. If one of these is wrong, run the Correct step on it as usual.

## Final assembly
When all sections are done, or when the student asks:
- Merge all section sheets into `revision/cheatsheet-final.md` in exam order.
- Check it against the page and format rules. Trim the least-used entries first, using `progress.md` to see which entries were cited.
- Run a short mixed mock exam across all sections that uses only the final sheet.

## Style
- Keep turns short and interactive, since the student is answering live.
- Use the course's own notation.
- Be honest about mistakes and specific about the fix.
