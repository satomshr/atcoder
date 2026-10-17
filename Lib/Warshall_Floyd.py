# INF = float('inf')
# ^ こっちは遅い
INF = 10**18

def warshall_floyd(n: int, edges: list) -> list:
    '''
    ワーシャルフロイド法 ; グラフ中のすべての頂点間の最短経路を求める
    返値 ; dist[i][j] -> i から j へ行く最短経路 (行けないときは INF)
    注意 ; edges は有向グラフを想定しているので, 無向グラフの際は要変更
    '''
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, cost in edges:
        dist[u][v] = min(dist[u][v], cost)
        # 無向グラフのときは下記のコメントを外す
        # dist[v][u] = min(dist[v][u], cost)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or i==k or j==k:
                    continue

                # if dist[i][k] + dist[k][j] < dist[i][j]:
                #     dist[i][j] = dist[i][k] + dist[k][j]
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    return dist

def warshall_floyd_update(dist: list, u: int, v: int, cost: int) -> list:
    '''
    ワーシャルフロイド法で計算した最短経路を更新する
    返値 ; dist[i][j] -> 更新後の i から j へ行く最短経路 (行けないときは INF)
    '''
    # 今の u->v の cost のほうが小さい場合は, 何もしない
    if dist[u][v] <= cost and dist[v][u] <= cost:
        return dist

    n = len(dist)

    for i in range(n):
        for j in range(n):
            if i==j:
                continue

            # if dist[i][u] + cost + dist[v][j] < dist[i][j]:
            #     dist[i][j] = dist[i][u] + cost + dist[v][j]
            dist[i][j] = min(dist[i][j], dist[i][u] + cost + dist[v][j])

    return dist
