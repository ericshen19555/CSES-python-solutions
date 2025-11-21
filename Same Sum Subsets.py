def main():
    from sys import stdin
    from random import shuffle
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    n1 = n >> 1
    n2 = n - n1
    b1 = 1 << n1
    b2 = 1 << n2
    mask = b2 - 1

    ctz = [-1] * b2
    for i in range(1, b2):
        ctz[i] = ctz[(i & -i) >> 1] + 1

    s1 = [0] * b1
    s2 = [0] * b2
    while True:
        shuffle(l)
        for b in range(1, b1):
            i = ctz[b]
            s1[b] = s1[b & (b - 1)] + l[i]
        mp = {v: b for b, v in enumerate(s1)}
        for b in range(1, b2):
            i = ctz[b] + n1
            s2[b] = v = s2[b & (b - 1)] + l[i]
            bb = mp.get(v)
            if bb is not None:
                ans = []
                while bb:
                    ans.append(l[ctz[bb]])
                    bb &= bb - 1
                print(len(ans))
                print(*ans)
                ans = []
                while b:
                    ans.append(l[ctz[b] + n1])
                    b &= b - 1
                print(len(ans))
                print(*ans)
                return
        for b in range(1, b2 >> 1):
            cb = b ^ mask
            if s2[b] < s2[cb]: b, cb = cb, b
            bb = mp.get(s2[b] - s2[cb])
            if bb is not None:
                ans = []
                while bb:
                    ans.append(l[ctz[bb]])
                    bb &= bb - 1
                while cb:
                    ans.append(l[ctz[cb] + n1])
                    cb &= cb - 1
                print(len(ans))
                print(*ans)
                ans = []
                while b:
                    ans.append(l[ctz[b] + n1])
                    b &= b - 1
                print(len(ans))
                print(*ans)
                return
main()