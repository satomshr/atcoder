
import heapq

class Dijkstra:
    def __init__(self, n):
        """
        n: ノード数（0 から n-1）
        """
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cost):
        """
        u -> v にコスト cost の有向辺を追加
        """
        self.graph[u].append((v, cost))

    def shortest_path(self, start):
        """
        start: 始点ノード
        戻り値: 各ノードへの最短距離リスト dist、および経路復元用リスト prev
        """
        dist = [float('inf')] * self.n
        prev = [-1] * self.n
        dist[start] = 0
        hq = [(0, start)]

        while hq:
            d, u = heapq.heappop(hq)
            if dist[u] < d:
                continue
            for v, cost in self.graph[u]:
                if dist[v] > d + cost:
                    dist[v] = d + cost
                    prev[v] = u
                    heapq.heappush(hq, (dist[v], v))
        return dist, prev

    def get_path(self, start, goal, prev):
        """
        start: 始点, goal: 終点, prev: shortest_path() の出力
        戻り値: start から goal への経路（ノード列）、到達不能なら空リスト
        """
        if prev[goal] == -1 and start != goal:
            return []  # 経路が存在しない
        path = []
        cur = goal
        while cur != -1:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path if path[0] == start else []  # 念のためチェック

dij = Dijkstra(5)
dij.add_edge(0, 1, 2)
dij.add_edge(1, 2, 1)
# ノード 3 や 4 にはつながっていない

dist, prev = dij.shortest_path(0)

print("ノード0から2までの最短距離:", dist[2])        # 3
print("ノード0から2までの経路:", dij.get_path(0, 2, prev))  # [0, 1, 2]

print("ノード0から4までの最短距離:", dist[4])        # inf
print("ノード0から4までの経路:", dij.get_path(0, 4, prev))  # []
