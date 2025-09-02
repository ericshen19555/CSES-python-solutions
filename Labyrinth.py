def main():
    from sys import stdin
    e = stdin.readline

    m, n = map(int, e().split())
    n += 1
    area = m * n
    l = [0] * (area + n)
    q = []
    for r in range(0, area, n):
        for i, c in enumerate(e(), r):
            if c == "#":
                l[i] = 0
            elif c == "A":
                l[i] = 0
                q.append(i)
            elif c == ".":
                l[i] = 1
            elif c == "B":
                l[i] = 2
    d = (1, n, -n, -1)
    for i in q:
        for di, ni in enumerate(d):
            ni = i + ni
            v = l[ni]
            if v < 1: continue
            l[ni] = ~di
            q.append(ni)
            if v == 2: break
        else: continue
        break
    else:
        print("NO")
        return

    print("YES")

    ans = []
    ds = "LUDR"
    while l[ni]:
        ans.append(ds[l[ni]])
        ni += d[l[ni]]

    print(len(ans))
    print("".join(reversed(ans)))
main()