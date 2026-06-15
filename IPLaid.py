import socket
import requests
import os
import time
import threading
import ipaddress
import asyncio
from urllib.parse import urlparse
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

lock = threading.Lock()

# =========================
# 🔹 CONFIG
# =========================
MAX_CONCURRENT = 800
OUTPUT_FILE = "Iplaid_scan.txt"

# =========================
# 🔹 CLEAR SCREEN
# =========================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# =========================
# 🔹 LOADING (SCI-FI STYLE)
# =========================
def loading():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    print(Fore.CYAN + Style.BRIGHT + "\n[ INITIALIZING NEURAL SCAN ENGINE ]" + Fore.RESET)
    for i in range(3):
        for frame in frames:
            print(Fore.GREEN + f"\r[>] BOOTING IPLaid v3.1.7 {frame}" + Fore.RESET, end="")
            time.sleep(0.05)
    clear()
    time.sleep(0.2)

# =========================
# 🔹 BANNER (REPLACED WITH SCI-FI ART + AUTHOR)
# =========================
def banner():
    sci_fi_art = f"""
{Fore.RED}{Style.BRIGHT}
        #####  #  ##### ##                     
     ######  / ######  /###                    
    /#   /  / /#   /  /  ###                   
   /    /  / /    /  /    ###                  
       /  /      /  /      ##                  
      ## ##     ## ##      ##                  
      ## ##     ## ##      ##                  
    /### ##   /### ##      /                   
   / ### ##  / ### ##     /                    
      ## ##     ## ######/                     
 ##   ## ##     ## ######                      
###   #  /      ## ##                          
 ###    /       ## ##                          
  #####/        ## ##                          
    ###    ##   ## ##                          
          ###   #  /                           
           ###    /                            
            #####/                             
              ###                              
                                               
     ##### /                             ##    
  ######  /                    #          ##   
 /#   /  /                    ###         ##   
/    /  /                      #          ##   
    /  /                                  ##   
   ## ##              /###   ###      ### ##   
   ## ##             / ###  / ###    ######### 
   ## ##            /   ###/   ##   ##   ####  
   ## ##           ##    ##    ##   ##    ##   
   ## ##           ##    ##    ##   ##    ##   
   #  ##           ##    ##    ##   ##    ##   
      /            ##    ##    ##   ##    ##   
  /##/           / ##    /#    ##   ##    /#   
 /  ############/   ####/ ##   ### / ####/     
/     #########      ###   ##   ##/   ###      
#                                              
 ##                                            
{Fore.CYAN}{Style.BRIGHT}
╔════════════════════════════════════════════════════════════════╗
║   IP LAID           v3.1.7        //  ADVANCED NETWORK SUITE   ║
║   CODED BY: SYLHETYHACKVENGER (THE-ERROR808)                   ║
║   RELEASE: [ SYLHET BD EDITION ]                               ║
╚════════════════════════════════════════════════════════════════╝
{Fore.YELLOW}{Style.DIM}   “Pushing bits through the void – like a ghost in the wire”{Fore.RESET}
"""
    print(sci_fi_art)

# =========================
# 🔹 DOMAIN CLEAN
# =========================
def clean_domain(input_value):
    if input_value.startswith("http"):
        return urlparse(input_value).netloc
    return input_value.strip()

