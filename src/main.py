# src/main.py

import numpy as np
from river.cluster import KMeans as RiverKMeans
from sklearn.cluster import MiniBatchKMeans

from src.data.stream import stream_batches
from src.features.engineer import extract_features
from src.utils.viz import plot_clusters
from src.config import N_CLUSTERS
import itertools

def run():
    # Instantiate models
    river_kmeans = RiverKMeans(n_clusters=N_CLUSTERS)
    minibatch_kmeans = MiniBatchKMeans(
        n_clusters=N_CLUSTERS,
        batch_size=100,
        random_state=42
    )

    history_centers_river = []
    history_centers_sklearn = []

    for batch in itertools.islice(stream_batches(), 50):
        feats_list = [extract_features(sess) for sess in batch]

        # Train River KMeans (in-place)
        for feats in feats_list:
            river_kmeans.learn_one(feats)

        # Train MiniBatchKMeans on full batch
        X_batch = np.array([list(f.values()) for f in feats_list])
        minibatch_kmeans.partial_fit(X_batch)

        # Record River centroids
        river_centroids = np.array([
            list(center.values())
            for center in river_kmeans.centers.values()
        ])

        history_centers_river.append(river_centroids)

        # Record scikit-learn centroids
        sklearn_centroids = minibatch_kmeans.cluster_centers_
        history_centers_sklearn.append(sklearn_centroids)


    # Plot drift
    plot_clusters(history_centers_river)
    plot_clusters(history_centers_sklearn)

if __name__ == "__main__":
    run()
