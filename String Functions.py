def main():
    s = input()
    n = len(s)
    z = [0] * n
    le = ri = 0
    for i in range(1, n):
        if i < ri: z[i] = min(ri - i, z[i - le])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]: z[i] += 1
        if i + z[i] > ri: le, ri = i, i + z[i]
    print(*z)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        c = s[i]
        while j and s[j] != c:
            j = lps[j - 1]
        j += s[j] == c
        lps[i] = j
    print(*lps)
main()