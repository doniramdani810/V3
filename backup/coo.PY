import pyautogui
import time

image_list = ['1.bmp', '2.bmp', '3.bmp', '4.bmp', '5.bmp', '6.bmp', '7.bmp', '8.bmp', '9.bmp', '10.bmp', '11.bmp', '12.bmp', '13.bmp', '14.bmp', '15.bmp', '16.bmp', '17.bmp', '18.bmp', '19.bmp', '20.bmp', '21.bmp', '22.bmp', '23.bmp', '24.bmp', '25.bmp', '26.bmp', '27.bmp', '28.bmp', '29.bmp', '30.bmp']

while True:
    for image_name in image_list:
        # Mencari gambar
        image = pyautogui.locateOnScreen(image_name, confidence = 0.8)

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
