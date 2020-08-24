# /usr/bin/python3
# Created By Erik
from colorama import Fore, init
import pyshorteners
import os, sys, time, random, json

colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]
color = random.choice(colors)

def main():
    Banner()
    print("")
    print("[{}01{}]  Google".format(color, Fore.LIGHTWHITE_EX))
    print("[{}02{}]  Youtube".format(color, Fore.LIGHTWHITE_EX))
    print("[{}03{}]  Spotify".format(color, Fore.LIGHTWHITE_EX))
    print("[{}04{}]  Instagram".format(color, Fore.LIGHTWHITE_EX))
    print("[{}05{}]  Facebook".format(color, Fore.LIGHTWHITE_EX))
    print("[{}06{}]  New York Times".format(color, Fore.LIGHTWHITE_EX))
    print("[{}07{}]  Personalized".format(color, Fore.LIGHTWHITE_EX))
    print("")
    print("[{}99{}]  Back".format(color, Fore.LIGHTWHITE_EX))
    print("")

    option = input(str(" Z0172CK ({}UrlHiden{}) > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    if option == '01' or option == '1':
        UrlGoogle()

    elif option == '02' or option == '2':
        UrlYoutube()

    elif option == '03' or option == '3':
        UrlSpotify()

    elif option == '04' or option == '4':
        UrlInstagram()

    elif option == '05' or option == '5':
        UrlFacebook()

    elif option == '06' or option == '6':
        UrlNewyorkTimes()

    elif option == '07' or option == '7':
        UrlPersonalized()

    elif option == '99':
        sys.exit()

    else:
        print("[!] Option not avalible")
        main()

def UrlGoogle():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Google{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    print("")
    Postlink = str(input("Z0172CK ({}UrlHiden/Google{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("Your link is: {}https://www.google.com-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("\n")
def UrlYoutube():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Youtube{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    
    Postlink = str(input("Z0172CK ({}UrlHiden/Youtube{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("Your link is: {}https://www.youtube.com-video-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("\n")

def UrlSpotify():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Spotify{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Postlink = str(input("Z0172CK ({}UrlHiden/Spotify{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("Your link is: {}https://www.spotify.com-video-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("\n")

def UrlInstagram():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Instagram{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    
    Postlink = str(input("Z0172CK ({}UrlHiden/Instagram{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("Your link is: {}https://www.instagram.com-photo-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("\n")

def UrlFacebook():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Facebook{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    
    Postlink = str(input("Z0172CK ({}UrlHiden/FaceBook{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print("\n\n")
    print("Your link is: {}https://www.facebook.com-profile-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("")

def UrlNewyorkTimes():
    print("")
    OriginalLink = str(input("Z0172CK ({}UrlHiden/NewyorkTime{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Postlink = str(input("Z0172CK ({}UrlHiden/NewyorkTimes{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("Your link is: {}https://www.newyorktimes.com-{}@{}{}".format(Fore.LIGHTRED_EX, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("")


def UrlPersonalized():
    print("")
    Domain = str(input("Z0172CK ({}UrlHiden/Personalized{}) Domain >  ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    OriginalLink = str(input("Z0172CK ({}UrlHiden/Personalized{}) Original URL > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))
    
    
    Postlink = str(input("Z0172CK ({}UrlHiden/Personalized{}) Post LINK > ".format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]

    print("\n\n")
    print("link is: {}https://www.{}-{}@{}{}".format(Fore.LIGHTRED_EX ,Domain, Postlink, Withouthttp, Fore.LIGHTWHITE_EX))
    time.sleep(2)
    print("\n")
    
def Banner():
    print('''{}
 █    ██  ██▀███   ██▓        ██░ ██  ██▓▓█████▄ ▓█████  ███▄    █ 
 ██  ▓██▒▓██ ▒ ██▒▓██▒       ▓██░ ██▒▓██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ 
▓██  ▒██░▓██ ░▄█ ▒▒██░       ▒██▀▀██░▒██▒░██   █▌▒███   ▓██  ▀█ ██▒
▓▓█  ░██░▒██▀▀█▄  ▒██░       ░▓█ ░██ ░██░░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒
▒▒█████▓ ░██▓ ▒██▒░██████▒   ░▓█▒░██▓░██░░▒████▓ ░▒████▒▒██░   ▓██░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░    ▒ ░░▒░▒░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░    ▒ ░▒░ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░
 ░░░ ░ ░   ░░   ░   ░ ░       ░  ░░ ░ ▒ ░ ░ ░  ░    ░      ░   ░ ░ 
   ░        ░         ░  ░    ░  ░  ░ ░     ░       ░  ░         ░ 
                                          ░                        
                                            By Erik172 @erik172_

    {}'''.format(color, Fore.LIGHTWHITE_EX))

    