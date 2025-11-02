def query(x: int) -> bool:
    # return x < secret
    print(f"? {x}", flush=True)
    return input() == "YES"

def main():
    s, t = 1, 10**9 + 1
    while s < t:
        mid = s + t >> 1
        if query(mid):
            s = mid + 1
        else:
            t = mid
    print(f"! {s}")
main()