import csv
import numpy as np
import umap
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_digits, load_iris
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits



digits = load_digits()
fig, ax_array = plt.subplots(20, 20)
axes = ax_array.flatten()
for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='gray_r')
plt.setp(axes, xticks=[], yticks=[], frame_on=False)
plt.tight_layout(h_pad=0.5, w_pad=0.01)
plt.show()
digits_df = pd.DataFrame(digits.data[:,100:110])
digits_df['digit'] = pd.Series(digits.target).map(lambda x: 'Digit {}'.format(x))
sns.pairplot(digits_df, hue='digit', palette='Spectral')
embedding = umap.UMAP().fit_transform(digits.data)



# data_path = "C:\\Users\\codyg\\OneDrive\\Desktop\\UMAP_work"
# image_size = 28 # width and length
# no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
# image_pixels = image_size * image_size
# train_data = np.loadtxt(data_path + "mnist_train.csv", 
#                         delimiter=",")
# test_data = np.loadtxt(data_path + "mnist_test.csv", 
#                        delimiter=",") 