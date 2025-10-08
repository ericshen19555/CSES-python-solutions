def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    print(f"{sum(i * (pow(i, n) - pow(i - 1, n)) for i in range(1, k + 1)) / pow(k, n):.6f}")
main()