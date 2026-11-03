# Week 8 flow network figures (Graphviz neato -n2, positions in points).
import subprocess, pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / "figures")
HEAD = '''  layout=neato; overlap=false; splines=true; pad=0.25; inputscale=1;
  node [shape=circle, style=filled, fillcolor="#ffffff", fontname="Helvetica", fontsize=15, width=0.5, fixedsize=true];
  edge [fontname="Helvetica", fontsize=13, color="#555555", arrowsize=0.8];
'''
def lab(w, col="black"): return f'<<TABLE BORDER="0" BGCOLOR="white" CELLPADDING="1"><TR><TD><FONT COLOR="{col}">{w}</FONT></TD></TR></TABLE>>'
def fig(name, pos, edges, note="", hl=()):
    s = f"// {note}\ndigraph G {{\n{HEAD}"
    for n,(x,y) in pos.items():
        fill = ' fillcolor="#e7f3e8"' if n in hl else ''
        s += f'  {n} [pos="{x*80},{y*70}"{fill}];\n'
    for e in edges:
        u,v,w = e[:3]; col = e[3] if len(e)>3 else None
        extra = f', color="{col}", penwidth=2.2' if col else ''
        key = "label"
        if (u,v) in (("A","D"),("C","B")) and name.startswith("w8-lesson"):
            key = "taillabel"; extra += ', labeldistance=3.2, labelangle=' + ("-28" if u=="A" else "28")
        s += f'  {u} -> {v} [{key}={lab(w, col or "black")}{extra}];\n'
    s += "}\n"
    p = f"{OUT}/{name}.dot"; open(p,"w").write(s)
    subprocess.run(["neato","-n2","-Tpng","-Gdpi=110",p,"-o",f"{OUT}/{name}.png"],check=True)
P1 = {"S":(0,1),"A":(1.8,2),"C":(1.8,0),"B":(3.6,2),"D":(3.6,0),"T":(5.4,1)}
fig("w8-lesson-net", P1, [("S","A",5),("S","C",8),("A","B",1),("A","D",2),("C","B",3),("C","D",4),("B","T",6),("D","T",7)], "Week 8 lab Q3 network, capacities")
R="#b3412e"
fig("w8-lesson-final", P1, [("S","A","3/5"),("S","C","7/8"),("A","B","1/1",R),("A","D","2/2",R),("C","B","3/3",R),("C","D","4/4",R),("B","T","4/6"),("D","T","6/7")], "Final max flow 10, min cut edges in red, left side S A C green", hl=("S","A","C"))
P2 = {"S":(0,1),"A":(1.8,2),"B":(1.8,0),"C":(3.6,2),"D":(3.6,0),"T":(5.4,1)}
fig("w8-q-net", P2, [("S","A",7),("S","B",4),("A","B",3),("A","C",4),("B","D",6),("C","T",5),("D","C",2),("D","T",4)], "Practice questions network, capacities")
fig("w8-q-flow", P2, [("S","A","5/7"),("S","B","4/4"),("A","B","1/3"),("A","C","4/4"),("B","D","5/6"),("C","T","5/5"),("D","C","1/2"),("D","T","4/4")], "Practice questions: a flow, flow/capacity")
