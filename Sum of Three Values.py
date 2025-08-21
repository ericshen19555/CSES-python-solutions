def main():
    from sys import stdin
    from operator import itemgetter
    e = stdin.readline

    n, x = map(int, e().split())
    l = sorted(enumerate(map(int, e().split()), start=1), key=itemgetter(1))
    for k in range(2, n):
        t = x - l[k][1]
        if t < 2: continue
        i, j = 0, k - 1
        while i < j:
            cur = l[i][1] + l[j][1]
            if cur == t:
                print(l[i][0], l[j][0], l[k][0])
                return
            elif cur > t:
                j -= 1
            else:
                i += 1
    print("IMPOSSIBLE")
main()