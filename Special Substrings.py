def main():
    s = input()
    m = 0
    mp = [-1] * 26
    for c in s:
        c = ord(c) - 97
        if ~mp[c]: continue
        mp[c] = m
        m += 1

    ans = 0
    cur = [0] * m
    cnt = {tuple(cur): 1}
    k = 0
    for c in s:
        c = mp[ord(c) - 97]
        k += (cur[c] == 0)
        cur[c] += 1
        if k == m:
            for i in range(m):
                cur[i] -= 1
                k -= (cur[i] == 0)
        key = tuple(cur)
        x = cnt.get(key, 0)
        ans += x
        cnt[key] = x + 1
    print(ans)
main()