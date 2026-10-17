def gcd(a: int, b: int) -> int:
    """2整数の最大公約数（非負）を返す。0や負にも対応。"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a  # どちらも0なら0を返す

def gcd_many(*nums: int) -> int:
    """複数整数の最大公約数。空なら0。"""
    from functools import reduce
    return reduce(gcd, nums, 0)

def extended_gcd(a: int, b: int):
    """
    拡張ユークリッドの互除法
    ax + by = gcd(a, b) を満たす (g, x, y) を返す
    g = gcd(a, b)
    """
    if b == 0:
        return a, 1, 0  # gcd(a,0)=a, このとき x=1, y=0
    g, x1, y1 = extended_gcd(b, a % b)
    # 再帰を戻しながら x, y を更新
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def simultaneous_congruence_equation(am: list):
    """
    連立合同方程式を解く
    x = ai (mod mi) を満たす x を返す

    am -> [(a0, m0), (a1, m1), (a2, m2), ...]
    ただし mi は互いに素
    """
    # https://for-spring.com/algebra/elemental_number_theory-12/

    m0 = 1
    for _, m in am:
        m0 *= m

    ans = 0

    for ai, m in am:
        mi = m0 // m
        _, y, _ = extended_gcd(mi, m) # 逆元
        ans += ai * mi * y

    return ans % m0, m0


# 使い方例
if __name__ == "__main__":
    print("(1) ユークリッドの互除法")
    print(gcd(54, 24))          # -> 6
    print(gcd(-18, 48))         # -> 6
    print(gcd(0, 0))            # -> 0
    print(gcd(0, 42))           # -> 42
    print(gcd_many(24, 60, 36)) # -> 12

    print("\n(2) 拡張ユークリッドの互除法")
    a, b = 240, 46
    g, x, y = extended_gcd(a, b)
    print(f"gcd({a}, {b}) = {g}")
    print(f"{a}*({x}) + {b}*({y}) = {g}")

    c = 4
    print(f"\n{a} * x + {b} * y = {c} を解く")
    x *= (c // g)
    y *= (c // g)
    print(f"{a}*({x}) + {b}*({y}) = {c}")

    print("\n逆元を求める")
    a = 3
    m = 4
    print(f"{a} * x = 1 (mod {m})")
    _, x, _ = extended_gcd(a, m)
    if x < 0:
        x += m
    print(f"{a} * {x} = 1 (mod {m})")

    print("\n(3) 連立合同方程式")
    am = [(2, 3), (3, 5), (2, 7)]
    for a, m in am:
        print(f"x = {a} (mod {m})")

    x, m = simultaneous_congruence_equation(am)
    print(f"x = {x} (mod {m})")


    am = [(1, 4), (1, 5), (1, 7), (1, 3)]
    x, m = simultaneous_congruence_equation(am)
    print(x)