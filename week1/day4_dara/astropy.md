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

Focussing on the actual image data:
```python
image_data = hdu_list[0].data
hdu_list.close()
```
We find:
```python
print(type(image_data))
print(image_data.shape)

<class 'numpy.ndarray'>
(893, 891)
```

Alternatively, we can define the image data more directly (if we're not concerned about viewing/modifying the header information):
```python
image_data = fits.getdata(image_file)
```
Looking at some numerical stats:
```python
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

Min: 3759
Max: 22918
Mean: 9831.481676287574
Stdev: 3032.3927542049046
```

Finally, let's visualise the image:
```python
plt.imshow(image_data, cmap='gray')
plt.colorbar()
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/horsehead_fits_image.png" width=500 style="display: block; margin: auto;" />
</div>

Depending on the dynamic range involved, it might be better to visualise things on a different scale (in this case, one that might reduce the effective contrast). To gauge the situation, let's plot a histogram of all the pixels. To do this, we can use the flatten method to first transform the 2D values into a single 1D array:
```python
plt.hist(image_data.flatten(), bins=50)
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/flattened_horsehead_histogram.png" width=500 style="display: block; margin: auto;" />
</div>
From this it is evident that the distribution of pixels is skewed towards the dimmer end. We can enhance the original image if we consider a log scaling:

```python
fig, ax = plt.subplots()
ax.hist(np.log(image_data.flatten()), bins='auto')
xticks = np.array([5000, 7500, 10000, 15000, 22500])
ax.set_xticks(np.log(xticks))
ax.set_xticklabels(xticks)
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/flattened_horsehead_histogram_logscale.png" width=500 style="display: block; margin: auto;" />
</div>
which effectively balances out/normalises the pixel values. Finally, let's view the original image in this logarithmic scale:

```python
plt.imshow(image_data, cmap='gray', norm=LogNorm())
cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/horsehead_fits_image_logscale.png" width=500 style="display: block; margin: auto;" />
</div>

Keeping with the theme of image enhancement, let's look at a more practical example of how this is typically done in Astronomy, through a technique called stacking. Stacking performs a mathematical addition of image pixels in order to improve the overall signal to noise ratio. Switching to a completely new set of observations, let's load in 5 images taken of the M13 globular cluster:
```python
num_m13_images = 5
base_url = 'http://data.astropy.org/tutorials/FITS-images/M13_blue_{0:04d}.fits'
image_list = [download_file(base_url.format(n), cache=True)
              for n in range(1, num_m13_images+1)]
image_concat = [fits.getdata(image) for image in image_list]
```
Next, let's plot each raw image:
```python
fig, ax = plt.subplots(nrows=3, ncols=2)
ax = ax.ravel()
for k in range(len(image_concat)):
    ax[k].imshow(image_concat[k], cmap='gray')
    ax[k].colorbar()
    ax[k].set_title("Image #{}".format(k+1))

fig.delaxes(ax[num_m13_images])
fig.tight_layout()
```

<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/m13_raw_images.png" width=500 style="display: block; margin: auto;" />
</div>

The first thing you'll notice is the differences in overall color scales between the images. This is ultimately something we won't worry about too much here, but keep in mind that image calibration is quite a crucial part of the Astronomical image processing. So, just to demonstrate the idea of stacking, let's perform the image addition in the most straight-forward way:
```python
final_image = np.sum(image_concat, axis=0)
```
Since we won't actually see much of an improvement visually, let's first check the resulting histogram to decide on an appropriate color scale to work with:
```python
plt.hist(final_image.flatten(), bins='auto')
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/histogram_m13_stacked.png" width=500 style="display: block; margin: auto;" />
</div>

Something like the following:
```python
plt.imshow(final_image, cmap='gray', vmin=2e3, vmax=3e3)
plt.colorbar()
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/m13_stacked.png" width=500 style="display: block; margin: auto;" />
</div>

Finally, to end of this subsection, let's write our stacked image out to its own FITS file:
```python
outfile = 'stacked_M13.fits'
hdu = fits.PrimaryHDU(final_image)
hdu.writeto(outfile, overwrite=True)
```

### Fitting models to data

**Learning Goals:**
1. Generate synthetic data (using basic models in astropy.modeling)
2. Use common functions to fit
3. Perform a quick fit to data
4. Plot the model with the data
5. Compare different models and fitters

#### E.g. a straight line 
```python
import numpy as np
import math
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting, polynomial
```

First, let's generate synthetic data, and visualise it:
```python
# define a model for a line
line_orig = models.Linear1D(slope=1.0, intercept=math.pi)
# generate x, y data non-uniformly spaced in x
# add noise to y measurements
npts = 30
rng = np.random.default_rng(5)
x = rng.uniform(0.0, 10.0, npts)
y = line_orig(x)
y_diff = rng.normal(0.0, 2.5, npts)
y_tot = y + y_diff
y_err = np.sqrt(np.abs(y_diff))
plt.errorbar(x,y_tot,y_err,fmt='k.')
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/synthetic_data_straight_line.png" width=500 style="display: block; margin: auto;" />
</div>

Next, we initialise an appropriate fitter and model that we think is best to use:
```python
# initialize a linear fitter
fit = fitting.LinearLSQFitter()
# initialize a linear model
line_init = models.Linear1D()
```

Finally, we can perform our fit to the data, check the resulting model parameters and visualise the result:
```python
# fit the data with the fitter
fitted_line = fit(line_init, x, y_tot,  weights=1.0/y_err)
print(fitted_line)
# plot the model
plt.figure()
plt.errorbar(x,y_tot,y_err,fmt='b.', label='Data')
plt.plot(x, fitted_line(x), 'k-', label='Fitted Model')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
```
```python
Model: Linear1D
Inputs: ('x',)
Outputs: ('y',)
Model set size: 1
Parameters:
          slope           intercept    
    ----------------- -----------------
    1.027343604331532 2.935010008085948
```
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/fit_straight_line.png" width=500 style="display: block; margin: auto;" />
</div>
