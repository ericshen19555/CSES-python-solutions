def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    cnt = [0] * n
    cnt[0] = 1
    ans = pre = 0
    for v in map(int, e().split()):
        pre = (pre + v) % n
        ans += cnt[pre]
        cnt[pre] += 1
    print(ans)
main()