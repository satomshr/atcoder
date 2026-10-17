# ac-library-python 遅延セグメントツリー チートシート

## 1. 基本的な考え方

遅延セグメントツリー（LazySegTree）は、次の2つを組み合わせたデータ構造です：

-   区間の値（モノイド）
-   区間に対する操作（遅延評価）

``` python
from atcoder.lazysegtree import LazySegTree

def op(a, b):
    ...

e = ...

def mapping(f, x):
    ...

def composition(f, g):
    ...

id_ = ...

seg = LazySegTree(op, e, mapping, composition, id_, v)
```

------------------------------------------------------------------------

## 2. よく使うパターン

### 区間加算 + 総和
#### コード
``` python
def op(a, b):
    return (a[0] + b[0], a[1] + b[1])

e = (0, 0)

def mapping(f, x):
    return (x[0] + f * x[1], x[1])

def composition(f, g):
    return f + g

id_ = 0

v = [(a, 1) for a in A]
seg = LazySegTree(op, e, mapping, composition, id_, v)
```

#### 区間和
``` python
# [1,4) = 2+3+4
print(seg.prod(1, 4)[0])
```

#### 区間加算
``` python
# 区間 [1, 4) に +10 する
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
print(seg.get(2)[0])
```

#### 1 点更新
``` python
# A[2] = 100
seg.set(2, (100, 1))
```

------------------------------------------------------------------------

### 区間加算 + 総和 (MOD)
#### コード
``` python
def op(a, b):
    return ((a[0] + b[0]) % MOD, a[1] + b[1])

e = (0, 0)

def mapping(f, x):
    return ((x[0] + f * x[1]) % MOD, x[1])

def composition(f, g):
    return (f + g) % MOD

id_ = 0

v = [(a % MOD, 1) for a in A]
seg = LazySegTree(op, e, mapping, composition, id_, v)
```

#### 区間和
``` python
# [1,4) = 2+3+4
print(seg.prod(1, 4)[0])
```

#### 区間加算
``` python
# 区間 [1, 4) に +10 する
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
print(seg.get(2)[0])
```

#### 1 点更新
``` python
# A[2] = 100
seg.set(2, (100, 1))
```


------------------------------------------------------------------------

### 区間加算 + 最大値
#### コード
``` python
def op(a, b):
    return max(a, b)

e = -10**18

def mapping(f, x):
    return x + f

def composition(f, g):
    return f + g

id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, A)
```

#### 区間最大値の取得
``` python
# [1,4)
print(seg.prod(1, 4))
```

#### 区間加算
``` python
# [1, 4) に +10
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
print(seg.get(2))
```

#### 1 点更新
``` python
seg.set(2, 100)
```
------------------------------------------------------------------------

### 区間代入 + 総和
#### コード
``` python
def op(a, b):
    return (a[0] + b[0], a[1] + b[1])

e = (0, 0)

def mapping(f, x):
    if f is None:
        return x
    return (f * x[1], x[1])

def composition(f, g):
    if f is None:
        return g
    return f

id_ = None

v = [(a, 1) for a in A]
seg = LazySegTree(op, e, mapping, composition, id_, v)
```

#### 区間和を取得
``` python
# [1,4)
print(seg.prod(1, 4)[0])
```

#### 区間代入
``` python
# 区間 [1, 4) に 10 を代入
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
print(seg.get(2)[0])
```

#### 1 点更新
``` python
seg.set(2, (100, 1))
```

------------------------------------------------------------------------

### 区間代入 + 最大値
#### コード例
``` python
def op(a, b):
    return max(a, b)

e = -10**18

def mapping(f, x):
    # f: 代入する値
    if f is None:
        return x
    return f

def composition(f, g):
    # 先に g、その後 f
    if f is None:
        return g
    return f

id_ = None

seg = LazySegTree(op, e, mapping, composition, id_, A)
```

#### 区間最大値
``` python
# [1, 4)
print(seg.prod(1, 4))
```

#### 区間代入
``` python
# [1, 4) を 10 にする
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
print(seg.get(2))
```

#### 1 点更新
``` python
seg.set(2, 100)
```
------------------------------------------------------------------------

### 区間加算 + 2乗和
#### コード
``` python
def op(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

e = (0, 0, 0)

def mapping(f, x):
    s, sq, l = x
    return (
        s + f * l,
        sq + 2 * f * s + f * f * l,
        l
    )

def composition(f, g):
    return f + g

id_ = 0

v = [(a, a*a, 1) for a in A]
seg = LazySegTree(op, e, mapping, composition, id_, v)

```

#### 区間和・2 乗和の取得
``` python
# [1,4)
s, sq, _ = seg.prod(1, 4)
print(s)
print(sq)
```

#### 区間加算
``` python
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
s, sq, _ = seg.get(2)
```

#### 1 点更新
``` python
# A[2] = 100
seg.set(2, (100, 10000, 1))
```

------------------------------------------------------------------------

### 区間代入 + 2乗和
#### コード
``` python
def op(a, b):
    return (
        a[0] + b[0],    # sum
        a[1] + b[1],    # square sum
        a[2] + b[2]     # length
    )

e = (0, 0, 0)

def mapping(f, x):
    s, sq, l = x
    if f is None:
        return x
    return (
        f * l,
        f * f * l,
        l
    )

def composition(f, g):
    # 先に g、その後 f
    if f is None:
        return g
    return f

id_ = None

v = [(a, a * a, 1) for a in A]
seg = LazySegTree(op, e, mapping, composition, id_, v)
```

#### 区間和・2 乗和
``` python
# [1,4)
s, sq, _ = seg.prod(1, 4)
print(s)
print(sq)
```

#### 区間代入
``` python
# 区間 [1, 4) に 10 を代入
seg.apply(1, 4, 10)
```

#### 1 点取得
``` python
s, sq , _ = seg.get(2)
```

#### 1 点代入
``` python
seg.set(2, (100, 10000, 1))
```
------------------------------------------------------------------------

## 4. 範囲

半開区間 \[l, r)

``` python
seg.prod(l, r)
```

------------------------------------------------------------------------

## 5. apply / prod

``` python
seg.apply(l, r, f)
seg.prod(l, r)
```

------------------------------------------------------------------------

## 6. よくあるミス

-   半開区間を忘れる
-   長さを持たない
-   2乗和だけ持つ
