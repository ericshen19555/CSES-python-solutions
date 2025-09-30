def main():
    from sys import stdin
    from heapq import heappop, heappush
    e = stdin.readline

    n, m = map(int, e().split())
    outdeg = [0] * n
    R = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        R[b].append(a)
        outdeg[a] += 1

    ans = []
    q = [-i for i in range(n-1, -1, -1) if outdeg[i] == 0]
    for _ in range(n):
        i = -heappop(q)
        ans.append(i + 1)
        for j in R[i]:
            outdeg[j] -= 1
            if outdeg[j] == 0:
                heappush(q, -j)
    print(*reversed(ans))
main()