def main():
    from sys import stdin
    from collections import defaultdict
    from itertools import product
    e = stdin.readline

    n, t = map(int, e().split())
    l = list(map(int, e().split()))
    mp = defaultdict(list)
    for i in range(1, n):
        for j in range(i):
            mp[l[i] + l[j]].append((j, i))
    for s, self in mp.items():
        if (s << 1) > t: continue
        if (other := mp.get(t - s)) is None: continue
        for (a, b), (c, d) in product(self, other):
            if a == c or a == d: continue
            if b == c or b == d: continue
            print(a + 1, b + 1, c + 1, d + 1)
            return
    print("IMPOSSIBLE")
main()