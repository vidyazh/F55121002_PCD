import cv2
import numpy as np

# Membaca citra
img = cv2.imread('gambar.png', 0)

# Konversi citra ke dalam float32
f = np.float32(img)

# Menghitung transformasi Fourier
dft = cv2.dft(f, flags=cv2.DFT_COMPLEX_OUTPUT)

# Menggeser frekuensi nol ke tengah
dft_shift = np.fft.fftshift(dft)

# Menerapkan filter Laplacian pada domain frekuensi
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.float32)
mask[crow - 30: crow + 30, ccol - 30: ccol + 30] = 1
dft_shift_filtered = dft_shift * mask

# Mengembalikan frekuensi nol ke posisi semula
dft_filtered = np.fft.ifftshift(dft_shift_filtered)

# Menghitung inversi transformasi Fourier
img_back = cv2.idft(dft_filtered)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Menampilkan hasil
cv2.imshow('Laplacian Filter (Frequency Domain)', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
