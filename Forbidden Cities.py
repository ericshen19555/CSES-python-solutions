# TODO: AC (currently WA)

import sys
from io import StringIO

testcase = """\
9 16 1
2 5
3 5
8 5
4 2
2 4
3 8
5 3
5 9
7 3
6 3
2 5
3 9
2 4
6 1
7 1
1 3
9 8 5
"""

sys.stdin = StringIO(testcase)

def main():
    from sys import stdin
    e = stdin.readline

    n, m, q = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)

    ans = [True] * q
    pr = [-1] * q
    qs = []
    qo = [[] for _ in range(n)]
    qc = [[] for _ in range(n)]
    for qi in range(q):
        a, b, c = map(int, e().split())
        if a == c or b == c:
            ans[qi] = False
        else:
            a, b, c = a - 1, b - 1, c - 1
            qs.append((a, b, c))
            qo[a].append(qi)
            qo[b].append(qi)
            qc[c].append(qi)

    rt_ch = 0
    stk = [0]
    idx = [0] * n
    dfn = [0] * n
    low = [0] * n
    pa = [0] * n
    dfc = 0
    cut = [False] * n
    while stk:
        i = stk[-1]
        it, x = G[i], idx[i]
        if x == 0:
            dfc += 1
            dfn[i] = low[i] = dfc
            for qi in qo[i]:
                c = qs[qi][2]
                if pr[qi] == -1:
                    pr[qi] = idx[c]
                elif pr[qi] != idx[c]:
                    ans[qi] = False
        if x < len(it):
            j = it[x]
            idx[i] += 1
            if not dfn[j]:
                if i == 0: rt_ch += 1
                pa[j] = i
                stk.append(j)
            elif j != pa[i] and dfn[j] < low[i]:
                low[i] = dfn[j]
        else:
            stk.pop()
            idx[i] = 0
            p = pa[i]
            if i == 0:
                if rt_ch >= 2:
                    cut[i] = True
            else:
                if low[i] < low[p]: low[p] = low[i]
                if p != 0 and low[i] >= dfn[p]:
                    cut[p] = True
    for i in range(n):
        if cut[i]: continue
        for qi in qc[i]:
            ans[qi] = True
    print("\n".join("YES" if v else "NO" for v in ans))
main()