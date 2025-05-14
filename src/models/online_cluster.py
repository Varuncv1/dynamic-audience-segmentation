# src/models/online_cluster.py

"""
Wrapper for multiple online clustering models.
"""

from river import cluster as river_cluster
# from river.cluster import DenStream  # Uncomment to use DenStream for density-based clustering
from sklearn.cluster import MiniBatchKMeans
import numpy as np


class OnlineClustering:
    """
    Manages multiple online clustering models and trains them incrementally.
    """
    def __init__(self, n_clusters=5, batch_size=100):
        # Initialize River KMeans
        self.models = {
            'river_kmeans': river_cluster.KMeans(n_clusters=n_clusters),
            # 'river_denstream': DenStream(epsilon=0.5, lambda_=0.01),  # River DenStream (commented)
            'sklearn_minibatchkmeans': MiniBatchKMeans(
                n_clusters=5,
                init='random',
                n_init=1,
                batch_size=1,
                random_state=42)
        }

    def partial_fit(self, x):
        """
        Incrementally fit each model on a single observation x (dict of features).
        Returns a dict of cluster assignments per model.
        """
        assignments = {}
        for name, model in self.models.items():
            if hasattr(model, 'learn_one'):
                # River model
                model.learn_one(x)
                assignments[name] = model.predict_one(x)
            else:
                # scikit-learn model expects a 2D array
                X = np.array([list(x.values())])
                model.partial_fit(X)
                assignments[name] = model.predict(X)[0]
        return assignments

    @property
    def centers(self):
        """
        Returns current cluster centers for each model.
        """
        centers = {}
        for name, model in self.models.items():
            if hasattr(model, 'centers'):
                centers[name] = model.centers
            else:
                centers[name] = model.cluster_centers_
        return centers
