def main():
    from sys import stdin
    from heapq import heapify, heappushpop
    e = stdin.readline

    a, b, n = map(int, e().split())
    l = [tuple(map(int, e().split())) for _ in range(n)]
    # x - y 越大 -> 當工程師的"潛力"越高
    l.sort(key=lambda x: x[1] - x[0])

    # 前後綴分解
    suf = [0] * (n - b - a + 1)
    h = [l[i][1] for i in range(n - b, n)]
    heapify(h)
    suf[-1] = cur = sum(h)
    for i in range(a, n - b)[::-1]:
        v = l[i][1]
        cur += v - heappushpop(h, v)
        suf[i - a] = cur

    ans = 0
    h = [l[i][0] for i in range(a)]
    heapify(h)
    cur = sum(h)
    for i in range(a, n - b):
        ans = max(ans, cur + suf[i - a])
        v = l[i][0]
        cur += v - heappushpop(h, v)
    ans = max(ans, cur + suf[-1])
    print(ans)
main()