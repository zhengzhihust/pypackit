def topsort(G):
    count = dict((u,0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0] #valid initial nodes
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S

import functools
def reg_dag_sp(W,s,t):
    @functools.lru_cache(maxsize=None)
    def d(u):
        if u == t:
            return 0
        return min(W[u][v] + d[v] for v in W[u])
    return d[s]

def dag_sp(W,s,t):
    d = {u:float('inf') for u in W}
    d[s] = 0
    for u in topsort(W):
        if u == t:
            break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])
    return d[t]