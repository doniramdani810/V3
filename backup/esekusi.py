import pyautogui
import time

while True:
    try:
        # Menentukan gambar yang dicari
        image = 'gambar1.png'
        image2 = 'gambar3.png'

        # Mencari gambar di layar
        location = pyautogui.locateOnScreen(image, confidence=0.7)

        # Jika gambar ditemukan
        if location:
            # Menentukan posisi x, y dari gambar yang ditemukan
            x, y = location[0], location[1]
            # Menentukan gambar yang akan diklik
            image2 = 'silang.bmp'
            # Mencari gambar di layar
            location2 = pyautogui.locateOnScreen(image2, confidence=0.7)
            # Jika gambar ditemukan
            if location2:
                # Menentukan posisi x, y dari gambar yang ditemukan
                x2, y2 = location2[0], location2[1]
                # Mengklik gambar yang ditentukan
                pyautogui.mouseDown(x2, y2)
                pyautogui.mouseUp(x2, y2)
                print("Gambar ditemukan, ulangi dari awal.")
                continue
            else:
                print("Gambar 2 tidak ditemukan.")
                time.sleep(3)
                continue
        else:
            print("Gambar 1 tidak ditemukan.")
            time.sleep(3)
            continue
    except pyautogui.ImageNotFoundException:
        print("Gambar tidak ditemukan.")
        time.sleep(3)
        continue
