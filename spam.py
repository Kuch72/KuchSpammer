# Input spammer made by Kuch!#0001, enjoy
import pyautogui, colorama, os, time, webbrowser
from colorama import init
init(autoreset=True)

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[39m"

def borrarpant():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def bienvenida():
    print("")
    print(RED+"██╗  ██╗██╗   ██╗ ██████╗██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗")
    print(RED+"██║ ██╔╝██║   ██║██╔════╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║")
    print(RED+"█████╔╝ ██║   ██║██║     ███████║    ███████╗██████╔╝███████║██╔████╔██║")
    print(RED+"██╔═██╗ ██║   ██║██║     ██╔══██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║")
    print(RED+"██║  ██╗╚██████╔╝╚██████╗██║  ██║    ███████║██║     ██║  ██║██║ ╚═╝ ██║")
    print(RED+"╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝")
    print("")                                                                                   
    print(GREEN+"Herramienta de automatización de spam universal desarrollada por Kuch!#0001 o Kuch72 en github")


def spam():
    bienvenida()
    inicio = 0
    print("")
    entrada1 = (input("Introduce el mensaje a enviar: "))
    time.sleep(2)
    entrada2 = int(input("Introduce el numero de mensajes: "))
    print(YELLOW+"Empezando spam en 5 segundos... ")
    time.sleep(5)

    while True:
        inicio += 1
        pyautogui.typewrite(entrada1)
        pyautogui.press("enter")
        if inicio == entrada2:
            break
            
            
def asd():
    print(CYAN+"""
    [1] Centro de SPAM
    [2] Visitar mi github
    """)

def kaxh():
    bienvenida()
    asd()
    opcion = input("Su opcion: ")
    if opcion == "1":
        print("")
        print(RED+"Redirigiendo... ")
        print("")
        time.sleep(2)
        borrarpant()
        spam()
    elif opcion == "2":
        github = "https://github.com/Kuch72"
        webbrowser.open(github)
        print(BLUE+"Gracias por utilizar esta herramienta.")
        print(RED+"Saliendo...")
        time.sleep(2)
        quit()
    else:
        print(RED+"Argumento inválido.")

kaxh()
borrarpant()
