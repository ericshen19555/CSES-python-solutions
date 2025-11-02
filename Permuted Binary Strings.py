n = int(input())

def query(b: list[int]) -> list[int]:
    # return [b[v] for v in secret]
    print("?", "".join(map(str, b)))
    return list(map(int, input()))

def main():
    bl = n.bit_length()
    ans = [0] * n
    for k in range(bl):
        b = query([(i >> k) & 1 for i in range(n)])
        for i in range(n):
            ans[i] |= b[i] << k
    print("!", *[v + 1 for v in ans])
main()