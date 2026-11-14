from collections import deque

def tree_diameter(G):
    '''
    木の直径を求める
    '''

    N = len(G)

    def bfs(start):
        dist = [-1] * N
        dist[start] = 0
        que = deque([start])
        farthest = start

        while que:
            v = que.popleft()

            if dist[v] > dist[farthest]:
                farthest = v

            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    que.append(nv)

        return farthest, dist[farthest]

    u, _ = bfs(0)
    v, diameter = bfs(u)

    return diameter


def tree_center(G):
    '''
    木の中心を返す.
    直径が奇数なら 2 頂点, 偶数なら 1 頂点
    '''

    N = len(G)

    def bfs(start):
        dist = [-1] * N
        parent = [-1] * N
        dist[start] = 0
        que = deque([start])
        farthest = start

        while que:
            v = que.popleft()

            if dist[v] > dist[farthest]:
                farthest = v

            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    parent[nv] = v
                    que.append(nv)

        return farthest, parent

    # 直径の両端を求める
    u, _ = bfs(0)
    v, parent = bfs(u)

    # 直径のパスを復元
    path = []
    cur = v
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    # 中心を返す
    m = len(path) // 2
    if len(path) % 2 == 1:
        return [path[m]]
    else:
        return [path[m - 1], path[m]]

# ================
# example
# ================

# 木の直径
N = 5
G = [[] for _ in range(N)]

edges = [
    (0, 1),
    (1, 2),
    (1, 3),
    (3, 4),
]

for a, b in edges:
    G[a].append(b)
    G[b].append(a)

print(tree_diameter(G))  # 3


# 木の中心
G = [
    [1],
    [0, 2, 3],
    [1],
    [1, 4],
    [3],
]

print(tree_center(G))  # [3, 1] または [1, 3]
