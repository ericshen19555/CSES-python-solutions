def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, e().split())

    siz = 1 << 15
    l = [0] * n
    s = [0] * n
    p = [0] * n
    c = [0] * siz
    for i in range(n): c[b[i] & 32767] += 1
    for i in range(1, siz): c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        x = b[i] & 32767
        c[x] -= 1
        p[c[x]] = i
    c = [0] * siz
    for i in range(n): c[b[p[i]] >> 15] += 1
    for i in range(1, siz): c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        x = b[p[i]] >> 15
        c[x] -= 1
        l[~c[x]] = p[i]
    pre = 0
    for i in range(n):
        cur = b[l[i]]
        s[l[i]] = s[l[i - 1]] if pre == cur else i
        pre = cur
    c = [0] * siz
    for i in range(n): c[a[l[i]] & 32767] += 1
    for i in range(1, siz): c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        x = a[l[i]] & 32767
        c[x] -= 1
        p[c[x]] = l[i]
    c = [0] * siz
    for i in range(n): c[a[p[i]] >> 15] += 1
    for i in range(1, siz): c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        x = a[p[i]] >> 15
        c[x] -= 1
        l[c[x]] = p[i]

    ans = [0] * n
    bit = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        i = l[i]
        x = v = n - s[i]
        res = 0
        while x:
            res += bit[x]
            x &= x - 1
        ans[i] = res
        x = v
        while x <= n:
            bit[x] += 1
            x += x & -x
    print(*ans)
    bit = [0] * (n + 1)
    for i in range(n):
        i = l[i]
        x = v = s[i] + 1
        res = 0
        while x:
            res += bit[x]
            x &= x - 1
        ans[i] = res
        x = v
        while x <= n:
            bit[x] += 1
            x += x & -x
    print(*ans)
main()