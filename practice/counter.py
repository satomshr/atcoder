from collections import Counter

A = ['a', 'b', 'a', 'c', 'b', 'a']
B = ['b', 'a', 'a', 'c']
C = ['b', 'a', 'b', 'b', 'c']

Ca = Counter(A)
Cb = Counter(B)
Cc = Counter(C)
print(Ca) # Counter({'a': 3, 'b': 2, 'c': 1})
print(Cb) # Counter({'a': 2, 'b': 1, 'c': 1})
print(Cc) # Counter({'b': 3, 'a': 1, 'c': 1})

# 同じようなことは defaultdict を使ってもできる
from collections import defaultdict
d = defaultdict(int)
for val in A:
    d[val] += 1

print(d) # defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 1})

# Counter は dict のサブクラスなので, dict のメソッドが使える
print(Ca.keys()) # dict_keys(['a', 'b', 'c'])
print(Ca.values()) # dict_values([3, 2, 1])

for k, v in Ca.items():
    print(k, v)

# a 3
# b 2
# c 1

# 集合のように扱える
Csum = Ca + Cb
Cdiff = Ca - Cb
print(Csum) # Counter({'a': 5, 'b': 3, 'c': 2})
print(Cdiff) # Counter({'a': 1, 'b': 1})

Cdiff2 = Ca - Cc
print(Cdiff2) # Counter({'a': 2})

Cdiff3 = Ca.copy() # Ca をコピーして
Cdiff3.subtract(Cc) # Cc を引く
print(Cdiff3) # Counter({'a': 2, 'c': 0, 'b': -1})

# 比較もできる (バージョン 3.10 で変更)
print(Ca == Counter({"a":2, "b": 2, "c": 1})) # False
print(Ca == Cb) # False
print(Ca >= Cb) # True

