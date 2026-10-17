INF = 10**18

def bellman_ford(n, edges, start):
    """
    ベルマンフォード法

    Parameters
    ----------
    n : int
        頂点数 (0 ～ n-1)
    edges : list[(u, v, cost)]
        有向辺のリスト
    start : int
        始点

    Returns
    -------
    dist : list
        start から各頂点への最短距離
        到達不能なら INF
    negative : list
        負閉路の影響を受ける頂点なら True
    """

    dist = [INF] * n
    dist[start] = 0

    # 最短距離の更新
    for _ in range(n - 1):
        updated = False
        for u, v, cost in edges:
            if dist[u] == INF:
                continue
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                updated = True
        if not updated:
            break

    # 負閉路の検出
    negative = [False] * n

    for _ in range(n):
        for u, v, cost in edges:
            if dist[u] == INF:
                continue
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                negative[v] = True
            if negative[u]:
                negative[v] = True

    return dist, negative


n = 5

edges = [
    (0, 1, 2),
    (0, 2, 5),
    (1, 2, -4),
    (2, 3, 2),
    (3, 4, 3),
]

dist, negative = bellman_ford(n, edges, 0)

for i in range(n):
    if negative[i]:
        print(i, "NEGATIVE CYCLE")
    elif dist[i] == INF:
        print(i, "INF")
    else:
        print(i, dist[i])
