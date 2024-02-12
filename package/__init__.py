import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import PIL


def cluster_image(image_path, num_clusters, save_path=None):
    """
    Perform K-means clustering on an image.

    Args:
    image_path (str): The path to the input image file.
    num_clusters (int): The number of clusters for K-means.
    save_path (str): The path to save the clustered image (default is None).

    """
    # Read the image
    image = np.asarray(PIL.Image.open(image_path))

    # Reshape the image to 2D array of pixels
    X = image.reshape(-1, 3)

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42).fit(X)

    # Get clustered image
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]
    segmented_img = segmented_img.reshape(image.shape)

    # Plot original and clustered images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(segmented_img.astype('uint8'))
    plt.title('Clustered Image ({} clusters)'.format(num_clusters))
    plt.axis('off')

    plt.show()

    # Save the segmented image if save_path is provided
    if save_path:
        segmented_img_pil = PIL.Image.fromarray(segmented_img.astype('uint8'))
        segmented_img_pil.save(save_path)
        print("Segmented image saved as", save_path)
