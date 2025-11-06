def main():
    from sys import stdin
    from heapq import heapify, heappop, heapreplace
    e = stdin.readline

    n = int(e().split()[1])
    h = list(map(int, e().split()))
    heapify(h)
    ans = 0
    for _ in range(n - 1):
        v = heappop(h) + h[0]
        ans += v
        heapreplace(h, v)
    print(ans)
main()