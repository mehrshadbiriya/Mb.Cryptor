from json.tool import main
import os, sys, design, myClasses
from click import option
from colorama import Fore as color
from time import sleep

bold = '\033[1m'
endbold = '\033[0m'


##########################

try:
    from colorama import Fore as color
except:
    print("Install The colorama library")

###########################

myClasses.Introduce()

while True:

    try:
        os.system('clear');design.banner();design.menu()
        option = int(input(color.RED+"\n[⚡] "+color.RED+"MB.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.GREEN+" ⇒ " ))
    
    #CHECK FOR OPTION
        if (option == 1):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"MB.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"base64"+color.LIGHTCYAN_EX+'/'+color.GREEN+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t ")
            os.system(f'echo {user_option} | base64')
            input('\n press any key...'+endbold)
            continue


        elif (option == 2):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"MB.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"hex"+color.LIGHTCYAN_EX+'/'+color.GREEN+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | xxd -p")
            input('\n press any key...'+endbold)
            continue

        elif (option == 3):
            os.system('clear');design.banner()
            print(color.WHITE+"Enter Your Text:")
            user_option = input(color.RED+"\n[⚡] "+color.RED+"MB.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"rot13"+color.LIGHTCYAN_EX+'/'+color.GREEN+" ⇒ " )
            print(bold+color.WHITE+"Encrypted ⚶\n \t")
            os.system(f"echo {user_option} | tr 'A-Za-z' 'N-ZA-Mn-za-m'")
            
            input('\n press any key...'+endbold)
            continue
        ##################DECODER
        
        elif (option == 4):
            os.system('clear');design.banner();design.decoder_menu()
            option = int(input(color.RED+"\n[⚡] "+color.RED+"MB.cryptor"+color.LIGHTCYAN_EX+'/'+color.LIGHTWHITE_EX+"home"+color.LIGHTCYAN_EX+'/'+color.GREEN+" ⇒ " ))
            design.decoder_menu(option)
            continue
            
        elif (option == 0):
            os.system('clear')
            sys.exit()


    except:
        sys.exit