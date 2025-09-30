def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        n = int(e())
        x = 0
        for i, v in enumerate(map(int, e().split())):
            if i & 1:
                x ^= v
        ans.append("first" if x else "second")
    print("\n".join(ans))
main()