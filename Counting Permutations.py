# OEIS A002464

def main():
    mod = 10**9 + 7
    n = int(input())
    if n <= 3:
        print(1 if n == 1 else 0)
        return
    pppp, ppp, pp, p = 1, 1, 0, 0
    for i in range(4, n + 1):
        pppp, ppp, pp, p = ppp, pp, p, ((i + 1) * p - (i - 2) * pp - (i - 5) * ppp + (i - 3) * pppp) % mod
    print(p)
main()