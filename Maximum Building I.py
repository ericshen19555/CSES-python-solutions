def main():
    from sys import stdin
    e = stdin.readline

    m, n = map(int, e().split())
    n += 1
    l = [0] * (n + 1)
    ans = 0
    stk = []
    for _ in range(m):
        s = e()
        stk.clear()
        pi = -1
        for i in range(n):
            v = l[i] = l[i] + 1 if s[i] == "." else 0
            while l[pi] > v:
                ppi = stk.pop()
                ans = max(ans, (i - ppi - 1) * l[pi])
                pi = ppi
            stk.append(pi)
            pi = i
    print(ans)
main()