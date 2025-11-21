def main():
    from sys import stdin
    from heapq import heappush, heappop
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    ans = 0
    q = []
    for v in l:
        heappush(q, -v)
        heappush(q, -v)
        ans += -heappop(q) - v
    print(ans)
main()