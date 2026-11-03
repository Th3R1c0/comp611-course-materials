# Max flow (Edmonds-Karp) and min cut, used to check the week 8 lesson and question answers.
from collections import deque
def maxflow(edges, s="S", t="T", log=True):
    R={}
    for u,v,c in edges: R.setdefault(u,{})[v]=R.get(u,{}).get(v,0)+c; R.setdefault(v,{}).setdefault(u,0)
    total=0
    while True:
        par={s:None};q=deque([s])
        while q and t not in par:
            u=q.popleft()
            for v in sorted(R[u]):
                if v not in par and R[u][v]>0: par[v]=u;q.append(v)
        if t not in par: break
        path=[t]
        while path[-1]!=s: path.append(par[path[-1]])
        path.reverse(); b=min(R[path[i]][path[i+1]] for i in range(len(path)-1))
        for i in range(len(path)-1): R[path[i]][path[i+1]]-=b; R[path[i+1]][path[i]]+=b
        total+=b
        if log: print(" ".join(path),"bottleneck",b,"total",total)
    reach={s};q=[s]
    while q:
        u=q.pop()
        for v in R[u]:
            if R[u][v]>0 and v not in reach: reach.add(v);q.append(v)
    cut=[(u,v,c) for u,v,c in edges if u in reach and v not in reach]
    print("max flow",total,"left side",sorted(reach),"cut",cut,"capacity",sum(c for *_,c in cut))
    return total
if __name__=="__main__":
    lab3=[("S","A",5),("S","C",8),("A","B",1),("A","D",2),("C","B",3),("C","D",4),("B","T",6),("D","T",7)]
    maxflow(lab3)
    q=[("S","A",7),("S","B",4),("A","B",3),("A","C",4),("B","D",6),("C","T",5),("D","C",2),("D","T",4)]
    maxflow(q)
