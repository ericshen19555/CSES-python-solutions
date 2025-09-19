def main():
    from sys import stdin
    e = stdin.readline
    A = 26

    lim = 5 * 10**5 + 1
    END, FAIL, POS = range(A, A + 3)
    tr = [[0] * (A + 3) for _ in range(lim)]

    s = e().rstrip()
    n = len(s)
    k = int(e())

    nxt = [-1] * (k + 1)
    siz = 1
    for idx in range(k):
        t = e().rstrip()
        o = 0
        for c in reversed(t):
            c = ord(c) - 97
            if not tr[o][c]:
                tr[o][c] = siz
                siz += 1
            o = tr[o][c]
        nxt[idx] = ~tr[o][END]
        tr[o][END] = ~idx

    # build ACAM
    q = [0]
    for o in q:
        node = tr[o]
        for c in range(A):
            if not (ch := node[c]): continue
            q.append(ch)
            if not o: continue
            fail = node[FAIL]
            while fail and not tr[fail][c]:
                fail = tr[fail][FAIL]
            if tr[fail][c]:
                fail = tr[fail][c]
            tr[ch][FAIL] = fail

    ans = ["-1"] * k
    o = 0
    for i in range(n):
        c = ord(s[~i]) - 97
        while o and not tr[o][c]:
            o = tr[o][FAIL]
        if tr[o][c]:
            o = tr[o][c]
        tr[o][POS] = i
    for o in reversed(q):
        node = tr[o]
        if not (pos := node[POS]): continue
        idx = ~node[END]
        str_pos = str(n - pos)
        while ~idx:
            ans[idx] = str_pos
            idx = nxt[idx]
        tr[node[FAIL]][POS] = max(tr[node[FAIL]][POS], pos)
    print("\n".join(ans))
main()