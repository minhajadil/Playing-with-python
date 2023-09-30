import pyautogui
import time

n = input()
n = int(n)

# to open notepad : (took extra sleep time to ensure apps opening)
pyautogui.press('win')
time.sleep(5)
pyautogui.write('Notepad', interval=0.25)
pyautogui.press('enter')

cnt = 1

time.sleep(10)

for i in range(n):
    for j in range(cnt):
        pyautogui.press('#')
    pyautogui.press('enter')
    cnt += 1

# to close notepad after the printing (without saving the file)
time.sleep(7)
pyautogui.hotkey('alt', 'f4')
pyautogui.press('right')
time.sleep(3)
pyautogui.press('enter')
