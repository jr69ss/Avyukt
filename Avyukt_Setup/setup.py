try:
    import subprocess
    import re
    import platform
    import time
    import os
    import sys
    from colorama import Fore
    import requests
    import pyfiglet
except ImportError:
    subprocess.call("pip install colorama", shell=True)
    subprocess.call("pip install pyfiglet", shell=True)
    subprocess.call("pip install requests", shell=True)

error_message = Fore.RED
success = Fore.GREEN

try:
    def setup():
        ascii_banner = pyfiglet.figlet_format("Avyukt Setup")
        print(ascii_banner)
        print(Fore.YELLOW + "\n[+] Setup File Version 1.0 (Beta)")
        print(Fore.YELLOW + "\n[+] Setup Build Date : 23/8/2020")
        print(Fore.YELLOW + "\n[+] Detected OS : " + platform.system())
        print(Fore.YELLOW + "\n[+] OS Release : " + platform.release())
        print(Fore.CYAN + "\n[+] Starting Setup, Please wait ... ")
        time.sleep(5)
        start_installation = raw_input("\nAvyukt>: Type y if you want to start installation else n >> ")
        if "y" in start_installation:
            print("\n[+] Starting Installation .... Sit Back and Relax!")
            print(Fore.CYAN + "\n\t[+] Updating Packages using apt-get update")
            print("\n")
            os.system("sudo apt-get update")
            print(Fore.CYAN + "\n\t[+] Installing Wine")
            print(Fore.YELLOW + "\n")
            subprocess.call("\n\nsudo apt-get install wine32", shell=True)
            print(Fore.YELLOW + "\n")
            print(Fore.CYAN + "\n\t[+] Downloading Python 2.7.14 MSI File")
            url = 'https://www.python.org/ftp/python/2.7.14/python-2.7.14.amd64.msi'
            r = requests.get(url, allow_redirects=True)
            open('python-2.7.14.amd64.msi', 'wb').write(r.content)
            print(Fore.CYAN + "\n\t[+] Installing Python 2.7.14 in Wine")
            print(Fore.YELLOW + "\n")
            subprocess.call("\n\nwine msiexec /i python-2.7.14.amd64.msi", shell=True)
            print(os.getcwd())
            os.chdir("/root/.wine/drive_c/Python27/")
            print(Fore.CYAN + "\n\t[+] Installing PyArmor")
            print(Fore.YELLOW + "\n")
            os.system("\n\nwine python.exe -m pip install pyarmor")
            print(Fore.CYAN + "\n\t[+] Installing PyInstaller")
            print(Fore.YELLOW + "\n")
            os.system("\n\nwine python.exe -m pip install pyinstaller")
            raw_input(Fore.GREEN + "\n[+] Setup was completed, Press enter to continue")
            raw_input("")
            os.system("reset")

        if "n" in start_installation:
            print(error_message + "\n[+] Quitting setup ..")
            os.system("reset")

except KeyboardInterrupt:
    print("[+] Quitting ")

setup()