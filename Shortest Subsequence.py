def main():
    A = "ACGT"
    u = set()
    ans = []
    for c in input():
        u.add(c)
        if len(u) == len(A):
            ans.append(c)
            u.clear()
    for c in A:
        if c not in u:
            ans.append(c)
            break
    print("".join(ans))
main()