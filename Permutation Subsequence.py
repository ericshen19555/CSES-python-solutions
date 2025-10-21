def main():
    from sys import stdin
    from bisect import bisect_right
    e = stdin.readline

    n, m = map(int, e().split())
    a = list(map(int, e().split()))
    b = list(map(int, e().split()))
    if n > m:
        n, m = m, n
        a, b = b, a

    pos = [-1] * (n + 1)
    for i, v in enumerate(b):
        if v > n: continue
        pos[v] = i
    pre = [0] * (n + 1)
    lis = [0]
    for v in a:
        if pos[v] > pos[lis[-1]]:
            x = len(lis)
            lis.append(v)
        else:
            x = bisect_right(lis, pos[v], key=pos.__getitem__)
            lis[x] = v
        pre[v] = lis[x - 1]

    print(len(lis) - 1)
    ans = []
    v = lis[-1]
    while v:
        ans.append(v)
        v = pre[v]
    print(*ans[::-1])
main()