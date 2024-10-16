# Astropy

*"The astropy package contains key functionality and common tools needed for performing astronomy and astrophysics with Python. It is at the core of the Astropy Project, which aims to enable the community to develop a robust ecosystem of affiliated packages covering a broad range of needs for astronomical research, data processing, and data analysis."* -- https://docs.astropy.org/en/stable/index.html

### Working with FITS data
*FITS (Flexible Image Transport System) is the data format most widely used within astronomy for transporting, analyzing, and archiving scientific data files. FITS is much more than just another image format (such as JPG or GIF) and is primarily designed to store scientific data sets consisting of multidimensional arrays (images) and 2-dimensional tables organized into rows and columns of information.* -- https://fits.gsfc.nasa.gov/fits_primer.html


**Learning Goals:**
1. Open FITS files and load image data
2. Make a 2D histogram with image data
3. Stack several images into a single image
4. Write image data to a FITS file

Firstly, import the required modules:
```python
from astropy.io import fits
from astropy.utils.data import download_file
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
```

Let's grab an example FITS image from the web:
```python
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
hdu_list = fits.open(image_file)
```
and display the "header" information:
```python
hdu_list.info()

No.    Name      Ver    Type      Cards   Dimensions   Format
  0  PRIMARY       1 PrimaryHDU     161   (891, 893)   int16   
  1  er.mask       1 TableHDU        25   1600R x 4C   [F6.2, F6.2, F6.2, F6.2] 
```

Looking at the actual image data:
```python
image_data = hdu_list[0].data
print(type(image_data))
print(image_data.shape)
hdu_list.close()
```
We find:
```python
<class 'numpy.ndarray'>
(893, 891)
```

Alternatively, we can define the image data more directly (if we're not concerned about viewing/modifying the header information):
```python
image_data = fits.getdata(image_file)
```

Let's now visualise the image:
```python
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/horsehead_fits_image.png" width=500 style="display: block; margin: auto;" />
</div>


