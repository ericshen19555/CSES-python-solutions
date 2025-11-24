def main():
    from sys import stdin
    from collections import deque
    e = stdin.readline

    n = int(e())
    l = [int(v) - 1 for v in e().split()]

    ans = []
    while True:
        swap = []
        vis = [0] * n
        for s in range(n):
            if vis[s] > 0: continue
            i = s
            q = deque()
            while vis[i] == 0:
                q.append(i)
                vis[i] += 1
                i = l[i]
            while len(q) >= 2:
                i, j = q.popleft(), q.pop()
                swap.append(f"{i+1} {j+1}")
                l[i], l[j] = l[j], l[i]
        if not swap: break
        ans.append(swap)
    print(len(ans))
    for swap in ans:
        print(len(swap))
        print("\n".join(swap))
main()