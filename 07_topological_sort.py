from collections import deque
from graphlib import TopologicalSorter, CycleError
#
# each course maps to the courses you must pass first
needs = {"Calculus": {"Algebra"}, "Probability": {"Calculus"},
         "Statistics": {"Probability"},
         "ML": {"Statistics", "Python"}}
print(list(TopologicalSorter(needs).static_order()))
#
# three spreadsheet cells that all wait on each other
cells = {"A1": {"C1"}, "B1": {"A1"}, "C1": {"B1"}}
try:
    print(list(TopologicalSorter(cells).static_order()))
except CycleError as e:
    print("CycleError:", e.args[1])      # the loop it found
#
# the same idea by hand (Kahn's method); arrows point course -> next
nxt = {"Algebra": ["Calculus"], "Calculus": ["Probability"],
       "Probability": ["Statistics"], "Statistics": ["ML"],
       "Python": ["ML"], "ML": []}
#
def kahn(graph):
    waiting = {v: 0 for v in graph}
    for v in graph:
        for w in graph[v]:
            waiting[w] += 1              # count unmet prerequisites
    ready = deque(v for v in graph if waiting[v] == 0)
    order = []
    while ready:
        v = ready.popleft()              # anything with nothing pending
        order.append(v)
        for w in graph[v]:
            waiting[w] -= 1              # v is done, w waits on one less
            if waiting[w] == 0:
                ready.append(w)
    if len(order) < len(graph):
        raise ValueError("cycle: some nodes never stopped waiting")
    return order
#
print(kahn(nxt))
