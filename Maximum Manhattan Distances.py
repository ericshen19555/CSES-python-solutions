def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())

    a, b = map(int, e().split())
    mx0 = mn0 = a + b
    mx1 = mn1 = a - b
    cur = 0
    ans = [cur]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a + b, a - b
        cur = max(cur, mx0 - a, a - mn0, mx1 - b, b - mn1)
        ans.append(cur)
        mx0, mn0 = max(mx0, a), min(mn0, a)
        mx1, mn1 = max(mx1, b), min(mn1, b)
    print(*ans, sep="\n")
main()