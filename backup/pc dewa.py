import pywinauto
import pyautogui
import keyboard
import threading
import logging
import sys
import time
import os
import glob
from threading import Thread

logging.basicConfig(level=logging.DEBUG, filename='myapp.log', filemode='w')

# Function to handle an error and log it to the file
def handle_error(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_error

# function to handle the first task
def koding1():
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
                time.sleep(0)
                break
        else:
            time.sleep(0)

def koding2():

    image_list = ['1CLICK.bmp', '1CLICKV1.bmp', '1CLICKV2.bmp', '1CLICKV3.bmp', '1CLICKV4.png', '1CLICKV5.png']

    while True:
        for image_name in image_list:            # Mencari gambar
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
            time.sleep(0)

def koding3():
    wait_time = 2
    while True:
        try:
            # Menentukan gambar yang dicari
            image = 'gambar1.png'

            # Mencari gambar di layar
            location = pyautogui.locateCenterOnScreen(image, confidence=0.7)

            # Jika gambar ditemukan
            if location:
                # Menentukan gambar yang akan diklik
                image2 = 'silang.bmp'
                # Mencari gambar di layar
                region = (location[0]-200, location[1]-100, location[0]+200, location[1]+100)
                location = pyautogui.locateOnScreen(image2, region=region, grayscale=False, confidence=0.7)
                # Jika gambar ditemukan
                if location:
                    # Mengklik gambar yang ditentukan
                    pyautogui.click(location)
                    logging.info("Gambar ditemukan, ulangi dari awal.")
                    continue
            else:
                logging.info("Gambar 1 tidak ditemukan.")
                time.sleep(wait_time)
                continue
        except pyautogui.ImageNotFoundException as e:
            logging.error(f"Error {e}")
            time.sleep(wait_time)
            continue


def koding4():
        def find_cross_image():
            image_path = r"C:\Users\Doni\Desktop\CROT\silang.bmp"
            current_position = pyautogui.position()
            image_location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)
            if image_location:
                print("Gambar ditemukan di koordinat: ", image_location)
                pyautogui.moveTo(image_location)
                pyautogui.click()
            else:
                print("Gambar tidak ditemukan.")

        def find_box_text_image():
            image_path = r"C:\Users\Doni\Desktop\CROT\box_text.png"
            image_location = pyautogui.locateOnScreen(image_path)
            if image_location:
                print("Gambar ditemukan di koordinat: ", image_location)
                pyautogui.moveTo(image_location)
                pyautogui.click()
            else:
                print("Gambar tidak ditemukan.")

        keyboard.add_hotkey('esc', find_cross_image)
        keyboard.add_hotkey('tab', find_box_text_image)

        print("Tekan esc untuk mencari gambar silang.")
        print("Tekan tab untuk mencari gambar text.")
        keyboard.wait()


def koding5():
    folder_path = r'C:\Users\Doni\Desktop\CROT\Badaklabalaba'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)

def koding6():
    folder_path = r'C:\Users\Doni\Desktop\CROT\dadu'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)

def koding7():
    folder_path = r'C:\Users\Doni\Desktop\CROT\Gambar'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)

def koding8():
    folder_path = r'C:\Users\Doni\Desktop\CROT\Kodok'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)

def koding9():
    folder_path = r'C:\Users\Doni\Desktop\CROT\Kotak'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)


def koding10():
    folder_path = r'C:\Users\Doni\Desktop\CROT\Pinguin'
    image_list = []

    for file in os.listdir(folder_path):
            if file.endswith('.png'):
                image_list.append(os.path.join(folder_path, file))

    while True:
            for image_name in image_list:
                image = pyautogui.locateOnScreen(image_name, confidence = 0.7)
                if image:
                    x, y = pyautogui.center(image)
                    pyautogui.click(x, y)
                    print("Gambar " + image_name + " ditemukan dan diklik")
                    break
            else:
                time.sleep(0)



if __name__ == "__main__":
    t1 = threading.Thread(target=koding1)
    t2 = threading.Thread(target=koding2)
    t3 = threading.Thread(target=koding3)
    t4 = threading.Thread(target=koding4)
    t5 = threading.Thread(target=koding5)
    t6 = threading.Thread(target=koding6)
    t7 = threading.Thread(target=koding7)
    t8 = threading.Thread(target=koding8)
    t9 = threading.Thread(target=koding9)
    t10 = threading.Thread(target=koding10)
    

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()

