import cv2

# Membaca citra
img = cv2.imread('gambar.png')

# Ukuran kernel
ksize = 5

# Median filter
median = cv2.medianBlur(img, ksize)

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Median Filtered Image', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
