def main():
    from sys import stdin
    e = stdin.readline

    def dfs(l):
        if not l: return 1
        res = 0
        for i, v in enumerate(l[0]):
            if not v: continue
            l_ = [row[:] for row in l[1:]]
            for j, row in enumerate(l_, 1):
                row[i] = False
                if i - j >= 0: row[i - j] = False
                if i + j <  8: row[i + j] = False
            res += dfs(l_)
        return res

    l = [[v == "." for v in e().rstrip()] for _ in range(8)]
    print(dfs(l))
main()