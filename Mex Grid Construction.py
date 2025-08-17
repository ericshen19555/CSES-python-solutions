n = int(input())
print("\n".join(" ".join(str(i ^ j) for j in range(n)) for i in range(n)))