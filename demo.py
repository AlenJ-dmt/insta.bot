import pyautogui as py

x = py.locateCenterOnScreen('ok.png')
y = (6, 6)
print(x)
if str(x) != 'None':
    py.moveTo(x)
    py.click()
else:
    print('lesser')
