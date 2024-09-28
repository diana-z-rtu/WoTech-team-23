"""Look at what is Central Limit Theorem and try to prove/ visualize it using NumPy
In probability theory, the central limit theorem (CLT) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution. This holds even if the original variables themselves are not normally distributed.

Proof / Visualization using NumPy:

Taking random samples from different distributions.
Calculating the mean of these samples.
Plotting the distribution of these means to show that they approximate a normal distribution as the sample size increases.
"""
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # import model to use

X, y = make_blobs(n_samples=100000, centers=10, cluster_std=.5)
plt.scatter(X[:,0], X[:,1], c=y, cmap='rainbow', edgecolor='k')

n_clusters=10
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)
cluster_labels = kmeans.predict(X)

plt.figure(figsize=(10,6))
plt.scatter(X[:,0], X[:,1], c=cluster_labels, cmap='rainbow', edgecolor='k')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, c='magenta', marker='*', label='Cluster Centers')
plt.title('KMeans Clustering with Cluster Centers')
plt.legend()
plt.show()


import seaborn as sns

# Analyze cluster centers to demonstrate CLT
cluster_centers = kmeans.cluster_centers_

# Create a histogram of the cluster centers
plt.figure(figsize=(12, 6))

# Plot distribution of the x-coordinates of cluster centers
plt.subplot(1, 2, 1)
sns.histplot(cluster_centers[:, 0], bins=10, kde=True, color='blue')
plt.title('Distribution of Cluster Centers (X Coordinate)')
plt.xlabel('X Coordinate of Cluster Centers')

# Plot distribution of the y-coordinates of cluster centers
plt.subplot(1, 2, 2)
sns.histplot(cluster_centers[:, 1], bins=10, kde=True, color='green')
plt.title('Distribution of Cluster Centers (Y Coordinate)')
plt.xlabel('Y Coordinate of Cluster Centers')

plt.tight_layout()
plt.show()

# Example 2
import numpy as np

population = np.random.exponential(scale=2, size=10000)
num_samples = 1000
sample_size = 1000
sample_means = []

for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# distribution of sample means
plt.figure(figsize=(8, 6))
sns.histplot(sample_means, bins=30, kde=True, color='purple')
plt.title(f"Distribution of Sample Means (n={sample_size}, num_samples={num_samples})")
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.show()









