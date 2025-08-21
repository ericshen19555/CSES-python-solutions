def main():
    from sys import stdin
    e = stdin.readline

    e()  # n
    ans = 1
    for v in sorted(map(int, e().split())):
        if ans < v:
            break
        ans += v
    print(ans)
main()