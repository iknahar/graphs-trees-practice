import networkx as nx
#
roads = nx.Graph()
roads.add_edge("start", "highway", weight=12)    # weight = minutes
roads.add_edge("highway", "airport", weight=8)
roads.add_edge("start", "dirt road", weight=15)
roads.add_edge("dirt road", "airport", weight=10)
#
print(nx.dijkstra_path(roads, "start", "airport"))   # via highway
roads["start"]["highway"]["weight"] = 45              # the crash
print(nx.dijkstra_path(roads, "start", "airport"))   # via dirt road
roads["start"]["dirt road"]["weight"] = 999          # rain made it mud
print(nx.dijkstra_path(roads, "start", "airport"))   # back to highway
print(nx.dijkstra_path_length(roads, "start", "airport"), "minutes")  # 53
