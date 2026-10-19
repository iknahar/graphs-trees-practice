# Graphs, Trees and DAGs: Practice Code

Small, runnable Python scripts for learning the shapes data science leans on: graphs, adjacency matrices, trees, decision trees, directed acyclic graphs (DAGs), Bayesian networks, causal diagrams, breadth first search and Dijkstra's shortest route.

Each example comes from something already on your phone: a group chat, Instagram follows, Google Maps, Akinator, a spreadsheet, a phone that won't charge, and "People You May Know". Every script runs on its own, prints its results and finishes in a second or two.

## Setup

```bash
python -m pip install -r requirements.txt
```

Python 3.9 or newer (script 07 uses `graphlib`, which arrived in 3.9).

## The scripts

| File | What it shows |
|---|---|
| `01_build_a_graph.py` | a group chat as a graph, friend counts (degree), the handshake rule, directed and weighted graphs |
| `02_paths_cycles_connectivity.py` | paths, cycles, bridges, connected pieces, and the old Konigsberg bridges puzzle |
| `03_maps_mud_detour.py` | a crash and a muddy dirt road changing the fastest route to the airport |
| `04_friendship_paradox.py` | why your friends have more friends than you, on Zachary's karate club |
| `05_trees.py` | n nodes and n - 1 edges, depth, leaves, and what one extra edge does |
| `06_decision_tree.py` | a two-question decision tree sorting 150 iris flowers |
| `07_topological_sort.py` | a safe course order, a spreadsheet loop caught by `graphlib`, and Kahn's method by hand |
| `08_bayes_charger.py` | a phone that won't charge, a bad cable or a dead socket, and "explaining away" |
| `09_ice_cream_sharks.py` | heat as the hidden cause behind ice cream sales and shark sightings |
| `10_people_you_may_know.py` | ranking strangers by mutual friends with `A @ A` |
| `11_walks_vs_paths.py` | the adjacency matrix, two-step walks, and walks against paths on a real network |
| `12_bfs_and_dijkstra.py` | breadth first search and Dijkstra, written from scratch |

## Exercises

Try each one before opening the answer.

**1. Handshake check.** Add the friendship `("A", "E")` in `01_build_a_graph.py`. What is the new total of friend counts, and why must it still be even?

<details><summary>Answer</summary>

14. One new friendship adds 1 to A's count and 1 to E's count, so the total grows by 2. A total of the form 2 × friendships is always even, which also means a graph can never have an odd number of people with an odd friend count.
</details>

**2. Another bad road.** In `03_maps_mud_detour.py`, keep the crash (`45`) but change the dirt road's second stretch, `("dirt road", "airport")`, from 10 to 30 minutes. Which route wins now, and how long does it take?

<details><summary>Answer</summary>

The dirt road still wins, at 15 + 30 = 45 minutes, because the highway now costs 45 + 8 = 53. Change any single number and Dijkstra re-checks every route for you.
</details>

**3. Paradox on your own network.** Build a small graph of your own friends (eight people is plenty) and run the two averages from `04_friendship_paradox.py` on it. Does the paradox hold?

<details><summary>Answer</summary>

It holds on average in almost any network where friend counts differ. It only fails when everyone has exactly the same number of friends, because then nobody extra-popular is around to pull the average up.
</details>

**4. Count the edges.** A tree has 40 nodes. How many edges does it have? If someone shows you a connected graph with 40 nodes and 40 edges, what must it contain?

<details><summary>Answer</summary>

39 edges. A connected graph with 40 nodes and 40 edges has exactly one loop, because it has one edge more than a tree.
</details>

**5. Deeper tree.** Change `max_depth=2` to `max_depth=4` in `06_decision_tree.py`. What happens to training accuracy and the number of leaves? Why is that not automatically good news?

<details><summary>Answer</summary>

Accuracy rises to about 0.99 and the number of leaves grows. A deeper tree can memorise odd training flowers, so it may do worse on flowers it has never seen. Always test on held-out data before celebrating.
</details>

**6. Break the order.** In `07_topological_sort.py`, add `"Algebra": {"ML"}` to the `needs` dictionary. What happens?

<details><summary>Answer</summary>

`TopologicalSorter` raises `CycleError`. Algebra now waits on ML, which waits on Statistics, which leads back to Algebra, so no course in that loop can ever go first.
</details>

**7. Explaining away.** In `08_bayes_charger.py`, change the socket's starting chance from 0.05 to 0.30. Recompute all three numbers. Does proving the socket is dead still clear the cable?

<details><summary>Answer</summary>

Yes. After the phone fails, the cable sits at about 0.44 and the socket at about 0.68. Once the socket is proven dead, the cable drops back to about 0.20, its starting value, because the socket fully explains the dead phone.
</details>

**8. A new suggestion.** In `10_people_you_may_know.py`, make you friends with G by adding `("You", "G")`. Who is suggested now, and with how many mutual friends?

<details><summary>Answer</summary>

E with 3, F with 2 and H with 1. G disappears from the list because G is now your friend, and H gains a mutual friend through G.
</details>

**9. Walks or paths.** In `11_walks_vs_paths.py`, compute `A @ A @ A` for the group chat. The entry for A to A is 2. List those two walks by hand. Are they paths?

<details><summary>Answer</summary>

A, B, C, A and A, C, B, A. They are loops of length 3 (triangles). A walk that comes back home is never a path, because a path may not repeat a node.
</details>

## Data

- Zachary's karate club network ships with `networkx` (34 members, 78 friendships, recorded in the 1970s).
- The iris flowers ship with `scikit-learn`.
- The ice cream and shark numbers in script 09 are simulated on purpose, so the hidden cause is known.

## License

MIT, see `LICENSE`.
