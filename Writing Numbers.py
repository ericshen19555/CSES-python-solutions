def main():
    from functools import lru_cache
    from bisect import bisect_left

    k = int(input())

    def check(n):
        num = tuple(map(int, str(n)))

        @lru_cache
        def DP(i=0, started=False, is_lim=True):
            if i == len(num): return started, [0] * 10
            lim = num[i] if is_lim else 9
            cnt = 0
            res = [0] * 10
            for d in range(lim + 1):
                new_started = started or d != 0
                new_is_lim = is_lim and d == lim
                c, r = DP(i + 1, new_started, new_is_lim)
                cnt += c
                if new_started: res[d] += c
                for dd in range(10):
                    res[dd] += r[dd]
            return cnt, res

        res = DP()[1]
        return all(c <= k for c in res)

    r = range(k + 10, 0, -1)
    print(r[bisect_left(r, True, key=check)])
main()