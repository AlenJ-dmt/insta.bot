import time
import pyautogui
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

    
def initiate_session():

    pyautogui.moveTo(pyautogui.locateCenterOnScreen('google.png'))
    pyautogui.click()
    pyautogui.click()

    time.sleep(3)

    pyautogui.moveTo(1340, 90)
    pyautogui.click()
    time.sleep(3)
    go_to_page("https://www.instagram.com/")
    time.sleep(2)

def log_in(account, password):
    pyautogui.moveTo(800, 270)
    pyautogui.click()
    time.sleep(3)
    pyautogui.write(account)
    time.sleep(3)
    pyautogui.moveTo(800, 320)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write(password)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.moveTo(700, 550)
    pyautogui.click()

def go_to_profile():

    initiate_session()
    log_in(account = account_Entry.get(), password = password_Entry.get())
    
    
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

    unfollow_people(answer= unfollow_entry.get())

    #Once on profile
    
def click_on_followers(num):

    time.sleep(3)
    pyautogui.moveTo(700, 225)
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
    
    if answer == 'yes':
        time.sleep(4)
        go_to_page('https://www.instagram.com/rollossolutions/')
        time.sleep(3)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(800, 225)
        time.sleep(4)
        pyautogui.click()

        i = 0
        while 100 > i:
            
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('following.png'))
            time.sleep(3)
            pyautogui.click()
            time.sleep(5)
            pyautogui.scroll(-100)
            time.sleep(3)
            i = i + 1



#Creates window
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height= 300)
canvas1.pack()

#Login Info

account_label = tk.Label (text = 'Username: ')
canvas1.create_window(100, 50, window = account_label)

account_Entry = tk.Entry(root)
canvas1.create_window(400, 50, window = account_Entry)

password_label = tk.Label (text = 'Password: ')
canvas1.create_window(100, 100, window = password_label)

password_Entry = tk.Entry(root)
canvas1.create_window(400, 100, window = password_Entry)
                          


#Add account Entry Box

get_user_label = tk.Label(text= 'Enter account to follow:')
canvas1.create_window(100, 150, window = get_user_label)

entry1 = tk.Entry(root)
canvas1.create_window(400, 150, window = entry1)

#Add How many to follow

get_qty = tk.Label(text = 'Enter how many people to follow(number):')
canvas1.create_window(150, 200, window = get_qty)

entry2 = tk.Entry(root)
canvas1.create_window(400, 200, window= entry2)

#Unfollow People

unfollow_label = tk.Label(text = 'Do you want to unfollow people?(yes/no):')
canvas1.create_window(150 , 225, window = unfollow_label)

unfollow_entry = tk.Entry(root)
canvas1.create_window(400, 225, window = unfollow_entry)

#Add Btn

button1 = tk.Button(text='Get User', command =go_to_profile)
canvas1.create_window(225, 250, window = button1)


root.mainloop()

