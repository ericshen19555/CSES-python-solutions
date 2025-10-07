def main():
    from sys import stdin
    inf = float("INF")
    e = stdin.readline

    n = int(e())
    l = [inf] + list(map(int, e().split())) + [inf]
    ans = 0

    for _ in range(n - 1):
        i = 1
        while l[i] > l[i + 2]:
            i += 1
        l[i] += l.pop(i + 1)
        ans += l[i]
        while l[i] > l[i - 1]:
            l[i], l[i - 1] = l[i - 1], l[i]
            i -= 1
    print(ans)
main()