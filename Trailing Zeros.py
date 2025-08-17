n = int(input())
ans = 0
x = 5
while x <= n:
    ans += n // x
    x *= 5
print(ans)