from itertools import islice

class SparseTable:
    def __init__(self, arr, func):
        self.func = func

        lim = len(arr) + 1
        log_2 = self.log_2 = [-1] * lim
        for i in range(1, lim):
            log_2[i] = log_2[i >> 1] + 1
        bl = log_2[-1] + 1  # n.bit_length()

        st = self.st = [None] * bl
        pre = st[0] = tuple(arr)

        len_ = 1
        for i in range(1, bl):
            pre = st[i] = tuple(map(func, pre, islice(pre, len_, None)))
            len_ <<= 1

    def query(self, s: int, t: int) -> int:
        r = self.log_2[t - s]
        row = self.st[r]
        return self.func(row[s], row[t - (1 << r)])

def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    st = SparseTable(list(map(int, e().split())), min)
    ans = []
    for _ in range(q):
        s, t = map(int, e().split())
        ans.append(st.query(s-1, t))
    print("\n".join(map(str, ans)))
main()