def main():
    from sys import stdin
    from heapq import heappush, heappop
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    d = dict.fromkeys(l, 0)

    h = []
    ans = []
    for i, v in enumerate(l):
        d[v] += 1
        heappush(h, (-d[v], v))
        if i >= k:
            d[l[i - k]] -= 1
        if i >= k - 1:
            while d[h[0][1]] != -h[0][0]:
                heappop(h)
            ans.append(h[0][1])
    print(*ans)
main()