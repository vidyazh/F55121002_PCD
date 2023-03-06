import cv2  #import modul yang dibutuhkan

img = cv2.imread("mammogram.tif", 0) #baca gambar mammogram

img_1 = 255 - img # ubah gambar jadi negatif

cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyALlWindows()