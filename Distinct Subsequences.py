def main():
    mod = 10**9 + 7
    A = 26

    s = input()
    d = 0
    last = [-1] * A
    for c in s:
        c = ord(c) - 97
        p = d * 2 - last[c]
        last[c] = d
        d = p % mod
    print(d)
main()