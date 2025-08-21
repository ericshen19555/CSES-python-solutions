def main():
    from sys import stdin
    e = stdin.readline

    e()
    stk = []
    pi = pv = 0
    ans = []
    for i, v in enumerate(map(int, e().split()), start=1):
        while pv >= v:
            pi, pv = stk.pop()
        ans.append(pi)
        stk.append((pi, pv))
        pi, pv = i, v
    print(*ans)
main()