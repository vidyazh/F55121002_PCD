import cv2
import numpy as np

# Membaca citra
img = cv2.imread('gambar.png')

# Menerapkan filter Gaussian blur
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Menghitung perbedaan citra dengan filter Gaussian blur
diff = cv2.subtract(img, blur)

# Menambahkan citra asli dengan hasil perbedaan yang telah dilipatgandakan
unsharp_mask = cv2.addWeighted(img, 1.5, diff, 0.5, 0)

# Menampilkan hasil
cv2.imshow('Unsharp Masking Filter', unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
