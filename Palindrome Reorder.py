from collections import Counter

cnt = Counter(input())
if sum(1 for c in cnt.values() if c & 1) > 1:
    print("NO SOLUTION")
else:
    for k, v in cnt.items():
        print(k * (v >> 1), end='')
    print(next((k for k, v in cnt.items() if v & 1), ""), end='')
    for k, v in reversed(tuple(cnt.items())):
        print(k * (v >> 1), end='')