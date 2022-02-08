from re import S
from colorama import Fore as color
from time import sleep

bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(bold+color.CYAN+'''



     __  __ ____   _____ _______     _______ _______ ____  _____  
    |  \/  |  _ \ / ____|  __ \ \   / /  __ \__   __/ __ \|  __ \ 
    | \  / | |_) | |    | |__) \ \_/ /| |__) | | | | |  | | |__) |
    | |\/| |  _ <| |    |  _  / \   / |  ___/  | | | |  | |  _  / 
    | |  | | |_) | |____| | \ \  | |  | |      | | | |__| | | \ \ 
    |_|  |_|____(_)_____|_|  \_\ |_|  |_|      |_|  \____/|_|  \_\                                                                          
     
                                                 Base64 | Hex | rot13                      
    
    '''+endbold)
    print(color.CYAN+'-----------------------------------------------------------------------')
    print(bold+color.CYAN+'''
    ------------------------------------
    | Developer : Mehrshad_Biriya      | 
    | Email : shadmehrbiriya@gmail.com |
    | IG : Mehrshad._.biriya           |
    ------------------------------------  
    '''+endbold)
    print(color.CYAN+'-----------------------------------------------------------------------')
    sleep(0.5)
    print()


def menu():

  print(bold+color.WHITE+"[1]" +color.LIGHTGREEN_EX+" Base64")
  print(color.RED+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[2]"+color.LIGHTGREEN_EX+" Hex")
  print(color.RED+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[3]"+color.LIGHTGREEN_EX+" Rot13")
  print(color.RED+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[4]"+color.LIGHTGREEN_EX+" Decoder")
  print(color.RED+"*********************")
  sleep(0.1)
  print(bold+color.WHITE+"[0]"+color.LIGHTGREEN_EX+" exit"+endbold)


def decoder_menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTGREEN_EX+" Base64")
    print(color.RED+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTGREEN_EX+" Hex")
    print(color.RED+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTGREEN_EX+" Rot13")
    print(color.RED+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTGREEN_EX+" back"+endbold)