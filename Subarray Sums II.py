def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n, k = map(int, e().split())
    pre = list(accumulate(map(int, e().split()), initial=0))
    cnt = dict.fromkeys(pre, 0)
    ans = 0
    for p in pre:
        ans += cnt.get(p - k, 0)
        cnt[p] += 1
    print(ans)
main()