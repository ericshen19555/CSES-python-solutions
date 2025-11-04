# TODO: optimize: https://cses.fi/problemset/hack/3422/entry/14322958/

def main():
    from sys import stdin
    from random import shuffle
    e = stdin.readline

    n = int(e())
    a = list(map(int, e().split()))
    b = list(map(int, e().split()))
    if n <= 2:
        print("IMPOSSIBLE")
        return
    c = list(range(1, n + 1))
    while True:
        if all(x != z and y != z for x, y, z in zip(a, b, c)):
            break
        shuffle(c)
    print(*c)
main()