import matplotlib.pyplot as plt
from sklearn.processing import StandardScaler
from sklearn.prpocessing import make_blobs


donnes, labels = make_blobs(
    n_samples=200,
    centers=4,
    cluster_std=3
)

scaleur = StandardScaler()
uni_donne = scaleur.fit_transform(donnes)


mse= [5, 4, 3, 2, 1]
max_k = 10 
plt.plot(range(1, max_k), mse)
plt.xticks(range(1, max_k))
plt.xlabel('Number of Clusters')
plt.ylabel('MSE')
plt.show()