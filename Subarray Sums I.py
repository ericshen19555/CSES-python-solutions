def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n, k = map(int, e().split())
    pre = [0]
    ans = j = 0
    for i, p in enumerate(accumulate(map(int, e().split()))):
        if p >= k:
            t = p - k
            while j <= i and pre[j] < t:
                j += 1
            ans += j <= i and pre[j] == t
        pre.append(p)
    print(ans)
main()