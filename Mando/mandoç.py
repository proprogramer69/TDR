import serial
import pyautogui
port = "COM3"
bluetooth = serial.Serial(port, 9600)
while True:
    #pyautogui.press('a')
    bluetooth.flushInput()
    input_data = bluetooth.readline()  # decode
    dada = input_data.splitlines()
    dada = str(dada[0])
    dada = dada.replace("b", "")
    dada = dada.replace("'", "")
    if dada == "1":
        pyautogui.press('up')
    elif dada == "3":
        pyautogui.press("down")
    elif dada == "2":
        pyautogui.press('right')
    elif dada == "4":
        pyautogui.press("left")
