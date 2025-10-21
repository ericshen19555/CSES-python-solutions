def main():
    from sys import stdin
    from bisect import bisect_right
    e = stdin.readline

    n = int(e())
    l = [int(v) - 1 for v in e().split()]

    bit = [0] * (n + 1)
    a1 = 0
    for v in l:
        i = v + 1
        while i <= n:
            a1 += bit[i]
            i += i & -i
        i = v + 1
        while i:
            bit[i] += 1
            i &= i - 1

    a4 = n
    it = reversed(l)
    v = n - 1
    while v in it:
        a4 -= 1
        v -= 1

    a3 = n
    lis = [-1]
    for v in l:
        if v > lis[-1]:
            lis.append(v)
            a3 -= 1
        else:
            lis[bisect_right(lis, v)] = v

    a2 = 0
    for i in range(n):
        while (j := l[i]) != i:
            l[i], l[j] = l[j], l[i]
            a2 += 1

    print(a1, a2, a3, a4)
main()