def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    ans = []
    tri = [i * (i + 1) >> 1 for i in range(1, 2 * 10**6)]
    for _ in range(int(e())):
        n = int(e())
        res = 3
        j = bisect_left(tri, n)
        if tri[j] == n:
            res = 1
        else:
            i = 0
            while i <= j:
                x = tri[i] + tri[j]
                if x == n:
                    res = 2
                    break
                elif x > n:
                    j -= 1
                else:
                    i += 1
        ans.append(res)
    print(*ans, sep='\n')
main()