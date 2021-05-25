import pyautogui, time

time.sleep(4) #time for running xd 
numberOfMenssages = 50
j = 0


for i in range(numeroDeMensajes):
    j = j + 1 #simple counter to make it more funny 
    pyautogui.typewrite(f"Message Number: {contador}") #here goes the text wich we are going to send
    pyautogui.press("enter")
