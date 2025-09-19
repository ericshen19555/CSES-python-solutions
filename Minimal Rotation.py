def main():
    s = input()
    n = len(s)

    s += s
    i, j = 0, 1
    while i < n and j < n:
        k = 0
        while k < n and s[i + k] == s[j + k]: k += 1
        if s[i + k] < s[j + k]: j += k + 1
        else: i += k + 1
        if i == j: j += 1
    i = min(i, j)
    print(s[i:i+n])
main()