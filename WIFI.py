import os
import time

def show_banner():
    os.system("clear")  # Terminal clear karega
    print("\033[1;31m")  # Red Color Text
    print("#############################################################")
    print("#                                                           #")
    print("#                     WELCOME TO TEAM 777                   #")
    print("#                  WIFI NETWORK SCANNER TOOL                #")
    print("#                                                           #")
    print("#############################################################")
    print("\033[0m")  # Reset color
    time.sleep(1)

def scan_wifi_network():
    print("[*] Scanning Wi-Fi network for connected devices...\n")
    os.system("nmap -sn 192.168.1.1/24 --unprivileged -T4 > wifi_scan_result.txt")
    
    print("[*] Scan completed! Showing connected devices:\n")
    os.system("grep 'Nmap scan report' wifi_scan_result.txt | awk '{print $5}'")
    print("\n[*] If no devices are listed, ensure you are connected to a Wi-Fi network.")

if __name__ == "__main__":
    show_banner()
    scan_wifi_network()
