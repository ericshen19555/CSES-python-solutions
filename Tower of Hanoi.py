def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    if n == 1:
        print(1)
    elif n <= 3:
        print("NO SOLUTION")
    else:
        n += 1
        print(" ".join(map(str, range(2, n, 2))), " ".join(map(str, range(1, n, 2))))
main()