def main():
    from sys import stdin
    from itertools import accumulate
    from operator import add
    e = stdin.readline

    n, q = map(int, e().split())
    pre = [0] * (n + 1)
    l = [pre]
    for _ in range(n):
        pre = list(map(add, pre, accumulate((v == '*' for v in e()), initial=0)))
        l.append(pre)
    ans = []
    for _ in range(q):
        a, b, c, d = map(int, e().split())
        a, b = a-1, b-1
        ans.append(l[c][d] - l[a][d] - l[c][b] + l[a][b])
    print("\n".join(map(str, ans)))
main()