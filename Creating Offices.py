# credit: ammojamo - https://cses.fi/problemset/hack/1752/entry/9695386/

def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    ne = [-1] * (n << 1)
    xe = [0] * n
    hd = [-1] * n
    for ei in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        xe[ei] = a ^ b
        ea, eb = ei << 1, ei << 1 | 1
        if ~hd[a]:
            ne[hd[a]], ne[ea] = eb, ne[hd[a]]
        else:
            ne[ea], hd[a] = eb, ea
        if ~hd[b]:
            ne[hd[b]], ne[eb] = ea, ne[hd[b]]
        else:
            ne[eb], hd[b] = ea, eb
    i = d = 0
    dep = [0] * n + [float("INF")]
    ei, ne[hd[i]] = ne[hd[i]], -1
    no = [-1] * n
    ans = [False] * n
    while ~ei:
        j = xe[ei >> 1] ^ i
        if j >= 0:
            xe[ei >> 1] = ~xe[ei >> 1]
            d += 1
            dep[j] = d
        else:
            j = ~j
            if dep[no[i]] - d >= k:
                ans[i] = True
                no[i] = i
            d -= 1
            if not no[j]:
                no[j] = no[i]
            else:
                di, dj = dep[no[i]], dep[no[j]]
                if di - d + dj - d < k:
                    if di > dj:
                        ans[no[j]] = False
                        no[j] = no[i]
                    else:
                        ans[no[i]] = False
                elif di < dj:
                    no[j] = no[i]
        i = j
        ei = ne[ei]
    if dep[no[i]] - d >= k:
        ans[i] = True
    ans = [i + 1 for i, v in enumerate(ans) if v]
    print(len(ans))
    print(*ans)
main()