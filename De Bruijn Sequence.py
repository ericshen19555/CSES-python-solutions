def main():
    n = int(input())
    k = 2

    a = list(map(str, range(k)))
    cur = [0] * k * n

    def dfs(i, p):
        if i == n:
            if n % p == 0:
                ans.extend(cur[:p])
        else:
            cur[i] = cur[i - p]
            dfs(i + 1, p)
            for j in range(cur[i - p] + 1, k):
                cur[i] = j
                dfs(i + 1, i + 1)

    ans = []
    dfs(0, 1)
    ans = "".join(a[i] for i in ans)
    print(f"{ans}{ans[0:n - 1]}")
main()