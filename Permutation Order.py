def main():
    from sys import stdin
    from itertools import accumulate
    from operator import mul
    e = stdin.readline
    fac = list(accumulate(range(1, 21), func=mul, initial=1))

    ans = []
    for _ in range(int(e())):
        o, n, *l = map(int, e().split())
        numbers = list(range(1, n + 1))
        if o == 1:
            k = l[0] - 1
            res = []
            for r in range(n-1, -1, -1):
                idx, k = divmod(k, fac[r])
                res.append(numbers.pop(idx))
            ans.append(" ".join(map(str, res)))
        else:
            res = 1
            for r in range(n-1, -1, -1):
                idx = numbers.index(l[~r])
                res += idx * fac[r]
                numbers.pop(idx)
            ans.append(res)
    print("\n".join(map(str, ans)))
main()