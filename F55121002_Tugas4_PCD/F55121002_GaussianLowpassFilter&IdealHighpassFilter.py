import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca gambar
img = cv2.imread('gambar.png', 0)

# Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Filter Gaussian Lowpass
rows, cols = img.shape
crow, ccol = rows/2, cols/2

# membuat filter lowpass Gaussian 2D dengan deviasi standar 20
D = 20
gaussian_lp = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        gaussian_lp[i,j] = np.exp(-((i-crow)**2+(j-ccol)**2)/(2*D**2))

# terapkan filter
fshift_gaussian = fshift * gaussian_lp
f_ishift_gaussian = np.fft.ifftshift(fshift_gaussian)
img_gaussian = np.fft.ifft2(f_ishift_gaussian)
img_gaussian = np.abs(img_gaussian)

# Filter Ideal Highpass
# membuat filter highpass ideal 2D dengan radius 50
ideal_hp = np.zeros((rows, cols))
D = 50
for i in range(rows):
    for j in range(cols):
        if np.sqrt((i-crow)**2+(j-ccol)**2) > D:
            ideal_hp[i,j] = 1

# terapkan filter
fshift_ideal = fshift * ideal_hp
f_ishift_ideal = np.fft.ifftshift(fshift_ideal)
img_ideal = np.fft.ifft2(f_ishift_ideal)
img_ideal = np.abs(img_ideal)

# tampilkan gambar
plt.subplot(2,2,1),plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(img_gaussian, cmap='gray')
plt.title('Gaussian Lowpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(img_ideal, cmap='gray')
plt.title('Ideal Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()
