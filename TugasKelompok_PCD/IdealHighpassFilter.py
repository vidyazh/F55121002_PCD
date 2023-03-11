import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra
img = cv2.imread('gambar.png', 0)

# Menghitung DFT
dft = np.fft.fft2(img)

# Menggeser nol frekuensi ke tengah
dft_shift = np.fft.fftshift(dft)

# Menentukan radius cutoff
radius = 50

# Membuat filter ideal highpass
rows, cols = img.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows, cols), np.uint8)
mask[crow-radius:crow+radius, ccol-radius:ccol+radius] = 1
mask = 1 - mask

# Mengalikan filter dengan spektrum frekuensi
dft_shift_filtered = dft_shift * mask

# Menggeser nol frekuensi kembali ke sudut kiri atas
dft_filtered = np.fft.ifftshift(dft_shift_filtered)

# Menghitung citra hasil filter dengan IDFT
img_filtered = np.fft.ifft2(dft_filtered)
img_filtered = np.abs(img_filtered)

# Menampilkan hasil
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_filtered, cmap='gray')
plt.title('Highpass Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
