def main():
    from sys import stdin
    e = stdin.readline

    e()
    ans = float("-INF")
    dp = 0
    for v in map(int, e().split()):
        dp += v
        if dp > ans: ans = dp
        if dp < 0: dp = 0
    print(ans)
main()