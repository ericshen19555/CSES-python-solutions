def query(i: int, j: int) -> bool:
    # return secret[i] < secret[j]
    print(f"? {i + 1} {j + 1}", flush=True)
    return input() == "YES"

def main():
    from functools import cmp_to_key
    n = int(input())
    def cmp(i: int, j: int) -> int:
        return -1 if query(i, j) else 1
    l = list(range(n))
    l.sort(key=cmp_to_key(cmp))
    print("!", *[l.index(i) + 1 for i in range(n)])
main()