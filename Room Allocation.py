def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = []
    for i in range(n):
        a, b = map(int, e().split())
        l.append((a << 1) << 20 | i)
        l.append((b << 1 | 1) << 20 | i)
    l.sort()
    stk = []
    res = 0
    ans = [0] * n
    for v in l:
        v, i = v >> 20, v & 0xfffff
        if v & 1:
            stk.append(ans[i])
        elif stk:
            ans[i] = stk.pop()
        else:
            res += 1
            ans[i] = res
    print(res)
    print(*ans)
main()