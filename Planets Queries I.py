def main():
    from sys import stdin
    lim = 30
    e = stdin.readline

    n, q = map(int, e().split())
    binary_lifting = [[0] * n for _ in range(lim)]
    pre = binary_lifting[0] = [int(v) - 1 for v in e().split()]
    for r in range(1, lim):
        cur = binary_lifting[r]
        for i in range(n):
            cur[i] = pre[pre[i]]
        pre = cur
    ans = []
    for _ in range(q):
        i, k = map(int, e().split())
        i -= 1
        for row in binary_lifting:
            if k & 1:
                i = row[i]
            k >>= 1
        ans.append(f"{i + 1}")
    print("\n".join(ans))
main()