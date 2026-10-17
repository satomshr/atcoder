# https://atcoder.jp/contests/abc456/submissions/75463015

import sys
# 再帰の深さ制限を拡張（深いDFSに対応）
sys.setrecursionlimit(2000000)

# 有向グラフ g に閉路（サイクル）が存在するか判定する関数
def cycle_detection(g):
    # 頂点数
    n = len(g)

    # visited:
    #   DFS探索中または探索済みの頂点を記録
    # finished:
    #   その頂点から到達可能な探索がすべて完了したかを記録
    visited, finished = [False] * n, [False] * n

    # 頂点 x からDFSを行い、閉路が見つかれば True
    def dfs(x):
        # すでに探索中の頂点に再訪した場合、閉路あり
        if visited[x]:
            return False

        # 訪問開始
        visited[x] = True

        # 隣接頂点を探索
        for y in g[x]:
            # 探索完了済みなら閉路判定不要
            if finished[y]:
                continue

            # 探索中ノードへの到達、または再帰先で閉路発見なら True
            if visited[y] or dfs(y):
                return True

        # 頂点 x の探索終了
        finished[x] = True

        # この経路では閉路なし
        return False

    # 全頂点を起点に探索
    ret = False
    for x in range(n):
        ret |= dfs(x)

    # グラフ全体に閉路があれば True
    return ret
