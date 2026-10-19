# Graphs, Trees and DAGs: Practice Code

Small, runnable Python scripts for learning the discrete structures data science leans on: graphs, adjacency matrices, trees, decision trees, directed acyclic graphs (DAGs), Bayesian networks, causal diagrams, breadth first search and Dijkstra's shortest path.

Each script runs on its own, prints its results, and finishes in a second or two.

## Setup

```bash
python -m pip install -r requirements.txt
```

Python 3.9 or newer (script 07 uses `graphlib`, which arrived in 3.9).

## The scripts

| File | What it shows |
|---|---|
| `01_build_a_graph.py` | undirected, directed and weighted graphs, degree, the handshake lemma |
| `02_paths_cycles_connectivity.py` | paths, cycles, bridges, components, the Konigsberg bridges |
| `03_adjacency_matrix_walks.py` | the adjacency matrix, `A @ A` counting walks, walks against paths |
| `04_friendship_paradox.py` | why your friends have more friends than you, on Zachary's karate club |
| `05_trees.py` | n nodes and n - 1 edges, depth, leaves, what one extra edge does |
| `06_decision_tree.py` | a depth-two decision tree on the iris flowers, printed as a tree |
| `07_topological_sort.py` | Kahn's algorithm by hand, and `graphlib` catching a cycle |
| `08_bayes_network_printer.py` | a three-node Bayesian network and "explaining away" |
| `09_confounder.py` | a hidden common cause making two things look linked |
| `10_bfs_and_dijkstra.py` | breadth first search and Dijkstra, written from scratch |
| `11_dependency_ancestors.py` | which packages break when one at the bottom disappears |

## Exercises

Try each one before opening the answer.

**1. Handshake check.** Add the friendship `("A", "E")` in `01_build_a_graph.py`. What is the new sum of degrees, and why must it still be even?

<details><summary>Answer</summary>

14. One new edge adds 1 to A's degree and 1 to E's degree, so the total grows by 2. Any sum of the form 2 × edges is even, which is also why a graph can never have an odd number of odd-degree nodes.
</details>

**2. Walks or paths.** In `03_adjacency_matrix_walks.py`, compute `A @ A @ A` for the group chat. The entry for A to A is 2. List those two walks by hand. Are they paths?

<details><summary>Answer</summary>

A, B, C, A and A, C, B, A. They are cycles of length 3 (triangles). A walk that comes back home is never a path, because a path may not repeat a node. The diagonal of A³ is twice the number of triangles through that node.
</details>

**3. Paradox on your own network.** Build a small graph of your own friends (eight people is plenty) and run the two averages from `04_friendship_paradox.py` on it. Does the paradox hold?

<details><summary>Answer</summary>

It holds on average in almost any network where friend counts differ. It fails only when everyone has the same number of friends, because then there is nobody extra popular to inflate the average.
</details>

**4. Count the edges.** A tree has 40 nodes. How many edges does it have? If someone shows you a connected graph with 40 nodes and 40 edges, what must it contain?

<details><summary>Answer</summary>

39 edges. A connected graph with 40 nodes and 40 edges has exactly one cycle, since it has one edge more than a tree.
</details>

**5. Deeper tree.** Change `max_depth=2` to `max_depth=4` in `06_decision_tree.py`. What happens to training accuracy and to the number of leaves? Why is that not automatically good news?

<details><summary>Answer</summary>

Accuracy rises (it reaches about 0.99) and the number of leaves grows. Deeper trees can memorise training flowers, including the odd ones, so they may do worse on new flowers. Test on held-out data before celebrating.
</details>

**6. Break the order.** In `07_topological_sort.py`, add `"ML": ["Algebra"]` to the `pre` dictionary. What does `kahn` do now?

<details><summary>Answer</summary>

It raises the cycle error. Algebra now waits on ML, which waits on Statistics, which leads back to Algebra, so no course in that loop ever reaches zero unmet prerequisites. Only Python gets ordered.
</details>

**7. Explaining away.** In `08_bayes_network_printer.py`, change the prior for a bad driver to 0.30. Recompute all three numbers. Does learning that the tray is empty still lower your suspicion of the driver?

<details><summary>Answer</summary>

Yes. After a failure the driver jumps to about 0.79 (it was a likely culprit from the start). Learning that the paper ran out pulls it back to about 0.31, right next to its prior of 0.30. A known cause "explains away" the other one.
</details>

**8. Shortest route.** In `10_bfs_and_dijkstra.py`, change the weight of `("C", "T")` from 3 to 9. What is the new shortest route from S to T and its cost?

<details><summary>Answer</summary>

S, B, D, T costs 1 + 7 + 6 = 14, and S, B, A, C, T now costs 3 + 5 + 9 = 17, so the route switches to go through D with cost 14.
</details>

**9. Blast radius.** In `11_dependency_ancestors.py`, which single package, if deleted, would break the most other packages? Use `nx.ancestors` in a loop.

<details><summary>Answer</summary>

left-pad, with six ancestors. Next comes line helper with four (Babel, React tools, test runner, your app), then Babel with three.
</details>

## Data

- Zachary's karate club network ships with `networkx` (34 members, 78 friendships, recorded in the 1970s).
- The iris flowers ship with `scikit-learn`.
- The ice cream and sunburn numbers in script 09 are simulated, on purpose, so the hidden cause is known.

## License

MIT, see `LICENSE`.
