def main():
    from sys import stdin
    from heapq import heappush, heappop
    l = [int(v) - 1 for v in stdin.read().split()]

    def dis(l):
        res = 0
        for i in range(3):
            for j in range(3):
                ii, jj = divmod(l[i * 3 + j], 3)
                res += abs(i - ii) + abs(j - jj)
        return res

    def encode(l):
        res = 0
        b = 1
        for v in l:
            res += v * b
            b *= 9
        return res

    swap = [(i - 1, i) for i in range(9) if i % 3] + [(i, i + 3) for i in range(6)]

    if l == list(reversed(range(9))):
        print(16)
        return

    vis = {encode(l)}
    cnt = 0
    q = [(dis(l) + 1 >> 1, 0, 1, l)]
    cnt += 1
    while q:
        vd, v, _, l = heappop(q)
        if vd == v:
            print(v)
            break
        for i, j in swap:
            p = l[:]
            p[i], p[j] = p[j], p[i]
            key = encode(p)
            if key in vis: continue
            vis.add(key)
            heappush(q, (v + 1 + (dis(p) + 1 >> 1), v + 1, cnt, p))
            cnt += 1
main()