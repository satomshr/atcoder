def gcd(a: int, b: int) -> int:
    """最大公約数"""
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def gcd3(a: int, b: int, c: int) -> int:
    """3整数の最大公約数"""
    return gcd(gcd(a, b), c)


def line_equation(x1: int, y1: int, x2: int, y2: int) -> tuple[int, int, int]:
    """
    2点を通る直線 ax + by + c = 0 を返す。
    gcd(a,b,c)=1, a>0 (a==0ならb>0)
    """
    if x1 == x2 and y1 == y2:
        raise ValueError("same point")

    a = y2 - y1
    b = x1 - x2
    c = -(a * x1 + b * y1)

    g = gcd3(a, b, c)
    if g:
        a //= g
        b //= g
        c //= g

    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c

    return (a, b, c)


def perpendicular_bisector(
    x1: int, y1: int, x2: int, y2: int
) -> tuple[int, int, int]:
    """
    線分の垂直二等分線 ax + by + c = 0 を返す。
    gcd(a,b,c)=1, a>0 (a==0ならb>0)
    """
    if x1 == x2 and y1 == y2:
        raise ValueError("same point")

    dx = x2 - x1
    dy = y2 - y1

    # 中点の分母を払うため2倍する
    a = 2 * dx
    b = 2 * dy
    c = -(dx * (x1 + x2) + dy * (y1 + y2))

    g = gcd3(a, b, c)
    if g:
        a //= g
        b //= g
        c //= g

    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c

    return (a, b, c)


def cross(ax: int, ay: int, bx: int, by: int) -> int:
    """外積"""
    return ax * by - ay * bx


def dot(ax: int, ay: int, bx: int, by: int) -> int:
    """内積"""
    return ax * bx + ay * by


def dist2(x1: int, y1: int, x2: int, y2: int) -> int:
    """距離の二乗"""
    dx = x2 - x1
    dy = y2 - y1
    return dx * dx + dy * dy


def ccw(x1: int, y1: int,
        x2: int, y2: int,
        x3: int, y3: int) -> int:
    """
    三点の向きを返す。

     >0 : 反時計回り
     <0 : 時計回り
      0 : 一直線
    """
    return cross(x2 - x1, y2 - y1,
                 x3 - x1, y3 - y1)


def point_on_line(a: int, b: int, c: int,
                  x: int, y: int) -> bool:
    """点が直線上にあるか"""
    return a * x + b * y + c == 0


def point_on_segment(x1: int, y1: int,
                     x2: int, y2: int,
                     x: int, y: int) -> bool:
    """点が線分上にあるか"""
    if ccw(x1, y1, x2, y2, x, y) != 0:
        return False

    return (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2))


def is_parallel(a1: int, b1: int,
                a2: int, b2: int) -> bool:
    """2直線が平行か"""
    return a1 * b2 == a2 * b1


def line_intersection(a1: int, b1: int, c1: int,
                      a2: int, b2: int, c2: int):
    """
    2直線の交点を有理数で返す。

    Returns
    -------
    None
        平行

    (xn, yn, d)
        x = xn / d
        y = yn / d
    """

    d = a1 * b2 - a2 * b1

    if d == 0:
        return None

    xn = b1 * c2 - b2 * c1
    yn = a2 * c1 - a1 * c2

    if d < 0:
        d = -d
        xn = -xn
        yn = -yn

    return (xn, yn, d)


def segment_intersect(x1: int, y1: int,
                      x2: int, y2: int,
                      x3: int, y3: int,
                      x4: int, y4: int) -> bool:
    """
    線分同士が交差するか（端点を含む）
    """

    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)

    if c1 == c2 == c3 == c4 == 0:
        return (max(min(x1, x2), min(x3, x4))
                <= min(max(x1, x2), max(x3, x4))
                and
                max(min(y1, y2), min(y3, y4))
                <= min(max(y1, y2), max(y3, y4)))

    return c1 * c2 <= 0 and c3 * c4 <= 0


