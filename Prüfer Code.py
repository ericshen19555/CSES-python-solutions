def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = [int(v) - 1 for v in e().split()]
    indeg = [0] * n
    for p in l:
        indeg[p] += 1
    ptr = 0
    while indeg[ptr]:
        ptr += 1
    leaf = ptr

    ans = []
    for pa in l:
        ans.append(f"{leaf + 1} {pa + 1}")
        indeg[pa] -= 1
        if indeg[pa] == 0 and pa < ptr:
            leaf = pa
        else:
            ptr += 1
            while indeg[ptr]:
                ptr += 1
            leaf = ptr
    ans.append(f"{leaf + 1} {n}")
    print("\n".join(ans))
main()