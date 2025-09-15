def main():
    from sys import stdin
    from math import lcm
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    ans = -1
    for i in range(n):
        c = 0
        while l[i]:
            c += 1
            j = l[i] - 1
            l[i] = 0
            i = j
        if c: ans = lcm(ans, c)
    print(ans % (10**9 + 7))
main()