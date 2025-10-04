def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    bl = n.bit_length()

    for k in range(bl):
        b = 1 << k
        for i in range(n):
            if i & b:
                l[i] ^= l[i ^ b]
    print(*l)
main()