with open(r"grid_path.txt", "r") as file:
    path = file.read()

from base64 import b64decode

path = [int.from_bytes(b64decode(cur), "big") for cur in path.split()]

# s = input()
s = "?" * 48

t = dict(zip("?UDLR", ("1111", "0001", "0010", "0100", "1000"))).__getitem__
s = int("".join(map(t, s)), 2)

print(sum(1 for mask in path if (mask & s) == mask))


##############################################################
##############################################################
##############################################################

# preprocess
n = 7
end = n * n - 1
d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

s = "?" * 48

path = []
cur = []

def dfs(p, i, j):
    if i == n-1 and j == 0:
        if p != end:
            return 0
        path.append("".join(cur))
        return 1
    if end - p < n-1 - i + j:
        return 0
    if not vis[i - 1][j] and not vis[i + 1][j] and vis[i][j - 1] and vis[i][j + 1]:
        return 0
    if vis[i - 1][j] and vis[i + 1][j] and not vis[i][j - 1] and not vis[i][j + 1]:
        return 0
    if vis[i + 1][j + 1] and not vis[i + 1][j] and not vis[i][j + 1]:
        return 0
    if vis[i - 1][j + 1] and not vis[i - 1][j] and not vis[i][j + 1]:
        return 0
    if vis[i + 1][j - 1] and not vis[i + 1][j] and not vis[i][j - 1]:
        return 0
    vis[i][j] = True
    res = 0
    for k in (d.keys() if s[p] == "?" else (s[p],)):
        ni, nj = d[k]
        ni += i; nj += j
        if not vis[ni][nj]:
            cur.append(k)
            res += dfs(p + 1, ni, nj)
            cur.pop()
    vis[i][j] = False
    return res
vis = [[False] * n + [True] for _ in range(n)] + [[True] * (n + 1)]
print(dfs(0, 0, 0))

from base64 import b64encode, b64decode

with open("grid_path.txt", "w") as file:
    file.write(" ".join(path))

t = dict(zip("?UDLR", ("1111", "0001", "0010", "0100", "1000"))).__getitem__
bl = 4 * end >> 3

path = [str(b64encode(int("".join(map(t, cur)), 2).to_bytes(bl, "big")))[2:-1] for cur in path]
s = " ".join(path)
with open("grid_path_64.txt", "w") as file:
    file.write(s)
