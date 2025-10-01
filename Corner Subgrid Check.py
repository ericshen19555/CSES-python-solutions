def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    ans = [False] * k
    flags = [[0] * n for _ in range(k)]
    for i in range(n):
        s = e()
        row = [0] * k
        for j in range(n):
            c = ord(s[j]) - 65
            if ans[c]: continue
            flag = flags[c]
            if row[c] & flag[j]:
                ans[c] = True
            else:
                flag[j] |= row[c]
                row[c] |= 1 << j
    print("\n".join("YES" if res else "NO" for res in ans))
main()
