print('Be patient, loading UMAP is kind of slow...')
import numpy as np
import pandas as pd
import seaborn as sns
import tkinter as tk
from sklearn.datasets import load_digits, load_iris
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import umap
from utils import hopkins, scale, average_hopkins

# Global Params
alpha = 0.05 # Hopkins hypothesis alpha level

def iris_analysis():
    iris = load_iris()

    # Setup the group variable, visualize the distributions pairwise
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    nTargets = len(iris.target_names)
    iris_df['species'] = pd.Series(iris.target).map(dict(zip(range(nTargets),iris.target_names)))
    sns.pairplot(iris_df, hue='species')

    # Check if clustering makes sense with hopkins, values close to 1 mean clusters likely exist
    H = hopkins(iris.data, alpha=alpha)
    print(f'The Hopkins Stat for Iris is {H}.')

    # Umap on Iris
    umap_instance = umap.UMAP()
    umap_fit = umap_instance.fit_transform(iris.data)

    # TSNE on Iris
    tsne_instance = TSNE(n_components=2, perplexity=50)
    tsne_fit = tsne_instance.fit_transform(iris.data)

    # Check our 2D projections for clusters
    H_umap = hopkins(umap_fit)
    H_tsne = hopkins(tsne_fit)
    print('After projecting...')
    print(f'UMAP: {H_umap}, TSNE: {H_tsne}')

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Iris Data')
    for sTarget in iris.target_names:
        bKeep = (iris_df.species == sTarget).values
        H_umap = hopkins(umap_fit[bKeep])
        H_tsne = hopkins(tsne_fit[bKeep])
        print(f'{sTarget} species Hopkins statistics')
        print(f'UMAP: {H_umap}, TSNE: {H_tsne}')

        axs[0].scatter(umap_fit[bKeep, 0], umap_fit[bKeep, 1], label=sTarget)
        axs[0].set_aspect('equal', 'datalim')
        axs[0].set_title('UMAP', fontsize=16)

        axs[1].scatter(tsne_fit[bKeep, 0], tsne_fit[bKeep, 1], label=sTarget)
        axs[1].set_aspect('equal', 'datalim')
        axs[1].set_title('TSNE', fontsize=16)

    for ax in axs:
        ax.legend()
    plt.show(block = False)
    print('********************************************************************************************')

def digits_analysis():
    digits = load_digits()

    # Setup the group variable, visualize the distributions pairwise
    digits_df = pd.DataFrame(digits.data, columns=digits.feature_names)
    nTargets = len(digits.target_names)
    digits_df['number'] = pd.Series(digits.target).map(dict(zip(range(nTargets),digits.target_names)))
    avg_pixel_val = digits_df.groupby('number').mean()

    divisions = np.arange(0, 64, 8)[1:]
    xlabels = np.tile(np.arange(0,8), 8)
    fig, axs = plt.subplots(5, 2, sharex=True, sharey=True)
    fig.suptitle('Unrolled average pixel intensity for 8x8 numbers')
    for (number, vals), ax in zip(avg_pixel_val.iterrows(), axs.flatten()):
        ax.plot(vals)
        for x in divisions:
            ax.axvline(x, c='k')
        ax.set_title(number)
        ax.set_xticklabels(xlabels)

    # Check if clustering makes sense with hopkins, values close to 1 mean clusters likely exist
    H = hopkins(digits.data)
    print(f'The Hopkins Stat for Digits is {H}.')

    # Umap Vs TSNE on Digits
    reducer = umap.UMAP(random_state=42)
    reducer.fit(digits.data)
    umap_fit = reducer.transform(digits.data)

    tsne_instance = TSNE(n_components=2, perplexity=50)
    tsne_fit = tsne_instance.fit_transform(digits.data)

    # Check our 2D projections for clusters
    H_umap = hopkins(umap_fit)
    H_tsne = hopkins(tsne_fit)
    print('After projecting...')
    print(f'UMAP: {H_umap}, TSNE: {H_tsne}')

    
    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Digits Data')
    for sTarget in digits.target_names:
        bKeep = (digits_df.number == sTarget).values
        H_umap = hopkins(umap_fit[bKeep])
        H_tsne = hopkins(tsne_fit[bKeep])
        print(f'Number {sTarget} Hopkins statistics')
        print(f'UMAP: {H_umap}, TSNE: {H_tsne}')

        axs[0].scatter(umap_fit[bKeep, 0], umap_fit[bKeep, 1], label=sTarget, cmap='Spectral', s=5)
        axs[0].set_title('UMAP', fontsize=16)

        axs[1].scatter(tsne_fit[bKeep, 0], tsne_fit[bKeep, 1], label=sTarget, s=5)
        axs[1].set_title('TSNE', fontsize=16)

    for ax in axs:
        ax.legend(ncol=2)
    plt.show(block = False)
    print('********************************************************************************************')

def kill_plots():
    plt.close('all')

def kill_window():
    plt.close('all')
    quit()

if __name__ == '__main__':
    # Setup popup dialogs
    root = tk.Tk()
    root.title('Hopkins Analyses')
    root.geometry('300x150')

    tk.Button(root, text='Run Iris Analysis', command=iris_analysis).grid(row=0, column=0, sticky=tk.W)
    tk.Button(root, text='Run Digits Analysis', command=digits_analysis).grid(row=0, column=1, sticky=tk.E)
    tk.Button(root, text='Close all plots', command=kill_plots).grid(row=1,column=0, sticky=tk.W)
    tk.Button(root, text='Quit...', command=kill_window).grid(row=2,column=0, sticky=tk.W)

    root.mainloop()