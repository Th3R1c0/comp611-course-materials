import subprocess, sys, os
import pathlib; OUT = str(pathlib.Path(__file__).resolve().parent.parent / "figures")
HEAD = '''  layout=neato; overlap=false; splines=true; pad=0.2; inputscale=1;
  node [shape=circle, style=filled, fillcolor="#ffffff", fontname="Helvetica", fontsize=15, width=0.5, fixedsize=true];
  edge [fontname="Helvetica", fontsize=13, color="#555555"];
'''
def lab(w): return f'<<TABLE BORDER="0" BGCOLOR="white" CELLPADDING="1"><TR><TD>{w}</TD></TR></TABLE>>'
def fig(name, directed, pos, edges, note=""):
    kw, op = ("digraph", "->") if directed else ("graph", "--")
    s = f"// {note}\n{kw} G {{\n{HEAD}"
    if directed: s += '  edge [arrowsize=0.8];\n'
    for n,(x,y) in pos.items(): s += f'  {n} [pos="{x*72},{y*62}"];\n'
    for e in edges:
        u,v,w = e[:3]; extra = e[3] if len(e)>3 else ""
        lbl = f', label={lab(w)}' if w is not None else ""
        s += f'  {u} {op} {v} [{lbl.lstrip(", ")}{extra}];\n'
    s += "}\n"
    p = f"{OUT}/{name}.dot"; open(p,"w").write(s)
    subprocess.run(["neato","-n2","-Tpng","-Gdpi=110",p,"-o",f"{OUT}/{name}.png"],check=True)

fig("w3-s1-directed", True, {"A":(0,1),"B":(1.8,2),"C":(1.8,0),"D":(3.6,1),"E":(5.2,2)},
  [("A","B",6),("A","C",2),("B","D",1),("B","E",4),("C","B",3),("C","D",5),("D","E",1)],
  "Week 3 lab Q1 graph: directed, weighted")
fig("w3-s2-bfs", False, {"A":(0,1),"B":(1.8,2),"C":(1.8,0),"D":(3.6,2),"E":(3.6,0),"F":(5.4,1)},
  [("A","B",4),("A","C",1),("B","D",4),("C","D",1),("C","E",2),("D","F",4),("E","F",1)],
  "BFS lesson graph: undirected, weights used only for the BFS-vs-lightest example")
fig("w3-s3-dijkstra", True, {"S":(0,1),"A":(1.8,2),"B":(1.8,0),"C":(3.6,0),"D":(3.6,2),"T":(5.4,1)},
  [("S","A",4),("S","B",2),("B","A",1),("A","C",2),("A","D",3),("B","C",5),("D","C",1),("C","T",3),("D","T",6)],
  "Week 3 lab Q4 graph: Dijkstra from S")
fig("w3-neg", True, {"S":(0,1),"A":(2,2),"B":(2,0)},
  [("S","A",2),("S","B",4),("B","A","−3")], "Negative edge breaks Dijkstra")
fig("w3-q-bfs", False, {"A":(0,1.5),"B":(1.6,3),"D":(1.6,0),"C":(3.4,3),"E":(3.4,1.5),"G":(3.4,0),"F":(5.2,2.4),"H":(5.2,0.4)},
  [("A","B",1),("A","D",4),("B","C",1),("B","E",2),("D","E",1),("D","G",5),("E","F",1),("C","F",2),("G","H",3),("F","H",1)],
  "Practice questions 2.x: BFS from A")
fig("w3-q-dijkstra", True, {"S":(0,1.5),"A":(1.8,3),"B":(1.8,0),"C":(3.6,1.5),"D":(5.4,3),"E":(5.4,0),"T":(7.2,1.5)},
  [("S","A",6),("S","B",1),("B","A",2),("B","C",9),("B","E",9),("A","C",2),("A","D",7),("C","D",2),("C","E",3),("D","T",4),("E","T",1)],
  "Practice questions 3.x: Dijkstra from S")
