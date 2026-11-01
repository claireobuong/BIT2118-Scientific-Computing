import numpy as np

# Mini website with 5 pages. links[i][j] = 1 means page i links to page j.
# Assumptions: damping factor 0.85 (a surfer follows a link 85% of the time
# and jumps to a random page 15% of the time).
pages = ["Home", "News", "Shop", "Blog", "Contact"]
links = np.array([
    [0, 1, 1, 1, 0],   # Home  -> News, Shop, Blog
    [1, 0, 0, 1, 0],   # News  -> Home, Blog
    [1, 0, 0, 0, 1],   # Shop  -> Home, Contact
    [1, 1, 0, 0, 0],   # Blog  -> Home, News
    [1, 0, 1, 0, 0],   # Contact -> Home, Shop
], dtype=float)

d = 0.85
n = len(pages)
P = links / links.sum(axis=1, keepdims=True)        # row-stochastic
G = d * P + (1 - d) * np.ones((n, n)) / n           # Google matrix

values, vectors = np.linalg.eig(G.T)
i = np.argmax(np.real(values))
rank = np.abs(np.real(vectors[:, i]))
rank = rank / rank.sum()

print("Dominant eigenvalue:", round(float(np.real(values[i])), 6))
for name, r in sorted(zip(pages, rank), key=lambda p: -p[1]):
    print(f"{name:8s} {r:.4f}")
print("Scores sum to:", rank.sum().round(6))
