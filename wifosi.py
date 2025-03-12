import pywifi
from pywifi import const 
import requests
import pyfiglet 
import os 

vb = pyfiglet.figlet_format("wifosi")
print(vb)

print("wifscn = wifi network scan and bssid find")
print("manf = wifi manufacturer information")

print("_______________________________________________")

varb = str(input("\ncommand = "))

if varb == "wifscn":
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    resulst = iface.scan_results()
    for netwrok in resulst:
        if netwrok.ssid:
            encryption = []
            if not netwrok.akm:
                encryption.append("open")
            encryption_str = "/".join(set(encryption))
            print(f"{netwrok.ssid}  {netwrok.bssid}  {netwrok.signal}")
else:
    print("command not found")
    exit()
    