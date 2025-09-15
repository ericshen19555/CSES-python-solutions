def main():
    from sys import stdin
    from itertools import combinations
    from functools import reduce
    from operator import mul
    e = stdin.readline

    n, k = map(int, e().split())
    ps = list(map(int, e().split()))
    ans = 0
    for r in range(1, k + 1):
        sign = 1 if r & 1 else -1
        for c in combinations(ps, r):
            ans += sign * (n // reduce(mul, c))
    print(ans)
main()