# =========================
# 🔹 DOMAIN LOOKUP (SCI-FI OUTPUT)
# =========================
def lookup(target):
    print(Fore.MAGENTA + Style.BRIGHT + "\n[>>] TARGET LOCK: DECODING DOMAIN ENTITY...\n")
    domain = clean_domain(target)

    try:
        ip = socket.gethostbyname(domain)
    except:
        print(Fore.RED + "[!] // ERROR: DOMAIN RESOLUTION FAILED //\n")
        return

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = "Not Found"

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", timeout=5).json()
    except:
        res = {}

    print(Fore.CYAN + Style.BRIGHT + "╔════════════════════════════════════════════╗")
    print(Fore.CYAN + "║" + Fore.GREEN + f"  🌐 DOMAIN      : {domain:<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.GREEN + f"  🟢 IP ADDRESS  : {ip:<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.MAGENTA + f"  🧠 HOSTNAME    : {hostname:<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "╠════════════════════════════════════════════╣")
    print(Fore.CYAN + "║" + Fore.YELLOW + f"  🌍 COUNTRY     : {res.get('country','Unknown'):<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f"  🏙️ CITY        : {res.get('city','Unknown'):<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f"  📡 ISP         : {res.get('isp','Unknown'):<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f"  🏢 ORG         : {res.get('org','Unknown'):<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + f"  🔢 ASN         : {res.get('as','Unknown'):<32}" + Fore.CYAN + "║")
    print(Fore.CYAN + "╚════════════════════════════════════════════╝\n")

# =========================
# 🔹 EXTRACT TITLE
# =========================
def extract_title(html):
    try:
        html = html.lower()
        if "<title>" in html:
            return html.split("<title>")[1].split("</title>")[0].strip()
    except:
        pass
    return None

# =========================
# 🔹 IP SCAN (OPTION 2) - SCI-FI STYLE
# =========================
def scan_ip(ip):
    ip = str(ip)

    hostname = None
    server = None
    title = None

    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        pass

    try:
        r = requests.get(f"http://{ip}", timeout=2)
        server = r.headers.get("Server")
        title = extract_title(r.text)
    except:
        pass

    if not hostname and not server:
        return

    with lock:
        print(Fore.GREEN + Style.BRIGHT + f"[+] TARGET → {ip}")
        if hostname:
            print(Fore.CYAN + f"    HOSTNAME: {hostname}")
        if server:
            print(Fore.MAGENTA + f"    SERVER  : {server}")
        if title:
            print(Fore.YELLOW + f"    TITLE   : {title}")
        print(Fore.BLUE + "  " + "-"*48)

# =========================
# 🔹 CIDR SCAN
# =========================
def cidr_scan(cidr):
    print(Fore.YELLOW + Style.BRIGHT + f"\n[⚡] INITIATING RANGE SCAN: {cidr}\n")

    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except:
        print(Fore.RED + "[!] INVALID CIDR FORMAT")
        return

    threads = []

    for ip in network.hosts():
        t = threading.Thread(target=scan_ip, args=(ip,))
        t.start()
        threads.append(t)

        if len(threads) >= 100:
            for th in threads:
                th.join()
            threads = []

    for th in threads:
        th.join()

    print(Fore.GREEN + Style.BRIGHT + "\n[✔] SUBNET SCAN COMPLETE\n")

# =========================
# 🔹 SAVE RESULT
# =========================
def save_line(text):
    with open(OUTPUT_FILE, "a") as f:
        f.write(text + "\n")

# =========================
# 🔹 ASYNC PORT CHECK (SCIFI PROGRESS FEEL)
# =========================
async def check_port(ip, port, sem):
    async with sem:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(ip, port), timeout=0.5
            )
            print(Fore.GREEN + f"   [OPEN] PORT {port}")
            save_line(f"{ip}:{port}")
            writer.close()
            await writer.wait_closed()
        except:
            pass

# =========================
# 🔹 DEEP SCAN IP (WITH VISUAL ENHANCEMENT)
# =========================
async def deep_scan_ip(ip):
    print(Fore.CYAN + Style.BRIGHT + f"\n[🔍] DEEP SCAN :: {ip}")

    # hostname
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(Fore.YELLOW + f"   ↳ HOSTNAME : {hostname}")
        save_line(f"{ip} Hostname: {hostname}")
    except:
        pass

    # server + title
    try:
        r = requests.get(f"http://{ip}", timeout=2)
        server = r.headers.get("Server")
        title = extract_title(r.text)

        if server:
            print(Fore.MAGENTA + f"   ↳ SERVER   : {server}")
            save_line(f"{ip} Server: {server}")

        if title:
            print(Fore.LIGHTWHITE_EX + f"   ↳ TITLE    : {title}")
            save_line(f"{ip} Title: {title}")
    except:
        pass

    sem = asyncio.Semaphore(MAX_CONCURRENT)

    # Port scanning range 1-65535
    tasks = [
        check_port(ip, port, sem)
        for port in range(1, 65536)
    ]

    await asyncio.gather(*tasks)

# =========================
# 🔹 DEEP SCAN NETWORK (FULL SCAN)
# =========================
async def deep_scan_network(cidr):
    print(Fore.RED + Style.BRIGHT + f"\n[🔥] FULL DEEP SCAN PROTOCOL: {cidr}\n")
    print(Fore.CYAN + "   [*] MODE: MASS ASYNC PORT SCANNER | MAX CONCURRENT: " + str(MAX_CONCURRENT) + Fore.RESET)

    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except:
        print(Fore.RED + "[!] CIDR MALFORMED")
        return

    open(OUTPUT_FILE, "w").close()

    try:
        for ip in network.hosts():
            await deep_scan_ip(str(ip))
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\n[!] ABORT SIGNAL RECEIVED – SHUTTING DOWN\n")
        return

    print(Fore.GREEN + Style.BRIGHT + f"\n[✔] REPORT SAVED → {OUTPUT_FILE}\n")

# =========================
# 🔹 MAIN MENU (GTA DEVELOPER VISUAL)
# =========================
def main():
    loading()
    clear()
    banner()

    while True:
        print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "┌─────────────────────────────────────────────┐")
        print(Fore.CYAN + Style.BRIGHT + "│  [1] DOMAIN INTELLIGENCE (IP + GEO + HOSTNAME)  │")
        print(Fore.GREEN + Style.BRIGHT + "│  [2] CIDR RANGE SCAN (/24 + SERVER + TITLE)    │")
        print(Fore.YELLOW + Style.BRIGHT + "│  [3] DEEP SCAN (ALL PORTS + SAVE)             │")
        print(Fore.RED + Style.BRIGHT + "│  [4] TERMINATE SESSION                         │")
        print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "└─────────────────────────────────────────────┘")
        choice = input(Fore.MAGENTA + "\nSELECT TARGET PROTOCOL > " + Fore.RESET)

        if choice == "1":
            target = input(Fore.CYAN + "DOMAIN ENTITY > " + Fore.RESET)
            lookup(target)

        elif choice == "2":
            cidr = input(Fore.CYAN + "CIDR BLOCK > " + Fore.RESET)
            cidr_scan(cidr)

        elif choice == "3":
            cidr = input(Fore.CYAN + "CIDR BLOCK > " + Fore.RESET)
            asyncio.run(deep_scan_network(cidr))

        elif choice == "4":
            print(Fore.RED + Style.BRIGHT + "\n[>] SYSTEM SHUTDOWN – STAY IN THE SHADOWS.\n")
            break

        else:
            print(Fore.RED + "[!] INVALID COMMAND – ABORTING")

if __name__ == "__main__":
    main()
