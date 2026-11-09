import networkx as nx
#
# a graph is just a list of who-is-linked-to-whom pairs
chat = nx.Graph([("A", "B"), ("A", "C"), ("B", "C"),
                 ("B", "D"), ("C", "D"), ("D", "E")])
#
print(dict(chat.degree()))     # {'A': 2, 'B': 3, 'C': 3, 'D': 3, 'E': 1}
print(sum(d for _, d in chat.degree()), 2 * chat.number_of_edges())
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
