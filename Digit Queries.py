def main():
    from sys import stdin
    stdin.readline()  # q
    base = 10
    for n in map(int, stdin):
        a, b = 1, base
        lim = a * b
        while n >= lim:
            n += b
            a += 1
            b *= base
            lim = a * b
        q, r = divmod(n, a)
        print(str(q)[r])
main()