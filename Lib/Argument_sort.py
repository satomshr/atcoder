# Argument_sort.py ; 偏角ソート by ChatGPT
from functools import cmp_to_key

# 反時計回り
def cmp_angle(a, b):
    ax, ay = a
    bx, by = b

    # 上半平面かどうか（y > 0 または y == 0 かつ x > 0）
    ha = (ay > 0) or (ay == 0 and ax > 0)
    hb = (by > 0) or (by == 0 and bx > 0)

    if ha != hb:
        # 上半平面を先に
        return -1 if ha else 1

    # 外積
    cross = ax * by - ay * bx
    if cross != 0:
        # 反時計回りを先に
        return -1 if cross > 0 else 1

    # 同一直線上：距離でソート（近い方を先）
    da = ax * ax + ay * ay
    db = bx * bx + by * by
    if da < db:
        return -1
    elif da > db:
        return 1
    else:
        return 0

# 反時計回り
def cmp_angle_cw(a, b):
    ax, ay = a
    bx, by = b

    # 上半平面（右方向を含む）
    ha = (ay > 0) or (ay == 0 and ax > 0)
    hb = (by > 0) or (by == 0 and bx > 0)

    if ha != hb:
        # 上半平面を先に
        return -1 if ha else 1

    # 外積
    cross = ax * by - ay * bx
    if cross != 0:
        # ★ 時計回り：外積の符号を反転
        return -1 if cross < 0 else 1

    # 同一直線上：距離でソート（近い方を先）
    da = ax * ax + ay * ay
    db = bx * bx + by * by
    if da < db:
        return -1
    elif da > db:
        return 1
    else:
        return 0

# テスト

points = [(-1, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (0, 1)]
points_ccw = sorted(points, key=cmp_to_key(cmp_angle))
points_cw = sorted(points, key=cmp_to_key(cmp_angle_cw))

print(points)
print(points_ccw)
print(points_cw)
