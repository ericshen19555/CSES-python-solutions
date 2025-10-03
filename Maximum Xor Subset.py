def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    bl = max(l).bit_length()

    basis = [0] * bl
    for v in l:
        for k in reversed(range(bl)):
            if (v >> k) & 1 == 0: continue
            if not basis[k]:
                basis[k] = v
                break
            v ^= basis[k]

    ans = 0
    for b in reversed(basis):
        ans = max(ans, ans ^ b)
    print(ans)
main()