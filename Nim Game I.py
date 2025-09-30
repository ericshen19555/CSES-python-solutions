def main():
    from sys import stdin
    from functools import reduce
    from operator import xor
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        n = int(e())
        x = reduce(xor, map(int, e().split()))
        ans.append("first" if x else "second")
    print("\n".join(ans))
main()