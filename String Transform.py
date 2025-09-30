def main():
    from string import ascii_lowercase as A
    A = "#" + A
    mp = {A[i]: i for i in range(27)}

    s = input()
    n = len(s)

    l = [0] * n
    cnt = [0] * 27
    for c in s:
        cnt[mp[c]] += 1
    for i in range(1, 27):
        cnt[i] += cnt[i - 1]
    for i in range(n-1, -1, -1):
        cnt[mp[s[i]]] -= 1
        l[cnt[mp[s[i]]]] = i

    ans = []
    i = l[0]
    for _ in range(n - 1):
        i = l[i]
        ans.append(s[i])
    print("".join(ans))
main()