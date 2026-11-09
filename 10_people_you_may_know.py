import networkx as nx
#
G = nx.Graph([("You", "B"), ("You", "C"), ("You", "D"),
              ("B", "E"), ("C", "E"), ("D", "E"),
              ("C", "F"), ("D", "F"), ("D", "G"), ("G", "H")])
people = sorted(G)
A = nx.to_numpy_array(G, nodelist=people, dtype=int)
mutual = A @ A                    # squaring the table = mutual friends
#
me = people.index("You")
for i, p in enumerate(people):
    if p != "You" and A[me, i] == 0:          # skip me and my friends
        print(p, mutual[me, i])               # E 3, F 2, G 1, H 0
#
# the same thing as a ranked list, most mutual friends first
scores = {p: int(mutual[me, i]) for i, p in enumerate(people)
          if p != "You" and A[me, i] == 0}
print(sorted(scores.items(), key=lambda kv: -kv[1]))
#
# the diagonal of A @ A is each person's friend count
print({p: int(mutual[i, i]) for i, p in enumerate(people)})
