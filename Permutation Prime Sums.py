# TODO: try optimizing(?): https://cses.fi/problemset/hack/3423/entry/13274103/

def main():
    n = int(input())
    lim = n * 2 + 1
    sieve = [True] * lim
    sieve[0] = sieve[1] = False
    for i, v in enumerate(sieve):
        if not v: continue
        for j in range(i * i, lim, i):
            sieve[j] = False
    ps = [i for i, v in enumerate(sieve) if v]

    pr = [0] * (n + 1)
    s = len(ps) - 1
    for i in range(n, 0, -1):
        if pr[i]: continue
        while i << 1 < ps[s]: s -= 1
        for pi in range(s, -1, -1):
            j = ps[pi] - i
            if not pr[j]:
                pr[j] = i
                pr[i] = j
                break
    print(*range(1, n + 1))
    print(*pr[1:])
main()