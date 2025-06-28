import pyautogui
import time

def send_kakao_message():
    # Get user inputs
    chat_name = input("Enter the chat name: ")
    message = input("Enter the message: ")
    repeat_count = int(input("Enter how many times to send the message: "))

    print("Starting in 5 seconds...")
    time.sleep(5)

    
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)  
    pyautogui.write(chat_name, interval=0.05) 
    time.sleep(0.5)
    pyautogui.press('enter') 

    time.sleep(0.5) 
    
    for _ in range(repeat_count):
        pyautogui.write(message)  
        pyautogui.press('enter') 

    print("Messages sent successfully!")


send_kakao_message()
