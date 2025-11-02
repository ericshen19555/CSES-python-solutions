n = int(input())

def query(i: int) -> bool:
    # return secret[i]
    print("?", i + 1)
    return input() == "R"

def main():
    i, m = 0, n >> 1
    c0 = query(i)
    while m:
        if i + m < n:
            c1 = query(i + m)
            if (c0 == c1) ^ (m & 1):
                i += m
                c0 = c1
        m >>= 1
    print("!", i + 1)
main()
