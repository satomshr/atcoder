'''
BIT:
  Fenwick Tree (BIT) の実装
  1-indexed であることに注意

FenwickOrderedSet:
  Fenwick Tree を利用した順序付き集合 (Ordered Set)
  要素へのアクセスは 0-indexed になります
'''
class BIT:
    def __init__(self, size):
        self.N = size + 2  # 1-based indexing
        self.tree = [0] * self.N

    def update(self, i, delta):
        while i < self.N:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def find_kth(self, k):
        """k番目の要素のインデックスを返す（1-indexed）"""
        idx = 0
        bitmask = 1 << (self.N.bit_length() - 1)
        while bitmask:
            t_idx = idx + bitmask
            if t_idx < self.N and self.tree[t_idx] < k:
                k -= self.tree[t_idx]
                idx = t_idx
            bitmask >>= 1
        return idx + 1

class FenwickOrderedSet:
    def __init__(self, max_value):
        self.max_value = max_value
        self.bit = BIT(max_value)
        self.data = set()  # To prevent duplicates

    def add(self, x):
        if x not in self.data:
            self.data.add(x)
            self.bit.update(x, 1)

    def discard(self, x):
        if x in self.data:
            self.data.remove(x)
            self.bit.update(x, -1)

    def __contains__(self, x):
        return x in self.data

    def __len__(self):
        return self.bit.query(self.max_value)

    def kth(self, k):
        """0-based index: kth(0) is the smallest element"""
        if k < 0 or k >= len(self):
            raise IndexError("k is out of bounds")
        return self.bit.find_kth(k + 1)

    def index(self, x):
        """xより小さい要素数を返す"""
        return self.bit.query(x - 1)

    def __iter__(self):
        for i in range(1, self.max_value + 1):
            if i in self.data:
                yield i


oset = FenwickOrderedSet(max_value=100)

oset.add(10)
oset.add(5)
oset.add(20)
print("All:", list(oset))          # [5, 10, 20]
print("10 in set?", 10 in oset)    # True
print("kth(0):", oset.kth(0))      # 5
print("kth(2):", oset.kth(2))      # 20
print("Index of 15:", oset.index(15))  # 2（5,10 の2つが15未満）
