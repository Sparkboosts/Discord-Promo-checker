import os
import re
import sys
import time
import yaml
import struct
import ctypes
import urllib.parse
from pystyle import *
from colorama import Fore, Style, Back,init
init()
try:os.system('cls')
except:pass
from datetime import datetime

def getTimeStampForReq() -> str:
        current_time = datetime.utcnow()
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return formatted_time
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

try:
   mask_promo = config["Mask_Promo"] 
   p_inv = config["Print_Invalid"]
   update_ttl = config["Update_Title"]
   u_cus_proxy = config["Use_Custom_Proxy"]
   proxy = config["Proxy"]
except:
    print("Please Recheck Your Config!")
    time.sleep(10)
    sys.exit(0)

def update_title(title):
    if update_ttl:
      ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        return None
    
def Sprint(tag,content,color):

    return print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}TOOL: {Fore.BLACK}{getTimeStampForReq()}{Fore.WHITE}] [{color}{tag}{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}{content}{Style.RESET_ALL}")

update_title('Welcome To Vintage X Promo Checker')




success = 0
fails   = 0
ratelimited = 0
alr_used = 0
info_title = f' Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer'
update_title(info_title)
ascii_text = '''

'''
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(ascii_text)))
os.system('cls')
threads = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Hey Buyer, Please Enter Amount Of {Fore.BLUE}Threads {Fore.WHITE}To Run {Fore.RED}>>> {Fore.WHITE}')
while not threads.isdigit():
    print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Invalid {Fore.BLUE}Input{Fore.WHITE}. Please Enter A {Fore.BLUE}Valid {Fore.WHITE}Integer.")
    threads = input(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}Hey Buyer, The Previous {Fore.BLUE}Threads {Fore.WHITE}Given Was Not Satisfying, Please Enter {Fore.BLUE}Valid {Fore.WHITE}Amount Of {Fore.BLUE}Threads {Fore.WHITE}To Run {Fore.RED}>>> {Fore.WHITE}')
threadsz = int(threads)
os.system('cls')
import string, random
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
os.system('cls')
ascii_text = '''
                ██╗   ██╗██╗███╗   ██╗████████╗ █████╗  ██████╗ ███████╗
                ██║   ██║██║████╗  ██║╚══██╔══╝██╔══██╗██╔════╝ ██╔════╝
                ██║   ██║██║██╔██╗ ██║   ██║   ███████║██║  ███╗█████╗  
                ╚██╗ ██╔╝██║██║╚██╗██║   ██║   ██╔══██║██║   ██║██╔══╝  
                 ╚████╔╝ ██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗
                  ╚═══╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
'''
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(ascii_text)))
print('')
print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Configurations ->')
print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Mask-Promo:       {Fore.BLUE}{mask_promo}')
print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Print-Invalid:    {Fore.BLUE}{p_inv}')
print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Update-Title:     {Fore.BLUE}{update_ttl}')
print(f'{Fore.WHITE}[{Fore.BLUE}%{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Use-Custom-Proxy: {Fore.BLUE}{u_cus_proxy}')
print('')
print(f'{Fore.WHITE}[{Fore.LIGHTCYAN_EX}@{Fore.WHITE}] {Fore.BLUE}- {Fore.WHITE}Status: {Fore.BLUE}Started.')
print('')

import tls_client
import requests

def get_proxy(protocol='http') -> str|None:
    endpoint = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all"
    
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            proxies = response.text.strip().split('\r\n')
            proxy = random.choice(proxies)
            return proxy
        else:
            return None
    except Exception as e:
        return None
    
