def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    sl = sorted(set(l))
    mp = {v: i for i, v in enumerate(sl)}
    m = len(mp)
    pos = [0] * m
    for v in l:
        pos[mp[v]] += 1
    pre = 0
    for i in range(m):
        pos[i], pre = pre, pre + pos[i]
    ans = 0
    for i, v in enumerate(l):
        v = mp[v]
        ans = max(ans, i - pos[v])
        pos[v] += 1
    print(ans)
main()