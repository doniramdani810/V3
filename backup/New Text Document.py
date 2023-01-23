import pyautogui
import keyboard

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
