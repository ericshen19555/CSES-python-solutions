def main():
    from sys import stdin
    e = stdin.readline

    lim = 10**6 + 1
    fac_num = [1] * lim  # 1
    for d in range(2, lim):
        for m in range(d, lim, d):
            fac_num[m] += 1

    ans = []
    for _ in range(int(e())):
        ans.append(fac_num[int(e())])
    print("\n".join(map(str, ans)))
main()