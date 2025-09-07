def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n, q = map(int, e().split())
    pre = list(accumulate(map(int, e().split()), initial=0))
    ans = []
    for _ in range(q):
        s, t = map(int, e().split())
        ans.append(pre[t] - pre[s - 1])
    print("\n".join(map(str, ans)))
main()