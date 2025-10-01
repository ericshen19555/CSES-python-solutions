def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    R = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        R[b].append(a)
        indeg[a] += 1

    bits = [1 << i for i in range(n)]
    q = [i for i in range(n) if indeg[i] == 0]
    for i in q:
        b = bits[i]
        for j in R[i]:
            bits[j] |= b
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    print(*[b.bit_count() for b in bits])
main()