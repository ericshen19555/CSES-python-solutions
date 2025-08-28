def main():
    from sys import stdin
    e = stdin.readline

    e()  # n
    stk = []
    pv, px = float("INF"), 0
    for v in map(int, e().split()):
        x = 1
        while pv < v:
            x = px + 1
            pv, px = stk.pop()
            px = max(px, x)
        if pv != v:
            stk.append((pv, px))
            pv, px = v, x
    stk.append((pv, px))
    print(max(x[1] + i for i, x in enumerate(stk, -1)))
main()
