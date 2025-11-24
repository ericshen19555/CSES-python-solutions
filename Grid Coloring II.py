# credit: qusol

def main():
    from sys import stdin
    from collections import deque
    e = stdin.readline

    m, n = map(int, e().split())
    l = [bytearray(e().encode()) for _ in range(m)]
    ans = [bytearray(n) for _ in range(m)]

    d = [0, -1, 0, 1]
    t = lambda c: 1 << c - 65
    q = deque()

    def f(i, j, bad):
        q.append((i, j, bad))
        while q:
            i, j, bad = q.popleft()
            if not (0 <= i < m and 0 <= j < n): continue
            if bad == l[i][j]: continue
            if ans[i][j]:
                if bad == ans[i][j]:
                    print("IMPOSSIBLE")
                    exit()
                continue
            c = ans[i][j] = 65 ^ 66 ^ 67 ^ l[i][j] ^ bad
            for di in range(4):
                q.append((i + d[di], j + d[di ^ 1], c))

    for i in range(m - 1):
        for j in range(n - 1):
            if t(l[i][j]) | t(l[i+1][j]) | t(l[i][j+1]) | t(l[i+1][j+1]) != 7: continue
            if l[i+0][j+0] == l[i+1][j+0]: f(i+0, j+0, l[i+1][j+1])
            if l[i+0][j+0] == l[i+0][j+1]: f(i+0, j+0, l[i+1][j+1])
            if l[i+1][j+1] == l[i+1][j+0]: f(i+1, j+1, l[i+0][j+0])
            if l[i+1][j+1] == l[i+0][j+1]: f(i+1, j+1, l[i+0][j+0])
    for i in range(m):
        for j in range(n):
            if ans[i][j]: continue
            f(i, j, l[i][j] + 1 if l[i][j] < 67 else 65)
    print("\n".join(map(bytearray.decode, ans)))
main()
