def main():
    mod = 10**9 + 7
    area = int(input()) ** 2
    print(pow(4, -1, mod) * (pow(2, area, mod) + (pow(2, area >> 2 | area & 1, mod) * 2) + pow(2, area >> 1 | area & 1, mod)) % mod)
main()