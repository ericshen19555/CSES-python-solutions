def main():
    from itertools import count
    A = 26
    LEN, POS, LINK, CNT = range(A, A + 4)
    cnt = count(1).__next__

    s = input()
    n = len(s)
    tr = [[0] * (A + 4) for _ in range(n << 1)]
    tr[0][POS] = -1
    tr[0][LEN] = 0
    tr[0][LINK] = -1
    tr[0][CNT] = 1
    last = 0
    for c in s:
        c = ord(c) - 97
        o = cnt()
        tr[o][LEN] = tr[last][LEN] + 1
        tr[o][POS] = tr[o][LEN]
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
                tr[clone][POS] = tr[q][POS]
                tr[clone][LEN] = tr[p][LEN] + 1
                tr[clone][CNT] = 0
                tr[o][LINK] = tr[q][LINK] = clone
                while ~p and tr[p][c] == q:
                    tr[p][c] = clone
                    p = tr[p][LINK]
    siz = cnt()
    indeg = [0] * siz
    for i in range(1, siz):
        indeg[tr[i][LINK]] += 1
    max_len, best_pos = 0, -1
    for i in range(siz):
        while not indeg[i]:
            indeg[i] = -1
            c = tr[i][CNT]
            if c >= 2 and tr[i][LEN] > max_len:
                max_len = tr[i][LEN]
                best_pos = tr[i][POS]
            p = tr[i][LINK]
            if p == -1: continue
            tr[p][CNT] += c
            indeg[p] -= 1
            i = p
    print(s[best_pos - max_len:best_pos] if max_len else -1)
main()