class Checker:
    def __init__(self, promo:str) -> None:
        self.full = promo
        if 'promos.discord.gg/' in promo:
            self.code = promo.split('https://promos.discord.gg/')[1]
        elif 'https://discord.com/billing/promotions/' in promo:
            self.code = promo.split('https://discord.com/billing/promotions/')[1]
        else:
            Sprint('-',f'Invalid Promo Type, Note: {Fore.RED}Opera Gx Promos Arent Supported.',Fore.RED)
            return None
        if '-' in self.code:
            self.origin = 'Alienware X Discord'
        else:
            self.origin = 'Xbox Gamepass'
        self.checksession = requests.Session()
        if u_cus_proxy:
            for proxyz in proxy:
              self.checksession.proxies = {
                'https':'http://'+proxyz
            }
        else:
            proxy_scrape = get_proxy()
            if not proxy_scrape == None:
              self.checksession.proxies = {
    'http': 'http://'+proxy_scrape,
    'https': 'http://'+proxy_scrape
}
            else:
                self.checksession.proxies = None
        self.checkurl = f'https://discord.com/api/v9/entitlements/gift-codes/{self.code}?country_code=US&with_application=false&with_subscription_plan=true'
        
    def checkpromo(self) -> bool:
        global fails
        global success
        global ratelimited
        global alr_used
        try:
          self.response = self.checksession.get(self.checkurl)
        except Exception as e:
            Sprint('-',f'Internet Or Proxy Issue. Retrying..., Excp: {Fore.YELLOW}{e}',Fore.RED)
            Checker(self.full).checkpromo()
            return False
        if '"uses"' in self.response.text and self.response.json()["uses"] == 1:
                with open('output/already_used.txt','a') as f:
                    f.write(self.full+'\n')
                Sprint('!',f'Promo Already Used: {Fore.YELLOW}{self.full if not mask_promo else self.code[:15]}.',Fore.RED)
                alr_used += 1
                update_title(f' Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer')
                return False
            
        elif '"uses"' in self.response.text and self.response.json()["uses"] == 0:
                with open('output/valids.txt','a') as f:
                    f.write(self.full+'\n')
                Sprint('+',f'Valid Promo Code: {Fore.GREEN}{self.full if not mask_promo else self.code[:15]}.{Fore.WHITE}',Fore.GREEN)
                success += 1
                update_title(f' Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer')
                return True
        
        elif 'Unknown Gift Code' in self.response.text:
            with open('output/invalid.txt','a') as f:
                f.write(self.full+'\n')
            fails += 1
            update_title(f' Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer')
            if p_inv:
              Sprint('-',f'Invalid Promo Code: {Fore.RED}{self.full if not mask_promo else self.code[:15]}.',Fore.RED)
            else:
                pass
            return False
        
        elif 'rate limited' in self.response.text:
            with open('output/ratelimited.txt','a') as f:
                f.write(self.full+'\n')
            ratelimited += 1
            update_title(f'Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer')
            Sprint('-',f'Ratelimited While Checking, Retrying In 40s...: {Fore.YELLOW}{self.full if not mask_promo else self.code[:15]}.',Fore.YELLOW)
            time.sleep(40)
            Checker(self.full).checkpromo()
            return False
        
        else:
            with open('output/unhandled.txt','a') as f:
                f.write(self.full+'\n')
            fails += 1
            update_title(f' Valid: {success}, Already Used: {alr_used}, Invalid: {fails}, Ratelimited: {ratelimited}, User: Buyer')
            Sprint('?',f'Unhandled Error: {Fore.YELLOW}{self.full if not mask_promo else self.code[:15]}.',Fore.RED)
            return False
from concurrent.futures import ThreadPoolExecutor, as_completed
def proccess(promo: str):
    Checker(promo).checkpromo()

with open('input/promos.txt', 'r', encoding='utf-8') as file:
    promos = file.read().splitlines()

def main():
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=threadsz) as exc:
        futures = [exc.submit(proccess, promo) for promo in promos]

        for future in as_completed(futures):
            future.result()
    print('')
    Sprint('#', f'Completed {Fore.BLUE}Threads{Fore.WHITE}, Checked {len(promos)} Promo(s) In {time.time()-start}s', Fore.BLUE)
    print('')
    Sprint('#', f'Proccessed:   {Fore.BLUE}{len(promos)}', Fore.BLUE)
    Sprint('#', f'Valids:       {Fore.BLUE}{success}', Fore.BLUE)
    Sprint('#', f'Already Used: {Fore.BLUE}{alr_used}', Fore.BLUE)
    Sprint('#', f'Ratelimited:  {Fore.BLUE}{ratelimited}', Fore.BLUE)
    Sprint('#', f'Invalids:     {Fore.BLUE}{fails}', Fore.BLUE)
    print('')
    Sprint('?', f'Press {Fore.BLUE}Enter {Fore.WHITE}To {Fore.BLUE}Exit.',Fore.BLUE)
    input(f'{Style.BRIGHT}{Fore.CYAN}~~')

if __name__ == '__main__':
    main()