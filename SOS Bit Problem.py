def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    bl = max(l).bit_length()

    bit = 1 << bl
    mask = bit - 1
    contain = [0] * bit
    inside = [0] * bit
    for v in l:
        contain[v] += 1
        inside[v] += 1
    for k in range(bl):
        b = 0
        bb = 1 << k
        while b < bit:
            b |= bb
            contain[b] += contain[b ^ bb]
            inside[b ^ bb] += inside[b]
            b += 1
    for v in l:
        print(contain[v], inside[v], n - contain[v ^ mask])
main()