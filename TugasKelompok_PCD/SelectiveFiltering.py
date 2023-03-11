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

# Menerapkan filter Gaussian pada domain frekuensi
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.float32)
mask[crow - 30: crow + 30, ccol - 30: ccol + 30] = 1
dft_shift_filtered = dft_shift * mask

# Menghitung spektrum frekuensi citra awal
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))

# Menghitung spektrum frekuensi citra hasil filter
magnitude_spectrum_filtered = 20 * np.log(cv2.magnitude(dft_shift_filtered[:, :, 0], dft_shift_filtered[:, :, 1]) + 1e-9)

# Menghitung inversi transformasi Fourier
img_back = cv2.idft(dft_shift_filtered)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Menampilkan hasil
cv2.imshow('Citra Awal', img)
cv2.imshow('Spektrum Frekuensi Citra Awal', magnitude_spectrum)
cv2.imshow('Spektrum Frekuensi Citra Hasil Filter', magnitude_spectrum_filtered)
cv2.imshow('Citra Hasil Filter', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
