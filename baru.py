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
                time.sleep(1)


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
                time.sleep(1)




if __name__ == "__main__":
    t1 = threading.Thread(target=koding1)
    t4 = threading.Thread(target=koding4)
    t5 = threading.Thread(target=koding5)

    t1.start()
    t4.start()
    t5.start()
