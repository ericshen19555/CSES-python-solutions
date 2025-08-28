def main():
    from sys import stdin
    e = stdin.readline

    e()
    bit = 1
    for v in map(int, e().split()):
        bit |= bit << v
    bit &= -2
    print(bit.bit_count())
    print(" ".join(str(i) for i, v in enumerate(f"{bit:b}"[::-1]) if v == "1"))
main()