# TODO: AC (currently WA)

import sys
from io import StringIO

testcase = """\
4 3
1 2
2 3
2 4
"""

sys.stdin = StringIO(testcase)

def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    n += 1  # 1-based
    hd = [-1] * (n << 1)
    to = [0] * (m << 1)
    ne = [0] * (m << 1)
    indeg = [0] * n
    for i in range(0, m << 1, 2):
        a, b = map(int, e().split())
        indeg[b] += 1
        to[i] = b
        ne[i] = hd[a]
        hd[a] = i
        i |= 1
        b += n
        to[i] = a
        ne[i] = hd[b]
        hd[b] = i
    q = [i for i in range(n) if indeg[i] == 0]
    o = [0] * n
    for x in range(1, n):
        i = q[x]
        o[i] = x
        ei = hd[i]
        while ~ei:
            j = to[ei]
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
            ei = ne[ei]

    pr = [-1] * n
    pr[0] = 0
    pi = 0
    pre = [0] * n
    for i in range(1, n):
        cont = False
        trans = -1 + (pr[0] >= pi)
        ei = hd[n + q[i]]
        while ~ei:
            j = o[to[ei]]
            cont = cont or j == i - 1
            if pr[j] >= pi:
                pr[j] = i
                trans = j
            ei = ne[ei]
        if not cont:
            pi = i
            if trans == -1:
                print("NO")
                return
        if ~trans: pr[i - 1] = i
        pre[i] = trans
        print(pi, pr, trans, cont)
    print(q)
    for i, x in enumerate(pre):
        print(i, x)
    print("YES")
    a, b = [], []
    i = n - 1
    while i:
        pi = pre[i]
        a.append(q[i])
        print(i, pi)
        if pi == -1:
            i -= 1
        else:
            b += [q[j] for j in range(i - 1, pi, -1)]
            i = pi
        print(a, b)
    print(len(a), *reversed(a))
    print(len(b), *reversed(b))
main()
