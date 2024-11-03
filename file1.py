import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import mean_squared_error

# Generate synthetic data for clustering
n_samples = 300
X, y_true = make_blobs(n_samples=n_samples, centers=3, cluster_std=1.0, random_state=42)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Initial Data Points")
plt.show()


# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, init='random', max_iter=300, n_init=1, verbose=1)
kmeans.fit(X)

# Get initial centroids and plot
initial_centroids = kmeans.cluster_centers_
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')
plt.scatter(initial_centroids[:, 0], initial_centroids[:, 1], s=200, c='red', marker='X')
plt.title("K-Means Initial Clusters")
plt.show()

# Final clusters, epochs, and error rate
final_centroids = kmeans.cluster_centers_
iterations = kmeans.n_iter_
mse = mean_squared_error(X, kmeans.cluster_centers_[kmeans.labels_])

# Plot final clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')
plt.scatter(final_centroids[:, 0], final_centroids[:, 1], s=200, c='blue', marker='X')
plt.title("K-Means Final Clusters")
plt.show()

# Display results
print(f"K-Means Final Clusters after {iterations} epochs")
print(f"Mean Squared Error: {mse}")

# Calculate cluster means based on labels
cluster_means = np.array([X[y_hc == i].mean(axis=0) for i in range(3)])

# Map each data point to its respective cluster mean
predicted_X = np.array([cluster_means[label] for label in y_hc])

# Calculate Mean Squared Error
mse_hc = mean_squared_error(X, predicted_X)

# Display results
print("Hierarchical Clustering Final Clusters")
print(f"Mean Squared Error: {mse_hc}")


