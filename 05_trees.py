import networkx as nx
#
# build a tree one node at a time, each new node brings one edge
T = nx.Graph()
T.add_node(1)
parent = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 6}
for child, p in parent.items():
    T.add_edge(p, child)
print(T.number_of_nodes(), "nodes,", T.number_of_edges(), "edges")
print("is a tree:", nx.is_tree(T))            # connected, no cycle
#
# root it at node 1: depth is the number of edges down from the root
depth = nx.single_source_shortest_path_length(T, 1)
print("depth:", depth)
leaves = [v for v in T if T.degree(v) == 1 and v != 1]
print("leaves:", leaves)
print("height:", max(depth.values()))
#
# one extra edge and it stops being a tree
T.add_edge(5, 6)
print("still a tree:", nx.is_tree(T))         # False
print("cycle:", nx.find_cycle(T, source=5))
#
# a full binary tree of depth d has 2 ** d leaves
for d in (1, 5, 10, 20):
    print(d, 2 ** d)
