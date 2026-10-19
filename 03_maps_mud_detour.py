import networkx as nx
#
# roads to the airport; weight = minutes the app expects
roads = nx.Graph()
roads.add_edge("start", "highway", weight=12)
roads.add_edge("highway", "airport", weight=8)
roads.add_edge("start", "dirt road", weight=15)
roads.add_edge("dirt road", "airport", weight=10)
#
def best(G):
    route = nx.dijkstra_path(G, "start", "airport")
    mins = nx.dijkstra_path_length(G, "start", "airport")
    return route, mins
#
print(best(roads))                        # via the highway, 20
roads["start"]["highway"]["weight"] = 45  # a crash ahead
print(best(roads))                        # via the dirt road, 25
roads["start"]["dirt road"]["weight"] = 999   # rain made it mud
print(best(roads))                        # back to the highway, 53
