def main():
    from sys import stdin
    from math import gcd
    e = stdin.readline

    for _ in range(int(e())):
        a, b, c = map(int, e().split())
        print("YES" if a >= c and c % gcd(a, b) == 0 else "NO")
main()