def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    l = sorted(map(int, e().split()))
    ans = ["L"] * n
    ans[0] = "W"
    for i in range(1, n):
        for v in l:
            if (j := i - v) < -1: break
            if j == -1 or ans[j] == "L":
                ans[i] = "W"
                break
    print("".join(ans))
main()