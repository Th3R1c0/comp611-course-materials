# Week 11 disjoint-set forest figures: arrows point from each node to its parent; roots have a self-loop label "root".
import subprocess, pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / "figures")
def fig(name, parent, ranks=None, hl=(), note=""):
    s = [f"// {note}", "digraph F {", "  rankdir=BT; nodesep=0.4; ranksep=0.5; pad=0.2;",
         '  node [shape=circle, style=filled, fillcolor="#ffffff", fontname="Helvetica", fontsize=15, width=0.5, fixedsize=true];',
         '  edge [color="#555555", arrowsize=0.8];']
    for v,p in parent.items():
        lab = f'{v}' if not ranks or v not in ranks else f'{v}'
        fill = ' fillcolor="#e7f3e8"' if v in hl else ''
        xl = ''  # ranks are given in the caption, to keep the picture clean
        s.append(f'  "{v}" [label="{lab}"{fill}{xl}];')
        if p != v: s.append(f'  "{v}" -> "{p}";')
    roots = [v for v,p in parent.items() if p == v]
    s.append("  { rank=same; " + " ".join(f'"{r}";' for r in roots) + " }")
    s.append("}")
    p = f"{OUT}/{name}.dot"; open(p,"w").write("\n".join(s))
    subprocess.run(["dot","-Tpng","-Gdpi=110",p,"-o",f"{OUT}/{name}.png"],check=True)
lab = {1:2, 2:4, 3:4, 4:6, 5:6, 6:6, 7:6, 8:7}
fig("w11-lesson-forest", lab, ranks={6:3}, note="Week 11 lab Q5 forest, root 6 rank 3")
fig("w11-lesson-compressed", {1:6, 2:6, 3:4, 4:6, 5:6, 6:6, 7:6, 8:7}, ranks={6:3}, hl=(1,2), note="After FIND-SET(1) with path compression")
q = {1:3, 2:1, 3:9, 5:3, 7:9, 8:7, 9:9, 4:4, 6:4}
fig("w11-q-forest", q, ranks={9:3, 4:1}, note="Practice questions forest: roots 9 (rank 3) and 4 (rank 1)")
