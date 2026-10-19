import networkx as nx
#
# two friend circles joined by exactly one friendship, 3 to 5
G = nx.Graph([("1", "2"), ("2", "3"), ("3", "4"), ("4", "1"),
              ("1", "3"), ("3", "5"), ("5", "6"), ("6", "7"),
              ("7", "8"), ("8", "5"), ("5", "7")])
#
print(nx.shortest_path(G, "4", "8"))      # one shortest route
print(nx.is_connected(G))                 # True, one piece
print(nx.cycle_basis(G)[:2])              # a couple of loops
#
# a bridge is an edge whose removal splits the graph
print(list(nx.bridges(G)))                # [('3', '5')]
G.remove_edge("3", "5")
print(nx.number_connected_components(G))  # 2
#
# Konigsberg: an Euler walk needs zero or two odd-degree nodes
K = nx.MultiGraph([("N", "I"), ("N", "I"), ("S", "I"), ("S", "I"),
                   ("I", "E"), ("N", "E"), ("S", "E")])
odd = [v for v, d in K.degree() if d % 2 == 1]
print("odd nodes:", odd)                  # all four of them
print(nx.has_eulerian_path(K))            # False
