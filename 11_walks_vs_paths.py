import numpy as np
import networkx as nx
#
chat = nx.Graph([("A", "B"), ("A", "C"), ("B", "C"),
                 ("B", "D"), ("C", "D"), ("D", "E")])
order = ["A", "B", "C", "D", "E"]       # fix the row order myself
A = nx.to_numpy_array(chat, nodelist=order, dtype=int)
print(A)
print("row sums = degrees:", A.sum(axis=1))
print("symmetric:", (A == A.T).all())
#
# A @ A counts two-step walks; entry [i, j] is walks from i to j
A2 = A @ A
print(A2)
print("two-step walks A to D:", A2[0, 3])   # 2, via B and via C
print("diagonal:", np.diag(A2))             # equals the degrees
#
# walks can revisit nodes, paths cannot; compare on a real network
K = nx.karate_club_graph()
M = nx.to_numpy_array(K, nodelist=sorted(K), dtype=np.int64,
                      weight=None)          # ignore stored weights
for k in range(2, 7):
    walks = np.linalg.matrix_power(M, k)[0, 33]
    paths = sum(1 for p in nx.all_simple_paths(K, 0, 33, cutoff=k)
                if len(p) - 1 == k)
    print(k, walks, paths)
