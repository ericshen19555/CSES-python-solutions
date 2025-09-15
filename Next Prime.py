def main():
    from sys import stdin
    from itertools import count
    e = stdin.readline

    ps = (2, 3, 5, 7, 11)

    def is_prime(n):
        if n < 2: return False
        if n & 1 == 0: return n == 2
        for p in ps:
            if n % p == 0:
                return n == p

        d = n - 1
        r = (d & -d).bit_length() - 1
        d >>= r

        for a in ps:
            if a % n == 0: continue
            x = pow(a, d, n)
            if x == 1 or x == n-1:
                continue
            for _ in range(r - 1):
                x = x * x % n
                if x == n-1: break
            else:
                return False
        return True

    ans = []
    for _ in range(int(e())):
        ans.append(next(filter(is_prime, count(int(e()) + 1))))
    print("\n".join(map(str, ans)))
main()