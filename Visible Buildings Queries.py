def main():
    from sys import stdin
    from bisect import bisect_right
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split())) + [float("INF")]

    ans = [0] * q
    qs = [[] for _ in range(n)]
    for qi in range(q):
        s, t = map(int, e().split())
        ans[qi] = t
        qs[s - 1].append(qi)

    stk = []
    pi = n
    for i in range(n-1, -1, -1):
        v = l[i]
        while l[pi] <= v:
            pi = -stk.pop()
        stk.append(-pi)
        pi = i
        for qi in qs[i]:
            ans[qi] = len(stk) - bisect_right(stk, -ans[qi]) + 1
    print("\n".join(map(str, ans)))
main()