n = int(input())
print("\n".join(f"{i ^ (i >> 1):0{n}b}" for i in range(1 << n)))