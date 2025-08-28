def main():
    from sys import stdin
    mod = 10 ** 9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    bit = 1 << n
    mask = bit - 1

    tiles = [0b11 << i for i in range(n - 1)]
    tiles_comb = [0b0]
    for tile in tiles:
        for tile_comb in tiles_comb:
            if not tile_comb & tile:
                tiles_comb.append(tile_comb | tile)
    # print(len(tiles_comb))  # <= 89

    trans = [[mask ^ (b | tile_comb)
              for tile_comb in tiles_comb
              if not b & tile_comb] for b in range(bit)]
    # print(sum(map(len, trans)))  # <= 5741

    d = [0] * bit
    d[0] = 1
    for _ in range(m):
        p = [0] * bit
        for b, v in enumerate(d):
            if not v: continue
            v %= mod
            for nb in trans[b]:
                p[nb] += v
        d = p
    print(d[0] % mod)
main()