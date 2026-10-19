import networkx as nx
#
# a simplified dependency graph: u -> v means "u needs v to build"
deps = nx.DiGraph([
    ("your app", "React tools"), ("your app", "test runner"),
    ("React tools", "Babel"), ("test runner", "Babel"),
    ("Babel", "line helper"), ("line helper", "left-pad"),
    ("test runner", "reporter"), ("reporter", "left-pad"),
    ("your app", "date lib")])
#
print("is a DAG:", nx.is_directed_acyclic_graph(deps))
#
# everything that can reach left-pad by following arrows breaks with it
print(sorted(nx.ancestors(deps, "left-pad")))
#
# a safe build order installs dependencies before the things using them
print(list(reversed(list(nx.topological_sort(deps)))))
