# Week 9 BST figures and checks: builds BSTs by insertion, draws them with dot, prints walks.
import subprocess, pathlib
OUT = str(pathlib.Path(__file__).resolve().parent.parent / "figures")
class N:
    def __init__(s,k): s.k=k; s.l=None; s.r=None
def insert(root,k,path=None):
    if root is None: return N(k)
    x=root
    while True:
        if path is not None: path.append(x.k)
        if k<x.k:
            if x.l is None: x.l=N(k); return root
            x=x.l
        else:
            if x.r is None: x.r=N(k); return root
            x=x.r
def build(keys):
    r=None
    for k in keys: r=insert(r,k)
    return r
def ino(x): return ino(x.l)+[x.k]+ino(x.r) if x else []
def pre(x): return [x.k]+pre(x.l)+pre(x.r) if x else []
def post(x): return post(x.l)+post(x.r)+[x.k] if x else []
def height(x): return -1 if x is None else 1+max(height(x.l),height(x.r))
def draw(root,name,hl=()):
    # x position = place in sorted (inorder) order, y = depth, so left and right children are never ambiguous
    order={k:i for i,k in enumerate(ino(root))}
    lines=['digraph T {','  layout=neato; pad=0.2;','  node [shape=circle, style=filled, fillcolor="#ffffff", fontname="Helvetica", fontsize=15, width=0.5, fixedsize=true];','  edge [color="#555555", arrowhead=none];']
    def go(x,d):
        fill=' fillcolor="#e7f3e8"' if x.k in hl else ''
        lines.append(f'  n{x.k} [label="{x.k}", pos="{order[x.k]*46},{-d*62}"{fill}];')
        for ch in (x.l,x.r):
            if ch: go(ch,d+1); lines.append(f'  n{x.k} -> n{ch.k};')
    go(root,0); lines.append('}')
    p=f"{OUT}/{name}.dot"; open(p,"w").write("\n".join(lines))
    subprocess.run(["neato","-n2","-Tpng","-Gdpi=110",p,"-o",f"{OUT}/{name}.png"],check=True)
if __name__=="__main__":
    for nm,keys in (("w9-lesson-bst",[50,30,70,20,40,60,80,45,75]),("w9-q-bst",[41,20,65,11,29,50,91,26,32,72,99])):
        r=build(keys); draw(r,nm)
        print(nm,"in",ino(r),"\n pre",pre(r),"\n post",post(r),"\n height",height(r))
    r=build([41,20,65,11,29,50,91,26,32,72,99]); p=[]; insert(r,30,p); print("insert 30 path",p)
    print("chain height", height(build([10,20,30,40,50])))
    print("q order", pre(build([8,3,10,1,6,14,4,7,13])))
