def main():
    from sys import stdin
    from collections import deque
    e = stdin.readline

    n, lo, hi = map(int, e().split())
    ans = float("-INF")
    q, qq = deque(), deque([0])
    p = 0
    for i, v in enumerate(map(int, e().split()), start=1):
        if i > hi and q and q[0][0] < i - hi:
            q.popleft()
        p += v
        if i >= lo:
            pi, pp = i - lo, qq.popleft()
            while q and q[-1][1] >= pp:
                q.pop()
            q.append((pi, pp))
            ans = max(ans, p - q[0][1])
        qq.append(p)
    print(ans)
main()