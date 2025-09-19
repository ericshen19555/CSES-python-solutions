def main():
    s = "#" + "#".join(input()) + "#"
    n = len(s)

    le = ri = 0
    z = [0] * n
    ans = [1] * (n >> 1)
    for i in range(1, n):
        if i < ri:
            z[i] = min(ri - i, z[2 * le - i])
        while 0 <= i - 1 - z[i] and i + 1 + z[i] < n and s[i - 1 - z[i]] == s[i + 1 + z[i]]:
            z[i] += 1
            if (i + z[i]) & 1:
                idx = i + z[i] - 1 >> 1
                ans[idx] = max(ans[idx], z[i] + 1)
        if i + z[i] > ri:
            le, ri = i, i + z[i]
    print(*ans)
main()