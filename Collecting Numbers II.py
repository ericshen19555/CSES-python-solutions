def main():
    from sys import stdin
    from itertools import pairwise, starmap
    from operator import gt
    e = stdin.readline

    n, m = map(int, e().split())
    l = list(map(int, e().split()))
    p = [n] * (n + 2)
    for i, v in enumerate(l):
        p[v] = i
    res = sum(starmap(gt, pairwise(p)))
    ans = []
    for _ in range(m):
        i, j = map(int, e().split())
        i, j = i - 1, j - 1
        l[i], l[j] = l[j], l[i]
        i, j = l[i], l[j]
        if i > j: i, j = j, i
        res -= (p[i - 1] > p[i]) + (p[i] > p[i + 1]) + (p[j] > p[j + 1])
        if i + 1 != j: res -= (p[j - 1] > p[j])
        p[i], p[j] = p[j], p[i]
        res += (p[i - 1] > p[i]) + (p[i] > p[i + 1]) + (p[j] > p[j + 1])
        if i + 1 != j: res += (p[j - 1] > p[j])
        ans.append(res)
    print("\n".join(map(str, ans)))
main()