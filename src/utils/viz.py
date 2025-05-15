import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def plot_clusters(centroid_history):
    """
    centroid_history: list of arrays or dict-like of shape (n_clusters, n_features)
    """
    for t, cents in enumerate(centroid_history):

        # 1) Normalize to a NumPy array if it's a dict/defaultdict
        if isinstance(cents, dict) or isinstance(cents, defaultdict):
            cents = np.array(list(cents.values()))
        else:
            cents = np.asarray(cents)

        # 2) Force 2D
        if cents.ndim == 1:
            cents = cents.reshape(-1, 1)

        n_clusters, n_features = cents.shape

        # 3) Choose plotting strategy
        if n_features < 2:
            ids = np.arange(n_clusters)      # numeric IDs only
            vals = cents[:, 0]
            plt.scatter(ids, vals, label=f"t={t}")
            plt.xlabel("Cluster ID")
            plt.ylabel("Centroid value (dim 0)")
        else:
            x = cents[:, 0]
            y = cents[:, 1]
            plt.scatter(x, y, label=f"t={t}")
            plt.xlabel("Centroid dim 0")
            plt.ylabel("Centroid dim 1")

    plt.title("Cluster Drift Over Time")
    plt.legend()
    plt.tight_layout()
    plt.show()
