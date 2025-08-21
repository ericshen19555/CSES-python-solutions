def main():
    from sys import stdin
    from bisect import bisect_right
    e = stdin.readline

    e()
    lis = [0]
    for v in map(int, e().split()):
        if v >= lis[-1]:
            lis.append(v)
        else:
            lis[bisect_right(lis, v)] = v
    print(len(lis) - 1)
main()