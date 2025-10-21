def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))

    res = [0] * (n + 1)
    suf = [0] * (n + 1)
    j = n
    for i in range(n - 1, -1, -1):
        suf[-1] += l[i]
        while suf[-1] > k:
            j -= 1
            suf[-1] -= l[j]
        res[i] = res[j] + 1
        suf[i] = suf[j]

    ans = n
    cur = 0
    for i in range(n):
        if cur + suf[i] <= k:
            ans = min(ans, res[i])
        cur += l[i]
    print(ans)
main()