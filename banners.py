from colorama import Fore, init
import random
import sys
import os

init()

def println(n):
  colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]
  color = random.choice(colors)
  banner1 = """{}
                                                           _   __,----'~~~~~~~~~`-----.__
                                        .  .    `//====-              ____,-'~`
                        -.            \_|// .   /||\\  `~~~~`---.___./
                  ______-==.       _-~o  `\/    |||  \\           _,'`
            __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
         _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
       .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
      / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
     ,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
               '         `-|      /|    )-'\~'      _,--"'
                           '-~^\_/ |    |   `\_   ,^             /|
                                /  \     \__   \/~               `\__
                            _,-' _/'\ ,-'~____-'`-/                 ``===°
                           ((->/'    \|||' `.     `\.  ,                _||
             ./                       \_     `\      `~---|__i__i__\--~'_/
            <_n_                     __-^-_    `)  \-.______________,-~'
             `B'\)                  ///,-'~`__--^-  |-------~~~~^'
             /^>                           ///,--~`-/
            `  `                                       -Erick172
    {}""".format(color, Fore.LIGHTWHITE_EX)

  banner2 = '''{}
                                                         _  _
                                                        ' \/ '
        _   _                        <|
          \/              __'__     __'__      __'__
                        /    /    /    /     /    /
                        /\____\    \____\     \____\              _  _
                      / ___!___   ___!___    ___!___               \/
                    // (      (  (      (   (      (
                  / /   \______\  \______\   \______(
                /  /   ____!_____ ___!______ ____!_____
              /   /   /         //         //         /
            /  E /   |     R   ||    I     ||   K     |
          /_____/     \         \          \          (
                \      \_________\__________\__________(
                  \         |          |         |
                  \________!__________!_________!________/
                    \|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_/| Shodan
                    \    _______________                /
      ^^^%^%^^^%^^\_"/_)/_)_/_)__)/_)/)/)_)_"_'_"_//)/)/)/)%^^^%^^^
      ^!!^^"!!^^^!^^^!!^^^%!!!!^^^^^^!!^^^!!!!!!%^^^^%^^%^^^!
    {}'''.format(color, Fore.LIGHTWHITE_EX)

  banner3 ='''{}
    . _  .    .__  .  .  __,--'
      (_)    '/__\ __,--'
    '  .  ' . | o|'     IpInfo
             [IIII]`--.__
              |  |       `--.__
              | :|             `--.__
              |  |                   `--.__
    ._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--..-.,._.,,._,-,.Erik172
    {}'''.format(color, Fore.LIGHTWHITE_EX)

  banner4 = '''{}
    
                   _______________________________________________________
                  |                                                      |
             /    |                                                      |
            /---, |           P   A  Y  L  O  A  D                       |
       -----# ==| |                     G  E  N  E  R  A  T  E           |
       | :) # ==| |                                                      |
  -----'----#   | |______________________________________________________|
  |)___()  '#   |______====____   \___________________________________|
 [_/,-,\"--"------ //,-,  ,-,\|\   |/             //,-,  ,-,  ,-,\  __#Erik172#
   ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||
----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------
  {}'''.format(color, Fore.LIGHTWHITE_EX)

  banner5 = """{}
     ____
     \   `.
      \    `.
       \ \   `.
        \ 01838`.
        :. . . . `._______________________.-~|~~-._
        \                                 ---'-----`-._
         /"""""""/             _...---------..         ~-._________
        //     .`_________  .-`           \ .-~           /
       //    .'       ||__.~             .-~_____________/
      //___.`           .~            .-~
                      .~           .-~
                    .~         _.-~
                    `-_____.-~'
  {}""".format(color, Fore.LIGHTWHITE_EX)

  banner6 = """{}
                                                         c=====e
                                                            H
   ____________                                         _,,_H__
  (__((__((___()                                       //|     |
 (__((__((___()()_____________________________________// |ERIK |
(__((__((___()()()------------------------------------'  |_____|
      Brute Force V0.1
  {}""".format(color, Fore.LIGHTWHITE_EX)

  Fsociety = """{}
                              ....'''...                              
                        .':oxOKXXNNNNNXK0kdc;.                        
                     .;d0NWMMMMMMMMMMMMMMMMMWXkc.                     
                    :OWMMMMMMMMMMMMMMMMMMMMMMMMW0c.                   
                  .lNMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.                  
                  .oKWMMMWWWWMMMMMMMMMMMMWWWWMMMMXx.                  
                   .'xXOdol:;lkXMMMMMMNOl::cookX0:.                   
                   ..:xdk0Kk:...cONW0l'..;xKKkoxl...                  
                   .;d0XWMWNKOo,,xNWO;,lkKXWMWXKk:,.                  
                  .xXXxkNk;..'l0XXWMNX0o,..,dXOdXNk'                  
                  lNMWK0kc;;,.,OKOXM0O0;.';;:x0KWMWd.                 
                 .xWMWNKXNWWNK0OkONMXOkkKNWWNXXNWMMO.                 
                 .kWXd:kWMMMMM0xXWMMMWOkNMMMMMKllKMO.                 
                 .xXc .dNWNKko;,oKNNKo,,cx0NWNk. :Kk.                 
                  :x'  .','.     .''.     .','.  'kl                  
                  .;;.                          .cl.                  
                    'llc;;;,............ .',;;cod;                    
                     ,0MWWWNk;. .........oKWWWMNc                     
                     .xWMMMMMNOoc:;;:cokXWMMMMMO.                     
                      :XMMMMMMMMMMWWMMMMMMMMMMNo                      
                       :0WMMMMMMMMMMMMMMMMMMMNd.                      
                        .oKWMMMMMMMMMMMMMMMXx;                        
                          .lONWMMMMMMMMMWKd'                          
                            .':lodxxxdoc,.   By Erick172
                                                by Z0172CK   
    {}""".format(color, Fore.LIGHTWHITE_EX)

  if n == 1 or n == '1':
    print(banner1)
      
  elif n == 2 or n == '2':
    print(banner2)
      
  elif n == 3 or n == '3':
    print(banner3)

  elif n == 4 or n == '4':
    print(banner4)
  
  elif n == 5 or n == '5':
    print(banner5)
  
  elif n == 6 or n == '6':
    print(banner6)

  elif n == 0 or n == '0':
    print(Fsociety)
  
  else:
    print("Banner")