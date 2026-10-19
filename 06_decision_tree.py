from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
#
# 150 iris flowers, 4 measurements each, 3 species
X, y = load_iris(return_X_y=True)
names = ["sepal length", "sepal width", "petal length", "petal width"]
#
# max_depth=2 means at most two questions before an answer
clf = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)
print(export_text(clf, feature_names=names))
print("training accuracy:", clf.score(X, y))   # 0.96
#
# the fitted model really is a binary tree you can walk by hand
t = clf.tree_
print("nodes:", t.node_count, "leaves:", clf.get_n_leaves())
print("flowers reaching each node:", t.n_node_samples)
