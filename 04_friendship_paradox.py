import numpy as np
import networkx as nx
#
# Zachary's karate club, 34 real members, 78 friendships (1977)
K = nx.karate_club_graph()
deg = dict(K.degree())
#
mine = np.array([deg[v] for v in K])
# for each person, the average friend count of their own friends
theirs = np.array([np.mean([deg[u] for u in K[v]]) for v in K])
#
print("my average friend count:", mine.mean().round(2))       # 4.59
print("my friends' average:", theirs.mean().round(2))         # 9.61
print("share with fewer friends than their friends:",
      (mine < theirs).mean().round(2))                         # 0.85
#
# why: a person with d friends shows up in d friend lists,
# so popular people get counted more often than quiet ones
d = mine
print("a random person's friends:", d.mean().round(2))          # 4.59
print("a random friend's friends:", ((d * d).sum() / d.sum()).round(2))
