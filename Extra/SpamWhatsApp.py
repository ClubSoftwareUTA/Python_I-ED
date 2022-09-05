import pyautogui
import webbrowser as web
from time import sleep

def spam():
    # Open WhatsApp Web phone=593999999999 numero de telefono
    web.open("https://web.whatsapp.com/send?phone=593999999999")
    # Espera 20 segundos para que cargue la pagina
    sleep(20)
    # numero de veces que se repite el mensaje
    for i in range(50):
        pyautogui.typewrite("Mensaje")
        pyautogui.press("enter")

spam()