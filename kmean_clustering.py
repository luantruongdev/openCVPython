import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

path='Resources/fissure.jpg'

img=cv2.imread(path)

# Reshape X into tensor2D: (width x heigth, n_channels)
X=img.reshape((-1, 3))

# Kmeans clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print('Centers found by scikit-learn:')
print(kmeans.cluster_centers_)
pred_label = kmeans.predict(X)

# Reshape pred_label
X_img = pred_label.reshape(img.shape[:2])


# # Display image clustering
# X_img = X_img.astype(np.uint8)
# cv2.imshow("k-Mean Clustering Image",X_img)
# cv2.waitKey(0)

# Display image clustering
fg, ax = plt.subplots(1, 2, figsize = (8, 4))
for i, image in enumerate([img, X_img]):
  ax[i].imshow(image)
  if i == 0:
    ax[i].set_title('Origin Image')
  else:
    ax[i].set_title('k-Mean clustering Image')

plt.show()





