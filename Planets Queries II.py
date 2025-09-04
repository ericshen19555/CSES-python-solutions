def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    nxt = [int(v) - 1 for v in e().split()]

    group_of = [-1] * n
    entry = list(range(n))
    entry_dis = [0] * n
    cycle_pos = [-1] * n
    cycle_len = []
    group_counter = 0
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

        tail = i
        if group_of[tail] == group_counter:
            k = path.index(tail)
            for i in range(k):
                entry[path[i]] = tail
                entry_dis[path[i]] = k - i
            for i in range(k, size):
                cycle_pos[path[i]] = i - k
            cycle_len.append(size - k)
            group_counter += 1
        else:
            for i in range(size):
                group_of[path[i]] = group_of[tail]
                entry_dis[path[i]] = entry_dis[tail] + size - i
                entry[path[i]] = entry[tail]

    jump = nxt
    binary_lifting = [jump]
    for _ in range(18):
        jump = [jump[jump[i]] for i in range(n)]
        binary_lifting.append(jump)

    ans = []
    for _ in range(q):
        i, j = map(int, e().split())
        i, j = i-1, j-1
        if i == j:
            ans.append(0)
        elif group_of[i] != group_of[j] or entry_dis[i] < entry_dis[j]:
            ans.append(-1)
        elif entry_dis[j] == 0:
            ans.append(entry_dis[i] + (cycle_pos[j] - cycle_pos[entry[i]]) % cycle_len[group_of[j]])
        elif entry_dis[i] == entry_dis[j]:
            ans.append(-1)
        else:
            dis = entry_dis[i] - entry_dis[j]
            ii, k = i, 0
            while dis:
                if dis & 1:
                    ii = binary_lifting[k][ii]
                dis >>= 1
                k += 1
            if ii == j:
                ans.append(entry_dis[i] - entry_dis[j])
            else:
                ans.append(-1)

    print("\n".join(map(str, ans)))
main()