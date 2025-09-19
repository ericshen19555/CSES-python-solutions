def main():
    s, p = input(), input()
    n, m = len(s), len(p)

    lps = [0] * m
    j = 0
    for i in range(1, m):
        c = p[i]
        while j and p[j] != c:
            j = lps[j - 1]
        j += (p[j] == c)
        lps[i] = j

    j = 0
    ans = 0
    for c in s:
        while j and p[j] != c:
            j = lps[j - 1]
        j += (p[j] == c)
        if j >= m:
            ans += 1
            j = lps[j - 1]
    print(ans)
main()