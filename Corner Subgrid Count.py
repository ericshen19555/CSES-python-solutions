def main():
    from sys import stdin
    e = stdin.readline
    n = int(e())
    l = [0] * n
    ans = 0
    for i in range(n):
        bi = l[i] = int(e(), 2)
        for j in range(i):
            c = (bi & l[j]).bit_count()
            ans += c * (c - 1) >> 1
    print(ans)
main()