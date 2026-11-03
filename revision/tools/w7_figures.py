# Week 7 MST figures (undirected weighted graphs, Graphviz neato -n2).
import subprocess, pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / "figures")
HEAD = '''  layout=neato; overlap=false; splines=true; pad=0.25; inputscale=1;
  node [shape=circle, style=filled, fillcolor="#ffffff", fontname="Helvetica", fontsize=15, width=0.5, fixedsize=true];
  edge [fontname="Helvetica", fontsize=13, color="#555555"];
'''
def lab(w, col): return f'<<TABLE BORDER="0" BGCOLOR="white" CELLPADDING="1"><TR><TD><FONT COLOR="{col}">{w}</FONT></TD></TR></TABLE>>'
def fig(name, pos, edges, mst=(), note=""):
    s = f"// {note}\ngraph G {{\n{HEAD}"
    for n,(x,y) in pos.items(): s += f'  {n} [pos="{x*80},{y*70}"];\n'
    for u,v,w in edges:
        on = (u,v) in mst or (v,u) in mst
        extra = ', color="#2f7d3a", penwidth=3' if on else ''
        s += f'  {u} -- {v} [label={lab(w, "#2f7d3a" if on else "black")}{extra}];\n'
    s += "}\n"; p = f"{OUT}/{name}.dot"; open(p,"w").write(s)
    subprocess.run(["neato","-n2","-Tpng","-Gdpi=110",p,"-o",f"{OUT}/{name}.png"],check=True)
LAB = [("P","Q",4),("P","R",2),("Q","R",1),("Q","S",5),("R","S",8),("R","U",10),("S","T",3),("S","U",6),("T","U",7)]
PL = {"P":(0,1),"Q":(1.8,2),"R":(1.8,0),"S":(3.6,1.6),"U":(3.6,-0.4),"T":(5.4,1.8)}
fig("w7-lesson-graph", PL, LAB, note="Week 7 lab Q2 graph")
fig("w7-lesson-mst", PL, LAB, mst=[("P","R"),("Q","R"),("Q","S"),("S","T"),("S","U")], note="MST weight 17")
Q = [("A","B",4),("A","C",1),("B","C",3),("B","D",2),("C","D",5),("C","E",7),("D","E",6),("D","F",9),("E","F",8),("E","G",10),("F","G",11)]
PQ = {"A":(0,1),"B":(1.6,2.2),"C":(1.6,-0.2),"D":(3.4,2.2),"E":(3.4,-0.2),"F":(5.2,2.2),"G":(5.2,-0.2)}
fig("w7-q-graph", PQ, Q, note="Practice questions graph, MST 30")
