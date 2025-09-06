def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    nxt = [int(v) - 1 for v in e().split()]

    group_of = [-1] * n
    group_counter = 0
    ans = [0] * n
    for i in range(n):
        if group_of[i] != -1: continue
        group_of[i] = group_counter
        path = [i]
        head, i = i, nxt[i]
        while group_of[i] == -1:
            path.append(i)
            group_of[i] = group_counter
            i = nxt[i]
        size = len(path)

        if group_of[i] == group_counter:
            k = path.index(i)
            cycle_size = size - k
            for i in range(k):
                ans[path[i]] = cycle_size + k - i
            for i in range(k, size):
                ans[path[i]] = cycle_size
            group_counter += 1
        else:
            group = group_of[i]
            count = ans[i]
            for i in range(size):
                group_of[path[i]] = group
                ans[path[i]] = count + size - i

    print(" ".join(map(str, ans)))
main()