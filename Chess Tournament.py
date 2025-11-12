def main():
    from sys import stdin
    from heapq import heapify, heappop, heappush
    e = stdin.readline

    n = int(e())
    h = [(-v, i) for i, v in enumerate(map(int, e().split())) if v]
    heapify(h)

    ans = []
    while h:
        vi, i = heappop(h)
        if len(h) < -vi:
            return print("IMPOSSIBLE")
        hh = [heappop(h) for _ in range(-vi)]
        for vj, j in hh:
            ans.append(f"{i + 1} {j + 1}")
            if vj < -1:
                heappush(h, (vj + 1, j))
    print(len(ans))
    print("\n".join(ans))
main()