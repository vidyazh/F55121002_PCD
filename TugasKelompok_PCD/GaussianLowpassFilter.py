import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra
img = cv2.imread('gambar.png', 0)

# Menentukan ukuran filter dan sigma
ksize = 25
sigma = 5

# Membuat kernel Gaussian
kernel = cv2.getGaussianKernel(ksize, sigma)

# Menghitung filter 2D dengan kernel Gaussian
kernel_2d = np.outer(kernel, kernel.transpose())
filtered_img = cv2.filter2D(img, -1, kernel_2d)

# Menampilkan hasil
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(filtered_img, cmap='gray')
plt.title('Gaussian Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
