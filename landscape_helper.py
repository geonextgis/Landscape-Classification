# Create a function to check the quality of the images
import numpy as np
from tqdm.auto import tqdm
import rasterio as rio

def check_image_quality(file_paths):

    maximum_value = 0
    minimum_value = 0
    count_of_images_with_nan = 0

    for f in tqdm(file_paths):
        with rio.open(f) as src:
            data = src.read()
            src.close()

            max_value = data.max()
            if max_value > maximum_value:
                maximum_value = max_value

            min_value = data.min()
            if min_value < minimum_value:
                minimum_value = min_value
            
            if np.isnan(data).sum() > 0:
                count_of_images_with_nan += 1

    print("Minimum Pixel Value: ", minimum_value)
    print("Maximum Pixel Value: ", maximum_value)
    print("Count of Images with NaN Values: ", count_of_images_with_nan)
