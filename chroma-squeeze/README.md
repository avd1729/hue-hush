# Chroma Squeeze

This Python module performs K-means clustering on an image to segment it into a specified number of clusters.

## Installation

You can install the module via pip:

```bash
pip install chroma-squeeze
```

## Usage

```python
from chroma-squeeze import cluster_image

# Example usage:
cluster_image('input_image.jpg', num_clusters=5, save_path='clustered_image.jpg')
```

## How it Works

The `cluster_image` function takes an input image, the number of clusters (K) to create, and an optional path to save the resulting clustered image. It applies K-means clustering to the colors in the image, replacing each pixel's color with the nearest cluster center.

## Example

Here's an example of using `cluster_image` function:

```python
cluster_image('input_image.jpg', num_clusters=5, save_path='clustered_image.jpg')
```

This would read the 'input_image.jpg', perform K-means clustering with 5 clusters, and save the resulting clustered image as 'clustered_image.jpg'.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/avd1729/Chroma-Squeeze/blob/main/chroma-squeeze/LICENSE.txt) file for details.

## Credits

- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Pillow](https://python-pillow.org/)

## Author

Aravind.M.S