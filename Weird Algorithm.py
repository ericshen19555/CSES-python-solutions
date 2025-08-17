def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    ans = [n]
    while n != 1:
        if n & 1:
            n = n * 3 + 1
        else:
            n >>= 1
        ans.append(n)
    print(*ans)
main()