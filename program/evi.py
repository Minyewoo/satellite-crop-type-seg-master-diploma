def compute_evi(sentinel2_image):
    band_2 = sentinel2_image[1]
    band_4 = sentinel2_image[3]
    band_8 = sentinel2_image[7]

    return 2.5 * (band_8 - band_4) / (band_8 + 6. * band_4 - 7.5 * band_2 + 1.)