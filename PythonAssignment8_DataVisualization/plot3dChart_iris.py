import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn.datasets import load_iris

iris = load_iris()
#print(iris.data)

centers = [[1, 1], [-1, -1], [1, -1]]
X = iris.data
y = iris.target

fig = plt.figure(1, figsize=(10, 8))
plt.clf()
ax = Axes3D(fig, elev=48, azim=134)

pca = decomposition.PCA(n_components=3)
X = pca.fit_transform(X)

for name, label in [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))


y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.rainbow_r)

ax.set_title("Three PCA Directions")

plt.show()
#plt.savefig("irisplot.png", dpi=300)
