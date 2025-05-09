import os
import time
import pyautogui
import random

# List of search queries
search_queries = [
    
  # Any queries you want to search for

]

os.startfile("msedge.exe")

time.sleep(3)
for i in range(len(search_queries)):  
    query =  search_queries[i] 
 
    pyautogui.write(query, interval=0.1)

    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.hotkey('ctrl','e')

    pyautogui.hotkey('ctrl', 'a')  

    pyautogui.press('backspace')   
