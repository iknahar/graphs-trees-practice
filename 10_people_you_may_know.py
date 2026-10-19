import numpy as np
import networkx as nx
#
G = nx.Graph([("You", "B"), ("You", "C"), ("You", "D"),
              ("B", "E"), ("C", "E"), ("D", "E"),
              ("C", "F"), ("D", "F"), ("D", "G"), ("G", "H")])
people = sorted(G)                       # a fixed order for the rows
A = nx.to_numpy_array(G, nodelist=people, dtype=int)
mutual = A @ A                           # two-step routes = mutual friends
#
me = people.index("You")
scores = {p: int(mutual[me, i]) for i, p in enumerate(people)
          if p != "You" and A[me, i] == 0}   # skip me and my friends
print(sorted(scores.items(), key=lambda kv: -kv[1]))
#
# the diagonal of A @ A is each person's friend count
print({p: int(d) for p, d in zip(people, np.diag(mutual))})
