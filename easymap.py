###NMAP AUOMATION ON THE GO RASBIAN PI OS
import os 
import colorama 
import time 
import sys 
from colorama import Fore

os.system(' clear ')
time.sleep(2)
print(" [!] starting nmap automation ")
time.sleep(3)
os.system(' clear ')
print(Fore.MAGENTA+"|===============================================")
print(Fore.MAGENTA+"| ____                      _   ____            ")
print(Fore.MAGENTA+"||  _ \ __ _ _ __ _ __ ___ | |_/ ___|  ___  ___ ")
print(Fore.MAGENTA+"|| |_) / _` | '__| '__/ _ \| __\___ \ / _ \/ __|")
print(Fore.MAGENTA+"||  __/ (_| | |  | | | (_) | |_ ___) |  __/ (__ ")
print(Fore.MAGENTA+"||_|   \__,_|_|  |_|  \___/ \__|____/ \___|\___|")
print(Fore.MAGENTA+"|===============================================")
print("|[1] ===>>  Simple scan                        |")
print("|[2] ===>>  UDP scan                           |")
print("|[3] ===>>  IPV6 scan                          |")
print("|[4] ===>>  list scan                          |")
print("|[5] ===>>  ping scan                          |")
print("|[6] ===>>  try every probe                    |")
print("|[7] ===>>  IPA RANGE SCAN                     |")
print("|[8] ===>>  MASS SCAN                          |")
print("|==============================================|") 
A = str(input(" [-] Options ==>> "))

if '1' in A:
       os.system(' clear ')
       IP = str(input(" [!]IPA: "))
       os.system(f' nmap {IP} ')

if '2' in A:
       os.system(' clear ')
       PI = str(input(" [!]IPA: "))
       os.system(f' sudo nmap -sU {PI} ')

if '3' in A:
       os.system(' clear ')
       OP = str(input(" [!]IPV6: "))
       os.system(f' nmap -6 {OP} ')

if '4' in A:
       os.system(' clear ')
       IO = str(input(" [-]IP 1 ==>  "))
       PO = str(input(" [-]IP 2 ==>  "))
       NO = str(input(" [-]IP 3 ==>  "))
       os.system(f' nmap {IO} {PO} {NO} ') 

if '5' in A:
       os.system(' clear ')
       OP = str(input(" [-]IPA ==> "))
       os.system(f' nmap -sn {OP} ')

if '6' in A:
       os.system(' clear ')
       IP = str(input(" [-]IPA ==> "))
       os.system(f' nmap -sV {IP}  ')        

if '7' in A:
       os.system(' clear ')
       OP = str(input(" IPA ==>> "))
       RANGE = str(input(" RANGE ==>> "))
       os.system(f' nmap {OP}-{RANGE} ')

if '8' in A:
       os.system(' clear ')
       print(" this is a massive all at once scan ")
       print(" please note this can take a while ")
       time.sleep(2)
       os.system(' clear ')
       os.system(' date ')
       time.sleep(1.5)
       os.system(' clear ')
       IPV4 = str(input(" [-]IPV4 ==>>> "))
       os.system(f' sudo namp -A -sU -O {IPV4} ')
