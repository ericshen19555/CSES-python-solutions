def main():
    s = input()
    n = len(s)

    le = ri = 0
    z = [0] * n
    ans = []
    for i in range(1, n):
        if i < ri:
            z[i] = min(ri - i, z[i - le])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > ri:
            le, ri = i, i + z[i]
        if i + z[i] == n:
            ans.append(z[i])
    print(" ".join(map(str, reversed(ans))))
main()