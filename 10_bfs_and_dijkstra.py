import heapq
from collections import deque
import networkx as nx
#
def bfs(G, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        v = queue.popleft()            # oldest discovery first
        for w in G[v]:
            if w not in dist:          # first visit is the shortest
                dist[w] = dist[v] + 1
                queue.append(w)
    return dist
#
K = nx.karate_club_graph()
d = bfs(K, 0)
print("farthest from member 0:", max(d.values()), "hops")
print("average distance:", round(nx.average_shortest_path_length(K), 2))
#
def dijkstra(G, start):
    best = {start: 0}
    heap = [(0, start)]
    while heap:
        cost, v = heapq.heappop(heap)  # cheapest unsettled stop
        if cost > best[v]:
            continue                   # stale entry, skip it
        for w, data in G[v].items():
            new = cost + data["weight"]
            if new < best.get(w, float("inf")):
                best[w] = new          # relax: found a cheaper route
                heapq.heappush(heap, (new, w))
    return best
#
M = nx.Graph()
for a, b, w in [("S", "A", 4), ("S", "B", 1), ("B", "A", 2),
                ("A", "C", 5), ("B", "D", 7), ("C", "D", 1),
                ("C", "T", 3), ("D", "T", 6)]:
    M.add_edge(a, b, weight=w)
print(dijkstra(M, "S"))                # T costs 11
print(nx.dijkstra_path(M, "S", "T"))   # ['S', 'B', 'A', 'C', 'T']
