def main():
    from sys import stdin
    from heapq import heappush, heappop
    e = stdin.readline

    def pack(v, i):
        return v << 20 | i

    def unpack(x):
        return x >> 20, x & 0xfffff

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    half = k + 1 >> 1

    ans = []
    le, ri = [], []
    lc = 0  # 有效(not outdated)元素數量
    ls = rs = 0  # 維護左右總和
    for i, v in enumerate(l):
        # 因為要取用 ri[0] 所以要先將 outdated 移除
        # 注意這邊是 < i - k 而非 <=
        while ri and unpack(ri[0])[1] < i - k:
            heappop(ri)
        # 決定要加到左邊或右邊
        if not ri or pack(v, i) < ri[0]:
            lc += 1
            ls += v
            heappush(le, pack(-v, i))
        else:
            rs += v
            heappush(ri, pack(v, i))
        if i >= k:
            p = l[i - k]
            # 剛剛已經將 outdated 移除，這邊免了
            # 決定要從左邊或右邊刪除
            if not ri or pack(p, i - k) < ri[0]:
                lc -= 1
                ls -= p
            else:
                rs -= p
        if i >= k - 1:
            # 維持左邊有效元素數量 == half
            while lc > half:
                pv, pi = unpack(heappop(le))
                if pi + k <= i: continue
                lc -= 1
                ls -= -pv
                rs += -pv
                heappush(ri, pack(-pv, pi))
            while lc < half:
                pv, pi = unpack(heappop(ri))
                if pi + k <= i: continue
                lc += 1
                ls += pv
                rs -= pv
                heappush(le, pack(-pv, pi))
            # 刪除左邊 outdated
            # 注意這邊是 <= i - k 而非 <
            while unpack(le[0])[1] <= i - k:
                heappop(le)
            ans.append(rs - ls + (-unpack(le[0])[0] if k & 1 else 0))
    print(*ans)
main()