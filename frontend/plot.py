import io

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

CMAP = mcolors.ListedColormap(["#0f0f14", "#00e664"])


def plot_step(matrix: np.ndarray) -> io.BytesIO:
    rows, cols = matrix.shape
    fig = plt.figure(figsize=(8, 8 * rows / cols), facecolor="none", dpi=150)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(matrix, cmap=CMAP, vmin=0, vmax=1, interpolation="nearest", aspect="auto")
    ax.axis("off")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf
