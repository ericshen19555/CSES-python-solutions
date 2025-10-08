def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        n = int(e())
        ans.append("first" if any(v & 1 for v in map(int, e().split())) else "second")
    print("\n".join(ans))
main()
