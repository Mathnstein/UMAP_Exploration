import numpy as np
import umap
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits, load_iris
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

## Iris Dataset

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['species'] = pd.Series(iris.target).map(dict(zip(range(3),iris.target_names)))

sns.pairplot(iris_df, hue='species')


# Umap on Iris
umap_instance = umap.UMAP()
umap_fit = umap_instance.fit_transform(iris.data)

# TSNE on Iris
tsne_instance = TSNE(n_components=2, perplexity=50)
tsne_fit = tsne_instance.fit_transform(iris.data)

fig, axs = plt.subplots(1, 2)
fig.suptitle('Iris Data')
axs[0].scatter(umap_fit[:, 0], umap_fit[:, 1], c=[sns.color_palette()[x] for x in iris.target])
axs[0].set_aspect('equal', 'datalim')
axs[0].set_title('UMAP', fontsize=16)

axs[1].scatter(tsne_fit[:, 0], tsne_fit[:, 1], c=[sns.color_palette()[x] for x in iris.target])
axs[1].set_aspect('equal', 'datalim')
axs[1].set_title('TSNE', fontsize=16)

## Digits Dataset

digits = load_digits()
fig, ax_array = plt.subplots(20, 20)
axes = ax_array.flatten()
for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='gray_r')
plt.setp(axes, xticks=[], yticks=[], frame_on=False)
plt.tight_layout(h_pad=0.5, w_pad=0.01)

# Umap Vs TSNE on Digits
reducer = umap.UMAP(random_state=42)
reducer.fit(digits.data)
embedding = reducer.transform(digits.data)

tsne_instance = TSNE(n_components=2, perplexity=50)
tsne_fit = tsne_instance.fit_transform(digits.data)
# Verify that the result of calling transform is
# idenitical to accessing the embedding_ attribute
assert(np.all(embedding == reducer.embedding_))
fig, axs = plt.subplots(1, 2)
fig.suptitle('Digits Data')
axs[0].scatter(embedding[:, 0], embedding[:, 1], c=digits.target, cmap='Spectral', s=5)
axs[0].set_title('UMAP', fontsize=16)

axs[1].scatter(tsne_fit[:, 0], tsne_fit[:, 1], c=digits.target, cmap='Spectral', s=5)
# fig.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10), ax=axs[1])
axs[1].set_title('TSNE', fontsize=16)
plt.show()
