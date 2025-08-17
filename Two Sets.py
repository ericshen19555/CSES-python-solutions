def main():
    n = int(input())
    if n & 3 and (n + 1) & 3:
        print("NO")
    else:
        a, b = [], []
        t = n * (n + 1) >> 2
        for v in range(n, 0, -1):
            if v <= t:
                a.append(v)
                t -= v
            else:
                b.append(v)
        print(f"YES\n"
              f"{len(a)}")
        print(*a)
        print(len(b))
        print(*b)
main()