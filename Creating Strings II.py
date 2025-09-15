def main():
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7

    s = input()
    n = len(s)
    fac = list(accumulate(range(1, n + 1), func=mul, initial=1))

    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - 97] += 1
    num = 1
    for v in cnt:
        num = num * fac[v] % mod
    print(fac[n] * pow(num, -1, mod) % mod)
main()