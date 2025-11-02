n, k = map(int, input().split())

def query(g: int, x: int) -> int:
    if x <= 0: return 10**10
    if x > n: return 0
    # return [f, s][g][x - 1]
    return int(input(f'{"FS"[g]} {x}\n'))

def main():
    s, t = 0, n + 1
    while s < t:
        mid = s + t >> 1
        if query(0, mid) < query(1, k - mid):
            t = mid
        else:
            s = mid + 1
    print("!", max(query(0, s), query(1, k - s + 1)))
main()