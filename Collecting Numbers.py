def main():
    from sys import stdin
    from itertools import pairwise, starmap
    from operator import gt
    e = stdin.readline

    l = [0] * int(e())
    for i, v in enumerate(map(int, e().split())):
        l[v-1] = i
    print(1 + sum(starmap(gt, pairwise(l))))
main()