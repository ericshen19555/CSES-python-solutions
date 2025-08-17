def main():
    from sys import stdin
    print("\n".join(str(i * i * (i * i - 1) // 2 - 4 * (i - 1) * (i - 2))
                    for i in range(1, int(stdin.readline()) + 1)))
main()