# https://qiita.com/manuo/items/12aa4e28795bd20c6d47

from typing import List, Tuple

# 点を (x, y) のタプルで表す
Point = Tuple[int, int]


def sub(p1: Point, p2: Point) -> Point:
    """
    2点の差ベクトルを求める。

    Parameters
    ----------
    p1, p2 : Point
        2次元平面上の点

    Returns
    -------
    Point
        ベクトル p2 -> p1
    """
    return (p1[0] - p2[0], p1[1] - p2[1])


def signed_area_vector(v1: Point, v2: Point) -> int:
    """
    2つのベクトルが張る平行四辺形の符号付き面積を求める。

    これは外積
        v1.x * v2.y - v1.y * v2.x
    に相当し、絶対値は平行四辺形の面積となる。

    戻り値の符号は次の意味を持つ。

    * 正：v2 は v1 の左側（反時計回り）
    * 負：v2 は v1 の右側（時計回り）
    * 0 ：3点が一直線上

    Parameters
    ----------
    v1, v2 : Point
        2次元ベクトル

    Returns
    -------
    int
        符号付き面積（＝外積）
    """
    area = v1[0] * v2[1] - v2[0] * v1[1]
    return area


def convex_hull_list(p_list: List[Point]) -> List[Point]:
    """
    Monotone Chain 法で凸包を求める。

    凸包の頂点を、
        x 座標が最小（同じなら y が最小）の点から始めて
        反時計回り
    に並べて返す。

    共線な点は凸包から除外され、
    各辺の両端のみが残る。

    Parameters
    ----------
    p_list : list[Point]
        点集合（3点以上）

    Returns
    -------
    list[Point]
        凸包を構成する頂点列

    Notes
    -----
    時間計算量は O(N log N)。
    ソートが支配的であり、凸包構築部分は O(N)。
    """
    assert len(p_list) >= 3

    # x, y の辞書順にソート
    p_list.sort()

    res = []
    k = 0

    # -------------------------
    # 下側凸包 (Lower Hull)
    # -------------------------
    for p in p_list:
        # 時計回りまたは一直線なら最後の点は不要
        while (
            k >= 2
            and signed_area_vector(
                sub(res[k - 1], res[k - 2]),
                sub(p, res[k - 1])
            ) <= 0
        ):
            res.pop()
            k -= 1

        res.append(p)
        k += 1

    # 上側凸包を追加し始める位置
    t = k + 1

    # -------------------------
    # 上側凸包 (Upper Hull)
    # -------------------------
    for p in p_list[:-1][::-1]:
        while (
            k >= t
            and signed_area_vector(
                sub(res[k - 1], res[k - 2]),
                sub(p, res[k - 1])
            ) <= 0
        ):
            res.pop()
            k -= 1

        res.append(p)
        k += 1

    # 始点が重複しているので削除
    res.pop()

    return res


def area_convex_hull(p_list: List[Point]) -> int:
    """
    凸包の面積の2倍を求める。

    多角形の面積は靴紐公式（Shoelace Formula）で計算する。

    座標がすべて整数なら、
    面積の2倍は必ず整数となるため、浮動小数点誤差が生じない。

    Parameters
    ----------
    p_list : list[Point]
        点集合

    Returns
    -------
    int
        凸包の面積の2倍
    """
    res = convex_hull_list(p_list)

    ans = sum(
        signed_area_vector(res[i], res[(i + 1) % len(res)])
        for i in range(len(res))
    )

    return abs(ans)
