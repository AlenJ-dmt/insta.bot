import pyautogui
import time
import tkinter as tk

def go_to_page(webpage):
    pyautogui.moveTo(300,50)
    pyautogui.click()
    time.sleep(2)
    if 'https://' in webpage:
        pyautogui.write(webpage)
    else:
        pyautogui.write('https://' + webpage)
    time.sleep(2)
    pyautogui.press('enter')


def open_navigator():
    pyautogui.moveTo(600, 750)
    pyautogui.click()
    time.sleep(3)

def go_to_profile():

    open_navigator()
    go_to_page('instagram.com')
    
    user_id = entry1.get()
    
    time.sleep(3)

    pyautogui.moveTo(674, 99)
    
    time.sleep(2)
    pyautogui.click()
    pyautogui.write(user_id)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')

    x = entry2.get()
    x = int(x)
    click_on_followers(x)

    #Once on profile
    
def click_on_followers(num):

    time.sleep(3)
    pyautogui.moveTo(723, 225)
    time.sleep(3)
    pyautogui.click()
    time.sleep(5)

    i = 0
    while num > i:
        
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('follow_btn.png'))
        time.sleep(3)
        pyautogui.click()
        time.sleep(5)
        pyautogui.scroll(-100)
        time.sleep(3)
        i = i + 1
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('close_followers_btn.png'))
    pyautogui.click()

def unfollow_people(answer):
    time.sleep(4)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('profile.png'))
    time.sleep(3)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('following_btn.png'))
    time.sleep(4)
    pyautogui.click()


    
#Creates window
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height= 200)
canvas1.pack()

#Add account Entry Box

get_user_label = tk.Label(text= 'Enter account to follow:')
canvas1.create_window(100, 50, window = get_user_label)

entry1 = tk.Entry(root)
canvas1.create_window(400, 50, window = entry1)

#Add How many to follow

get_qty = tk.Label(text = 'Enter how many people to follow(number):')
canvas1.create_window(150, 100, window = get_qty)

entry2 = tk.Entry(root)
canvas1.create_window(400, 100, window= entry2)
                   

#Add Btn

button1 = tk.Button(text='Get User', command =go_to_profile)
canvas1.create_window(225, 150, window = button1)


root.mainloop()

