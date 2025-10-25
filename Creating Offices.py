def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    pa = [0] * n
    deg = [0] * n
    deg[0] = 2
    for ei in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        pa[a] ^= b
        pa[b] ^= a
        deg[a] += 1
        deg[b] += 1
    ans = [False] * n
    no = [(-1, k)] * n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            x, dx = no[i]
            if dx >= k:
                ans[i] = True
                x, dx = i, 1
            else:
                dx += 1

            p = pa[i]
            y, dy = no[p]
            if y == -1:
                no[p] = x, dx
            elif dx + dy >= k:
                if dx < dy:
                    no[p] = x, dx
            elif dx > dy:
                ans[y] = False
                no[p] = x, dx
            else:
                ans[x] = False
            pa[p] ^= i
            deg[p] -= 1
            i = p
    if no[0][1] >= k:
        ans[0] = True
    ans = [i + 1 for i, v in enumerate(ans) if v]
    print(len(ans))
    print(*ans)
main()