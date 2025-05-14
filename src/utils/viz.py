import matplotlib.pyplot as plt

def plot_clusters(centroid_history):
    for t, cents in enumerate(centroid_history):
        plt.scatter(cents[:,0], cents[:,1], label=f"t={t}")
    plt.legend(); plt.xlabel("feat_1"); plt.ylabel("feat_2")
    plt.show()
