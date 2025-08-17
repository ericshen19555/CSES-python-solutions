def main():
    from sys import stdin
    e = stdin.readline

    for _ in range(int(e())):
        n, a, b = map(int, e().split())
        m = a + b
        if n < m or (a == 0) != (b == 0):
            print("NO")
            continue
        print("YES")
        print(*range(1, m + 1), *range(m + 1, n + 1))
        print(*range(m - b + 1, m + 1), *range(1, a + 1), *range(m + 1, n + 1))
main()