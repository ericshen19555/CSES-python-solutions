def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        i, j = map(int, e().split())
        r = i if i > j else j
        ans.append(r * r - r + 1 + (j - i if r & 1 else i - j))
    print("\n".join(map(str, ans)))
main()