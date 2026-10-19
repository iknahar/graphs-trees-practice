import networkx as nx
#
# five people in a group chat, each pair is one friendship
chat = nx.Graph()
chat.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"),
                     ("B", "D"), ("C", "D"), ("D", "E")])
#
print("vertices:", chat.number_of_nodes())   # 5
print("edges:", chat.number_of_edges())      # 6
print("degrees:", dict(chat.degree()))       # how many friends each
#
# the handshake lemma: every edge has two ends, so it is counted twice
total = sum(d for _, d in chat.degree())
print(total, "==", 2 * chat.number_of_edges())   # 12 == 12
#
# directed: following is one way, so A -> B says nothing about B -> A
follows = nx.DiGraph([("A", "B"), ("B", "A"), ("C", "A")])
print("A is followed by", follows.in_degree("A"))   # 2
print("A follows", follows.out_degree("A"))         # 1
#
# weighted: each edge carries a number, here minutes between stops
bus = nx.Graph()
bus.add_edge("home", "library", weight=7)
bus.add_edge("library", "campus", weight=4)
print(bus["home"]["library"]["weight"])   # 7
