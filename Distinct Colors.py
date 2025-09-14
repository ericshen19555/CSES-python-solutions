def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    u = [{int(v)} for v in e().split()]
    deg = [0] * n
    deg[0] = 2
    pa = [0] * n
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        deg[a] += 1
        deg[b] += 1
        pa[a] ^= b
        pa[b] ^= a

    ans = [0] * n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            ui = u[i]
            ans[i] = len(ui)
            p = pa[i]
            up = u[p]
            if len(up) < len(ui): up, ui = ui, up
            up.update(ui)
            u[p] = up
            pa[p] ^= i
            deg[p] -= 1
            i = p
    ans[0] = len(u[0])
    print(*ans)
main()