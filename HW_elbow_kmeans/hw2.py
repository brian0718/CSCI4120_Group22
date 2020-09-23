import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from scipy.stats import mode
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import confusion_matrix
from yellowbrick.cluster import KElbowVisualizer

X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

# TODO determine the best k for k-means
visualizer = KElbowVisualizer(KMeans(), k=(2, 10))
visualizer.fit(X)
visualizer.show()


# TODO calculate accuracy for best K
best_k = visualizer.elbow_value_
kmeans = KMeans(n_clusters=best_k)
labels = kmeans.fit_predict(X)

#make the labels predicted from KMeans match y_true from make_blobs
predictions = np.zeros_like(labels)
for i in range(best_k):
    mask=(labels==i)
    predictions[mask]=mode(y_true[mask])[0]


accuracy = accuracy_score(y_true, predictions)
print("Accuracy Score = ", accuracy*100, "%")

# TODO draw a confusion matrix
mat = confusion_matrix(y_true, predictions)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.show()