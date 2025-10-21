def main():
    n = int(input())
    nn = n * n
    half = nn >> 1

    s, t = 0, nn + 1 >> 1
    while s < t:
        mid = s + t >> 1
        lo = mid // n
        res = n * lo
        for i in range(lo + 1, n + 1):
            res += mid // i
        if res > half:
            t = mid
        else:
            s = mid + 1
    print(s)
main()