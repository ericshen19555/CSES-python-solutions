def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    ans = 1
    while n >= 10:
        n -= max(map(int, str(n)))
        ans += 1
    print(ans)
main()