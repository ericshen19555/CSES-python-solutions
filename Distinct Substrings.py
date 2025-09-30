def main():
    from itertools import count
    A = 26
    LEN, LINK = range(A, A + 2)
    cnt = count(1).__next__

    s = input()
    n = len(s)
    tr = [[0] * (A + 2) for _ in range(n << 1)]
    tr[0][LEN] = 0
    tr[0][LINK] = -1
    last = 0
    for c in s:
        c = ord(c) - 97
        o = cnt()
        tr[o][LEN] = tr[last][LEN] + 1
        p, last = last, o
        while ~p and not tr[p][c]:
            tr[p][c] = o
            p = tr[p][LINK]
        if p == -1:
            tr[o][LINK] = 0
        else:
            q = tr[p][c]
            if tr[p][LEN] + 1 == tr[q][LEN]:
                tr[o][LINK] = q
            else:
                clone = cnt()
                tr[clone] = tr[q].copy()
                tr[clone][LEN] = tr[p][LEN] + 1
                tr[q][LINK] = tr[o][LINK] = clone
                while ~p and tr[p][c] == q:
                    tr[p][c] = clone
                    p = tr[p][LINK]
    siz = cnt()
    ans = sum(tr[o][LEN] - tr[tr[o][LINK]][LEN] for o in range(1, siz))
    print(ans)
main()