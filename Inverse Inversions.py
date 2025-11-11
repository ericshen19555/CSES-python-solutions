def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    lo, hi = 1, n
    ans = []
    while lo <= hi:
        if k >= hi - lo:
            ans.append(hi)
            k -= hi - lo
            hi -= 1
        else:
            ans.append(lo)
            lo += 1
    print(*ans)
main()