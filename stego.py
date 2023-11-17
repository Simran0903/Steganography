import cv2
import os
from tkinter import *

# two dictionaries, one for storing ascii values and one for storing
d = {}
c = {}
img = None  # Initialize img as a global variable

def encrypt_image():
    global img
    for i in range(255):
        d[chr(i)] = i  # character to ASCII
        c[i] = chr(i)  # ASCII to character

    image_path = r"C:\Users\simra\OneDrive\Desktop\Steganography\flower.jpg"
    img = cv2.imread(image_path)

    key = key_entry.get()
    text = text_entry.get()

    kl = 0
    z = 0  # decides planes
    n = 0  # number of columns
    m = 0  # number of rows

    for i in range(len(text)):
        img[n, m, z] = d[text[i]] ^ d[key[kl]]
        n += 1
        m += 1
        m = (m + 1) % 3
        kl = (kl + 1) % len(key)

    cv2.imwrite("encryptedimg.jpg", img)
    os.startfile("encryptedimg.jpg")
    result_label.config(text="Data is successfully hidden in Image.")
def decrypt_image():
    global c, img  # Use the global c and img variables

    key = key_entry.get()
    kl = 0
    z = 0
    n = 0
    m = 0

    decrypt = ""
    text = text_entry.get()
    for i in range(len(text)):
        decrypt += c[img[n, m, z] ^ d[key[kl]]]
        n += 1
        m += 1
        m = (m + 1) % 3
        kl = (kl + 1) % len(key)

    result_label.config(text=f"Encrypted text was: {decrypt}")

root = Tk()
root.title("Steganography")

# Entry and label for key
key_label = Label(root, text="Enter key (Security key):")
key_label.grid(row=0, column=0, padx=10, pady=10)
key_entry = Entry(root, show="*")
key_entry.grid(row=0, column=1, padx=10, pady=10)

# Entry and label for text
text_label = Label(root, text="Enter text to hide:")
text_label.grid(row=1, column=0, padx=10, pady=10)
text_entry = Entry(root)
text_entry.grid(row=1, column=1, padx=10, pady=10)

# Buttons for Encrypt and Decrypt
encrypt_button = Button(root, text="Encrypt", command=encrypt_image)
encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

decrypt_button = Button(root, text="Decrypt", command=decrypt_image)
decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display result
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
