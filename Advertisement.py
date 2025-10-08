def main():
    from sys import stdin
    e = stdin.readline

    n = int(e()) + 1
    l = list(map(int, e().split())) + [0]
    ans = 0
    stk = []
    pi = pv = -1
    for i in range(n):
        v = l[i]
        while pv >= v:
            h = pv
            pi, pv = stk.pop()
            ans = max(ans, (i - pi - 1) * h)
        stk.append((pi, pv))
        pi, pv = i, v
    print(ans)
main()