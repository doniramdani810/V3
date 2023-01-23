import threading
import pyautogui
from PIL import ImageGrab
import keyboard
import os
import time
import cv2
import numpy as np
import glob
import pytesseract
import mss



def koding1():
    
    path = r"C:\Users\Doni\Desktop\CROT\crot\*.png"
    files = glob.glob(path)

    while True:
        for file in files:
            template = cv2.imread(file, 0)
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Convert the screenshot to grayscale
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

            # Set the similarity level (0-1)
            similarity = 0.7

            # Check if the template is on the screen
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= similarity)

            if len(loc[0]) > 0:
                # Get the center of the first match
                x, y = loc[1][0], loc[0][0]
                w, h = template.shape[1], template.shape[0]
                center = (x + w/2, y + h/2)

                # Click at the center
                original_position = pyautogui.position()
                pyautogui.click(center)
                pyautogui.moveTo(original_position)
                
    
def koding2():

    image_list = ['1CLICK.bmp', '1CLICKV1.bmp', '1CLICKV2.bmp', '1CLICKV3.bmp', '1CLICKV4.png', '1CLICKV5.png']

    while True:
        for image_name in image_list:            # Mencari gambar
            image = pyautogui.locateOnScreen(image_name, confidence = 0.8)

            # Jika gambar ditemukan
            if image:
                x, y = pyautogui.center(image)
                original_position = pyautogui.position()
                pyautogui.click(x, y)
                pyautogui.moveTo(original_position)
                break
        else:
            time.sleep(0)


def koding4():
        def find_cross_image():
            image_path = r"C:\Users\Doni\Desktop\CROT\silang.bmp"
            current_position = pyautogui.position()
            image_location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)
            if image_location:
                pyautogui.moveTo(image_location)
                pyautogui.click()
            else:
                print("t")

        def find_box_text_image():
            image_path = r"C:\Users\Doni\Desktop\CROT\box_text.png"
            image_location = pyautogui.locateOnScreen(image_path)
            if image_location:
                pyautogui.moveTo(image_location)
                pyautogui.click()
            else:
                print("Gambar tidak ditemukan.")

        keyboard.add_hotkey('esc', find_cross_image)
        keyboard.add_hotkey('tab', find_box_text_image)

        print("Tekan esc/tab silang/gambar.")
        keyboard.wait()

def koding3():
    count = 1
    while True:
        if keyboard.is_pressed('-'):  # check whether f1 key is pressed or not
            print("Resetting IP in: ", end="")
            for i in range(5, 0, -1):
                print(i, end=" ")
                time.sleep(5)
            print("\nResetting IP, attempt number: ", count)
            os.system("ipconfig /flushdns") # reset cache DNS
            os.system("netsh interface ip set address name=”Ethernet” source=dhcp")
            os.system("netsh winsock reset") # reset winsock
            os.system("netsh int ip reset") # reset setting IP
            os.system("ping google.com -t") # ping ke google.com
            time.sleep(3600) # delay selama 30 menit (1800 detik)
            count += 1
        else:
            time.sleep(30)  # wait for 5 seconds if f1 is not pressed

def koding5():
    
    path = r"C:\Users\Doni\Desktop\CROT\Kudanil*.png"
    files = glob.glob(path)

    while True:
        for file in files:
            template = cv2.imread(file, 0)
            # Take a screenshot
            screenshot = pyautogui.screenshot()
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Convert the screenshot to grayscale
            gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

            # Set the similarity level (0-1)
            similarity = 0.7

            # Check if the template is on the screen
            result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= similarity)

            if len(loc[0]) > 0:
                # Get the center of the first match
                x, y = loc[1][0], loc[0][0]
                w, h = template.shape[1], template.shape[0]
                center = (x + w/2, y + h/2)

                # Click at the center
                original_position = pyautogui.position()
                pyautogui.click(center)
                pyautogui.moveTo(original_position)




if __name__ == "__main__":
    t1 = threading.Thread(target=koding1)
    t2 = threading.Thread(target=koding2)
    t4 = threading.Thread(target=koding4)
    t3 = threading.Thread(target=koding3)
    t5 = threading.Thread(target=koding5)

    t1.start()
    t2.start()
    t4.start()
    t3.start()
    t5.start()
