def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    n_ = n + 1
    l = "_".join(e().rstrip() for _ in range(n)) + '_' * n_
    vis = [0] * (n_ * n_)
    cur = [0]
    ans = [l[0]] * ((n << 1) - 1)
    for r in range(1, (n << 1) - 1):
        mn = "Z"
        nxt = []
        for i in cur:
            mn = min(mn, l[i + 1], l[i + n_])
        for i in cur:
            if l[i + 1] == mn and not vis[i + 1]:
                vis[i + 1] = 1
                nxt.append(i + 1)
            if l[i + n_] == mn and not vis[i + n_]:
                vis[i + n_] = 1
                nxt.append(i + n_)
        cur = nxt
        ans[r] = mn
    print("".join(ans))
main()