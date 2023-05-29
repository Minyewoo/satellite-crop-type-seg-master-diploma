import numpy as np

def max_scale(image, max=21412.0):
    return image / max

def std_scale(
    image,
    # metrics, precomputed for bands with indexes [1,4,5] on dataset
    means=[3023.4853225, 3359.01293091, 3806.80140723],
    stds=[3280.42597627, 2844.80353716, 2497.64292712],
):
    scaled_image=np.array(shape=image.shape)
    for band_i in range(scaled_image.shape[-1]):
        scaled_image[..., band_i] = (scaled_image[..., band_i] - means[band_i]) / stds[band_i]
    
    return scaled_image