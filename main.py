import pyautogui
import time
import pyperclip
import cv2
import pyperclip


imgxx = cv2.imread('hbxx2.png')
imghb = cv2.imread('hb2.png')
imgk = cv2.imread('kai.png')
imgx = cv2.imread('x.png')

def begin():
    i = 0
    while True:
        location = pyautogui.locateCenterOnScreen(imgxx)
        #location = pyautogui.locateCenterOnScreen(imgshuzhen)
        if location is not None:
            print('找到红包！')
            pyautogui.click(location.x,location.y,button='left')
            # while True:
            #     location2 = pyautogui.locateCenterOnScreen(imghb)
            #     if location2 is not None:
            #         pyautogui.click(location2.x,location2.y,button='left')
            #         break
            #     print('没找到')
            time.sleep(0.5)
            pyautogui.click(350, 850, button='left') # 点红包
            time.sleep(0.7)
            pyautogui.click(467,685, button='left') # 开红包
            time.sleep(0.5)
            pyautogui.press('esc')
            pyperclip.copy('谢谢老板！')
            time.sleep(1)
            pyautogui.click(300, 970,button='left')
            time.sleep(0.5)
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            pyautogui.press('enter')  # 按下并松开（轻敲）回车键
            time.sleep(0.5)
            pyautogui.click(226, 93, button='left')
            time.sleep(0.5)
        i = i+1
        print('没有红包{}'.format(i))
        time.sleep(0.5)


begin()
