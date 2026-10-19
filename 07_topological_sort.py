from collections import deque
from graphlib import TopologicalSorter, CycleError
#
# an arrow a -> b means "take a before b"
pre = {"Algebra": ["Calculus"], "Calculus": ["Probability"],
       "Probability": ["Statistics"], "Statistics": ["ML"],
       "Python": ["ML"], "ML": []}
#
def kahn(graph):
    indeg = {v: 0 for v in graph}
    for v in graph:
        for w in graph[v]:
            indeg[w] += 1                # count unmet prerequisites
    ready = deque(v for v in graph if indeg[v] == 0)
    order = []
    while ready:
        v = ready.popleft()              # anything with nothing pending
        order.append(v)
        for w in graph[v]:
            indeg[w] -= 1                # v is done, w waits on one less
            if indeg[w] == 0:
                ready.append(w)
    if len(order) < len(graph):
        raise ValueError("cycle: some nodes never reached zero")
    return order
#
print(kahn(pre))
#
# the standard library does the same job (it wants predecessors)
before = {"A1": {"C1", "D1"}, "B1": {"A1"}, "C1": {"B1"}, "D1": set()}
try:
    print(list(TopologicalSorter(before).static_order()))
except CycleError as e:
    print("CycleError:", e.args[1])      # the loop it found
