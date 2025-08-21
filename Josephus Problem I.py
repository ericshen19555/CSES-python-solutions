def main():
    n = int(input())
    m = 2
    ans = []

    # build BIT
    bit = [i & -i for i in range(n + 1)]
    # n's highest bit
    hb = 1 << n.bit_length() - 1

    target = 0
    for r in range(n, 0, -1):
        # update bisect target
        target = (target + m - 1) % r
        # bisect_right for target on BIT
        b = hb
        i = v = 0
        while b > 0:
            if (_i := i + b) <= n and (_v := v + bit[_i]) <= target:
                i, v = _i, _v
            b >>= 1
        # add to answer
        ans.append(i + 1)
        # update BIT
        i += 1  # 0-based to 1-based
        while i <= n:
            bit[i] -= 1
            i += i & -i
    print(*ans)
main()