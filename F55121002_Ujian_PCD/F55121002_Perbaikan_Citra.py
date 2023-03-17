import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# fungsi untuk memperbaiki citra dengan metode peningkatan kecerahan
def brightness_correction(img):
    brightness = 50
    corrected_img = cv2.add(img, brightness)
    return corrected_img

# fungsi untuk memperbaiki citra dengan metode smoothing
def smoothing_correction(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    smoothed_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return smoothed_img

def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_img = cv2.filter2D(img, -1, kernel)
    return sharpened_img

def noise_reduction(img):
    denoised_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    return denoised_img


# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'brightness':
        corrected_img = brightness_correction(original_img)
        show_image(corrected_img, 350, 120, 'Perbaikan Metode 1')
    elif method == 'smoothing':
        corrected_img = smoothing_correction(original_img)
        show_image(corrected_img, 650, 120, 'Perbaikan Metode 2')
    elif method == 'sharpening':
        corrected_img = sharpening(original_img)
        show_image(corrected_img, 350, 450, 'Perbaikan Metode 3')
    elif method == 'noise':
        corrected_img = noise_reduction(original_img)
        show_image(corrected_img, 650, 450, 'Perbaikan Metode 4')

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Vidya Az Zahra    NIM : F55121002    Kelas : A')
    creator_label.place(x=1000, y=50)

# fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        show_image(original_img, 50, 120, 'Gambar Original')
        size_label.config(text='Dimensi : {} x {}'.format(original_img.shape[1], original_img.shape[0]))

# membuat jendela utama
root = tk.Tk()
root.geometry('1400x1000')
root.title('GUI Aplikasi Penerapan Perbaikan Citra')

# menambahkan judul gambar original
title_label = tk.Label(root, text='Gambar Original')
title_label.place(x=50, y=20)

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Buka Gambar', command=open_image)
open_button.place(x=50, y=50)

# menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(root, text='Dimensi : -')
size_label.place(x=150, y=50)

# menambahkan kotak untuk perbaikan citra
correction_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=350, y=20, width=500, height=70)

# tombol untuk perbaikan metode 1 (peningkatan kecerahan)
brightness_button = tk.Button(correction_box, text='Peningkatan Kecerahan', command=lambda: process_image('brightness'))
brightness_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 2 (smoothing)
smoothing_button = tk.Button(correction_box, text='Penghalusan', command=lambda: process_image('smoothing'))
smoothing_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 3 (sharpening)
sharpening_button = tk.Button(correction_box, text='Penajaman', command=lambda: process_image('sharpening'))
sharpening_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode 3 (sharpening)
denoised_button = tk.Button(correction_box, text='Pengurangan Noise', command=lambda: process_image('noise'))
denoised_button.pack(side=tk.LEFT, padx=5)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Creator', padx=5, pady=5)
creator_box.place(x=950, y=20, width=400, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan program
root.mainloop()

