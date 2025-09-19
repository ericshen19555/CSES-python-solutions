def main():
    s = input()
    ss = "#" + "#".join(s) + "#"
    n = len(ss)

    le = ri = 0
    z = [0] * n
    for i in range(1, n):
        if i < ri:
            z[i] = min(ri - i, z[2 * le - i])
        while 0 <= i - 1 - z[i] and i + 1 + z[i] < n and ss[i - 1 - z[i]] == ss[i + 1 + z[i]]:
            z[i] += 1
        if i + z[i] > ri:
            le, ri = i, i + z[i]
    m = max(z)
    i = z.index(m) >> 1
    print(s[i-(m >> 1):i+(m + 1 >> 1)])
main()