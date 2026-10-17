'''
FenwickTree
  こちらは外面は 0-indexed です

OrderedSet
  順序付き集合 (座標圧縮) です
  最初に登録する値のリストを与える必要があり, さらに値を add していく必要があります
  想定外の値で index すると, エラーになります
'''
class FenwickTree:
    def __init__(self, size):
        self.N = size + 2 # 1-based indexing
        self.tree = [0] * self.N
        
    def update(self, i, delta):
        i += 1  # convert to 1-based
        while i < self.N:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1  # convert to 1-based
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def find_kth(self, k):
        idx = 0
        bitmask = 1 << (self.N.bit_length() - 1)
        while bitmask:
            next_idx = idx + bitmask
            if next_idx < self.N and self.tree[next_idx] < k:
                k -= self.tree[next_idx]
                idx = next_idx
            bitmask >>= 1
        return idx  # 0-based index

class OrderedSet:
    def __init__(self, values):
        # 座標圧縮
        self.sorted_vals = sorted(set(values))
        self.val_to_idx = {v: i for i, v in enumerate(self.sorted_vals)}
        self.idx_to_val = {i: v for i, v in enumerate(self.sorted_vals)}
        self.ft = FenwickTree(len(self.sorted_vals))
        self.present = set()

    def add(self, x):
        """
        x を追加する. 初期化した際の要素にない場合はエラーになる.
        """
        if x not in self.val_to_idx:
            raise ValueError(f"Unexpected value: {x} (not in initial domain)")
        if x not in self.present:
            i = self.val_to_idx[x]
            self.ft.update(i, 1)
            self.present.add(x)

    def discard(self, x):
        """
        x を削除する. add されていない値を指定した場合は何もしない
        """
        if x in self.present:
            i = self.val_to_idx[x]
            self.ft.update(i, -1)
            self.present.remove(x)

    def __contains__(self, x):
        return x in self.present

    def index(self, x):
        if x not in self.val_to_idx:
            raise ValueError(f"Unexpected value: {x}")
        i = self.val_to_idx[x]
        return self.ft.query(i - 1)

    def kth(self, k):
        if k < 0 or k >= len(self):
            raise IndexError("k out of bounds")
        idx = self.ft.find_kth(k + 1)
        return self.idx_to_val[idx]

    def __len__(self):
        return self.ft.query(len(self.sorted_vals) - 1)

    def __iter__(self):
        for v in self.sorted_vals:
            if v in self.present:
                yield v

    def lower(self, x):
        """
        x より小さい集合内の最大要素（存在しなければ None）
        """
        # x より小さい値を圧縮済みリストから探す
        from bisect import bisect_left

        i = bisect_left(self.sorted_vals, x)  # x 未満の要素数
        while i > 0:
            i -= 1
            v = self.sorted_vals[i]
            if v in self.present:
                return v
        return None
    
    def upper(self, x):
        """
        x より大きい集合内の最小要素（存在しなければ None）
        """
        from bisect import bisect_right

        i = bisect_right(self.sorted_vals, x)
        while i < len(self.sorted_vals):
            v = self.sorted_vals[i]
            if v in self.present:
                return v
            i += 1
        return None
    
    def floor(self, x):
        """
        x 以下で最大の集合要素（存在しなければ None）
        """
        from bisect import bisect_right

        i = bisect_right(self.sorted_vals, x)
        while i > 0:
            i -= 1
            v = self.sorted_vals[i]
            if v in self.present:
                return v
        return None

    def ceil(self, x):
        """
        x 以上で最小の集合要素（存在しなければ None）
        """
        from bisect import bisect_left

        i = bisect_left(self.sorted_vals, x)
        while i < len(self.sorted_vals):
            v = self.sorted_vals[i]
            if v in self.present:
                return v
            i += 1
        return None


values = [100, 300, 1000, 500, 10]
oset = OrderedSet(values)

oset.add(300)
oset.add(100)
oset.add(500)
oset.add(10)

print("中身:", list(oset)) # [10, 100, 300, 500]
print("300 in oset?", 300 in oset) # True
print("index of 300:", oset.index(300)) # 2
print("kth(0):", oset.kth(0)) # 10
print("kth(2):", oset.kth(2)) # 300

oset.discard(100)
print("中身 after discard:", list(oset)) # [10, 300, 500]

print("Lower")
print(oset.lower(20)) # 10
print(oset.lower(10)) # None
print(oset.lower(400)) # 300
print(oset.lower(5)) # None

print("Upper")
print(oset.upper(5)) # 10
print(oset.upper(20)) # 300
print(oset.upper(300)) # 500
print(oset.upper(600)) # None

print("Floor")
print(oset.floor(20)) # 10
print(oset.floor(10)) # 10
print(oset.floor(400)) # 300
print(oset.floor(5)) # None

print("Ceil")
print(oset.ceil(5)) # 10
print(oset.ceil(20)) # 300
print(oset.ceil(300)) # 300
print(oset.ceil(600)) # None
