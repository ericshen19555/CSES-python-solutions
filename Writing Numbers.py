k = int(input())
s, t = 9, k + 11
while s < t:
    x = s + t >> 1
    c = 0
    p = 1
    while p <= x:
        q = p
        p *= 10
        c += x // p * q + max(0, min(x % p - q + 1, q))
    if c > k: t = x
    else: s = x + 1
print(s - 1)