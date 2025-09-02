def main():
    from sys import stdin
    e = stdin.readline

    m, n = map(int, e().split())
    n += 1
    area = m * n
    l = [3] * (area + n)
    pre = [0] * area
    q = []
    s = 0
    for r in range(0, area, n):
        for i, c in enumerate(e(), r):
            if c == "#":
                l[i] = 0
            elif c == "A":
                l[i] = 1
                s = i
                pre[i] = -1
            elif c == ".":
                l[i] = 2
            elif c == "M":
                l[i] = 0
                q.append(i)
    q.append(~s)

    d = (1, n, -n, -1)
    for i in q:
        if i < 0:
            player = True
            i = ~i
        else:
            player = False
        for di, ni in enumerate(d):
            ni = i + ni
            if player:
                if l[ni] < 2: continue
                if l[ni] == 3: break
                pre[ni] = di
            elif l[ni] < 1 or l[ni] == 3: continue
            l[ni] -= 1
            q.append(~ni if player else ni)
        else: continue
        break
    else:
        print("NO")
        return

    print("YES")

    ans = []
    ds = "RDUL"
    while pre[i] >= 0:
        ans.append(ds[pre[i]])
        i -= d[pre[i]]

    print(len(ans))
    print("".join(reversed(ans)))
main()