def main():
    from sys import stdin
    from functools import reduce
    from operator import xor
    e = stdin.readline

    mask = ~(int(e()) - 1)
    print(reduce(xor, (v for i, v in enumerate(map(int, e().split())) if mask & i == 0), 0))
main()