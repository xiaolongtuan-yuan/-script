import pyautogui
import time
import pyperclip
import cv2
import pyperclip


imgxx = cv2.imread('hbxx2.png')
imghb = cv2.imread('hb.png')
# imgshuzhen = cv2.imread('shuzhen.png')
imgk = cv2.imread('kai.png')
imgx = cv2.imread('x.png')

def begin():
    i=0
    # while True:
    #     location2 = pyautogui.locateCenterOnScreen(imghb)
    #     if location2 is not None:
    #         pyautogui.click(location2.x,location2.y,button='left')
    while True:
        location3 = pyautogui.locateCenterOnScreen(imgk)
        if location3 is not None:
            pyautogui.click(location3.x, location3.y, button='left')
            time.sleep(0.5)
            pyautogui.press('esc') # 按下并松开（轻敲）回车键
            pyperclip.copy('谢谢老板！')
            pyautogui.click(300, 970, button='left')
            pyperclip.paste()
            pyautogui.press('enter')

        else:
            i = i + 1
            print('没找到{}'.format(i))


begin()
