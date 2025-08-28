def main():
    from sys import stdin
    from functools import cache
    e = stdin.readline

    @cache
    def dp(i: int = 0, pre: int = -1, is_lim: bool = True) -> int:
        if i == len(num): return 1
        res = 0
        lim = num[i] if is_lim else 9
        for d in range(lim + 1):
            if d == pre: continue
            res += dp(i + 1, -1 if pre == -1 and d == 0 else d, is_lim and d == lim)
        return res

    lo, hi = map(int, e().split())
    num = tuple(map(int, str(hi)))
    ans = dp()
    if lo:
        dp.cache_clear()
        num = tuple(map(int, str(lo - 1)))
        ans -= dp()
    print(ans)
main()