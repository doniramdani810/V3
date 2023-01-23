import pyautogui
import time

image_list = ['1CLICK.bmp', '1CLICKV1.bmp', '1CLICKV2.bmp', '1CLICKV3.bmp']

while True:
    for image_name in image_list:
        # Mencari gambar
        image = pyautogui.locateOnScreen(image_name, confidence = 0.7)

        # Jika gambar ditemukan
        if image:
            # Mendapatkan posisi gambar
            x, y = pyautogui.center(image)
            # Klik pada posisi gambar
            pyautogui.click(x, y)
            print("Gambar " + image_name + " ditemukan dan diklik")
            break
    else:
        time.sleep(1)
