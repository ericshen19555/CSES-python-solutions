def main():
    from itertools import count
    A = 26
    LEN, LINK, CNT, DP = range(A, A + 4)
    cnt = count(1).__next__

    s = input()
    n = len(s)
    k = int(input())

    tr = [[0] * (A + 4) for _ in range(n << 1)]
    tr[0][LEN] = 0
    tr[0][LINK] = -1
    tr[0][CNT] = 0
    last = 0
    for c in s:
        c = ord(c) - 97
        o = cnt()
        tr[o][LEN] = tr[last][LEN] + 1
        tr[o][CNT] = 1
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
                tr[clone][CNT] = 0
                tr[q][LINK] = tr[o][LINK] = clone
                while ~p and tr[p][c] == q:
                    tr[p][c] = clone
                    p = tr[p][LINK]
    size = cnt()

    bs = [[] for _ in range(n + 1)]
    for o in range(size):
        bs[tr[o][LEN]].append(o)
    for b in reversed(bs):
        for o in b:
            tr[o][DP] = 0
            if o: tr[tr[o][LINK]][CNT] += tr[o][CNT]
            for c in range(A):
                ch = tr[o][c]
                if not ch: continue
                tr[o][DP] += tr[ch][DP] + tr[ch][CNT]

    o = 0
    ans = []
    while k:
        for c in range(A):
            ch = tr[o][c]
            if not ch: continue
            if k <= tr[ch][CNT]:
                ans.append(chr(c + 97))
                k = 0
                break
            k -= tr[ch][CNT]
            if k <= tr[ch][DP]:
                ans.append(chr(c + 97))
                o = ch
                break
            k -= tr[ch][DP]
    print("".join(ans))
main()