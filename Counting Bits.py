def main():
    from sys import stdin
    e = stdin.readline

    n = int(e()) + 1
    ans = 0
    b = 1
    mask = -1
    while b < n:
        ans += ((n >> 1) & mask)
        mask <<= 1
        if (r := n & ~mask) > b:
            ans += r - b
        b <<= 1
    print(ans)
main()