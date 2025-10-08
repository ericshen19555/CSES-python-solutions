def main():
    from sys import stdin
    from heapq import heapify, heappop, heappush
    e = stdin.readline

    n, k = map(int, e().split())
    k = min(k + 1, n)
    l = list(map(int, e().split()))

    ans = [0] * n
    h = l[:k]
    heapify(h)
    for i in range(n):
        ans[i] = heappop(h)
        if i + k < n: heappush(h, l[i + k])
    print(*ans)
main()