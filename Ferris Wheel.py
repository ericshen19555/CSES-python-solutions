def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = sorted(map(int, e().split()))
    ans = n
    j = n - 1
    for i, v in enumerate(l):
        while i < j and v + l[j] > k:
            j -= 1
        if i >= j: continue
        ans -= 1
        j -= 1
    print(ans)
main()