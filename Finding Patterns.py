def main():
    from sys import stdin
    e = stdin.readline
    A = 26

    lim = 5 * 10**5 + 1
    END, FAIL, VIS = range(A, A + 3)
    tr = [[0] * (A + 3) for _ in range(lim)]

    s = e().rstrip()
    k = int(e())

    nxt = [-1] * (k + 1)
    siz = 1
    for idx in range(k):
        t = e().rstrip()
        o = 0
        for c in t:
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

    ans = ["NO"] * k
    o = 0
    for c in s:
        c = ord(c) - 97
        while o and not tr[o][c]:
            o = tr[o][FAIL]
        if tr[o][c]:
            o = tr[o][c]
        tr[o][VIS] = True
    for o in reversed(q):
        node = tr[o]
        if not node[VIS]: continue
        idx = ~node[END]
        while ~idx:
            ans[idx] = "YES"
            idx = nxt[idx]
        tr[node[FAIL]][VIS] = True
    print("\n".join(ans))
main()