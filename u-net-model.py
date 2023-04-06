from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

import numpy as np

plt.style.use(astropy_mpl_style)

image_file = get_pkg_data_filename('hst_11924_02_wfc3_uvis_f606w_drz.fits')
fits.info(image_file)

print(type(image_file))

image_data = fits.getdata(image_file, ext=1)
f = fits.open(image_file)
input_image = fits.getdata('hst_11924_02_wfc3_uvis_f606w_drz.fits', ext=0)
plt.figure()
plt.imshow(input_image,cmap='gray')
plt.colorbar()