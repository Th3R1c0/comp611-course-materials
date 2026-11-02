---
name: algo-diagrams
description: Draw clean, exam-style algorithm diagrams with Graphviz, such as weighted graphs (Prim, Dijkstra, Kruskal), red-black and other trees, flow and residual networks, and DP tables, then render them to PNG and check them visually. Use it whenever a lesson, cheatsheet or practice question needs a figure.
---

# Algorithm diagrams (Graphviz)

Use Graphviz DOT for every figure. It gives exact control over edge weights, node colours and tree shape, which is what algorithm questions need. Don't use ASCII art except as a last-resort fallback.

## Setup
- Check `which dot`. If it's missing, install Graphviz (`brew install graphviz` on macOS, or `apt-get install -y graphviz`).
- If it can't be installed, write the DOT anyway and tell the student it can be pasted into https://dreampuf.github.io/GraphvizOnline to view it.

## Workflow
1. Start from the closest template in `templates/` (this skill's folder):
   - `weighted-graph.dot` for Prim, Dijkstra and Kruskal. Show the distance or key inside each node, put weights on a white background, highlight tree edges, and fill visited nodes.
   - `red-black-tree.dot` for red-black trees and BSTs. Use red and black fills, set `ordering=out`, and add invisible siblings so a lone child sits on the correct side.
   - `flow-network.dot` for max-flow. Label edges `flow/capacity`, highlight the augmenting path, use dashed back edges in residual graphs, and shade the min-cut S side.
   - `dp-table.dot` for DP tables. Shade the traceback path, and colour the cell being computed.
2. Write the `.dot` file next to where it's used, e.g. `revision/figures/<section>-q<N>.dot`.
3. Render it with `dot -Tpng -Gdpi=110 file.dot -o file.png`. The `layout=` line in the file picks the engine.
4. **Look at the PNG before showing it** (open or read the image). Check that:
   - no label overlaps another label or a node
   - every edge weight can clearly be read as belonging to one edge
   - tree children are on the correct left/right side (BST order)
   - colours match the state being asked about
   - what you drew matches the question text exactly (same nodes, weights and colours)
   Fix the DOT and re-render until all of these pass.
5. Show the image, and keep the `.dot` source so the figure can be edited later, e.g. "show the state after the next step".

## Conventions (keep them consistent so the student learns to read them fast)
| Meaning | Style |
|---|---|
| In tree / visited / S side of a cut | fill `#cfe3f5` |
| Chosen edge (MST / shortest-path tree) | `penwidth=3, color="#1f77b4"` |
| Augmenting path | `penwidth=3, color="#2ca02c"` |
| Current cell / node being processed | fill `#fff2a8` |
| Red node / black node | fill `#d62728` / `#222222`, white text |
| Residual back edge | `style=dashed` |

## Step-by-step traces
For "show each step" questions, render one PNG per step (`...-step1.png`, `...-step2.png`). Change only what changed in that step, and put a one-line caption under each image saying what happened.

## In cheatsheets
Cheatsheets are mostly text. Add a small figure only when it saves space or prevents a common mistake, such as the four red-black insert fix-up cases or a residual-graph example. Keep figures small and black-and-white-safe if the sheet will be printed: use pattern or line weight as well as colour.
