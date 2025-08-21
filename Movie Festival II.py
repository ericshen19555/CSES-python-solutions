# lined list O(sort + n)

def main():
    from sys import stdin
    from operator import itemgetter
    from bisect import bisect_right
    e = stdin.readline

    n, k = map(int, e().split())
    l = [tuple(map(int, e().split())) for _ in range(n)]
    l.sort(key=itemgetter(1))
    ans = 0
    end = []
    nxt = list(range(n + 1))
    for s, t in l:
        i = bisect_right(end, s)
        while nxt[i] != i:
            nxt[i] = i = nxt[nxt[i]]

        if i: nxt[i] -= 1
        elif k: k -= 1
        else: continue

        end.append(t)
        ans += 1
    print(ans)
main()
