import cv2
import numpy as np

img = cv2.imread('gambar.png', 0)
rows, cols = img.shape

# 1. Membuat filter lowpass
cutoff_frequency = 30
filter = np.zeros((rows, cols, 2), np.float32)
filter[rows//2-cutoff_frequency:rows//2+cutoff_frequency, cols//2-cutoff_frequency:cols//2+cutoff_frequency] = 1

# 2. Transformasi Fourier dari gambar input
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

# 3. Mengalikan filter dengan DFT
dft_filtered = filter * dft

# 4. Menghitung transformasi invers Fourier
img_filtered = cv2.idft(dft_filtered, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

# 5. Menampilkan hasil output
cv2.imshow("Input Image", img)
cv2.imshow("Filtered Image", img_filtered)
cv2.waitKey(0)
