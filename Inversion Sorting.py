n = int(input())

def query(i, j):
    print(i + 1, j)
    return int(input())
    secret[i:j] = secret[i:j][::-1]
    return sum(secret[j] > secret[i] for i in range(n) for j in range(i))

def main():
    ans = []
    pre = query(0, n); query(0, n)
    rest = [1] * n
    r = n
    for i in range(1, n):
        r -= 1
        cur = query(i, n) - pre
        sm = 0
        for v in range(n):
            if rest[v]:
                if sm - (r - sm) == cur:
                    ans.append(v)
                    rest[v] = 0
                    break
                sm += 1
        pre += cur
        query(i, n)
    ans.append(rest.index(1))

    for v in range(n):
        i = ans.index(v)
        ans[v:i+1] = ans[v:i+1][::-1]
        query(v, i + 1)
main()
