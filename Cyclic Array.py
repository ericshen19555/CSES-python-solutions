def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    if sum(l) <= k:
        print(1)
        return

    nxt = [0] * n
    j = -1
    cur = 0
    for i in range(n):
        while cur <= k:
            j += 1
            if j == n: j = 0
            cur += l[j]
        nxt[i] = j
        cur -= l[i]
    i = 0
    for _ in range(n):
        i = nxt[i]
    ans = 0
    s = i
    cycle = 0
    while cycle < 2 and (cycle == 0 or i < s):
        ans += 1
        j = nxt[i]
        if j < i:
            cycle += 1
        i = j
    print(ans)
main()