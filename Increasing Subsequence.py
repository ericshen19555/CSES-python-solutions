def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    e()  # n
    lis = []
    mx = 0
    for v in map(int, e().split()):
        if v > mx:
            lis.append(v)
            mx = v
        else:
            lis[bisect_left(lis, v)] = v
            mx = lis[-1]
    print(len(lis))
main()