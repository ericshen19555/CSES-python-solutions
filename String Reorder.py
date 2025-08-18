from collections import Counter

s = input()

n = len(s)
cnt = Counter(s)
t = len(cnt)
key = sorted(cnt)
val = [cnt[k] for k in key]
mi = max(range(t), key=val.__getitem__)
if val[mi] > (n + 1) >> 1:
    print(-1)
else:
    ans = []
    pre = "#"
    i, ni = 0, 1
    for n in range(n, 0, -1):
        mi = max(range(t), key=val.__getitem__)
        if val[mi] > (n >> 1):
            cur = key[mi]
            assert pre != cur
            val[mi] -= 1
        elif key[i] == pre:
            cur = key[ni]
            val[ni] -= 1
            while ni < t and val[ni] == 0:
                ni += 1
        else:
            cur = key[i]
            val[i] -= 1
            while i < t and val[i] == 0:
                i += 1
            if i == ni:
                ni += 1
                while ni < t and val[ni] == 0:
                    ni += 1
        ans.append(cur)
        pre = cur
    print("".join(ans))