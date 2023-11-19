import os 
import threading
import requests, random
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Alex's Group Finder")


def groupfinder():
    id = random.randint(1000000, 3200000)
    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'Hit: https://www.roblox.com/groups/group.aspx?gid={id}')
                print(f"[+] Hit: {id}")
            else:
                print(f"[-] No Entry Allowed: {id}")
        else:
            print(f"[-] Group Locked: {id}")
    else:
        print(f"[-] Group Already Owned: {id}")



#your webhook
hook = input("[-] Enter your webhook url: https://discord.com/api/webhooks/1175850510226555011/MhwsErwSqdyDi-71XQLpWwrPZZUwIcE-BO_s1oBZuBVY8U8DKwdRx02vKRr03GY6yWNw"))
#number of threads
threads = int(input("[-] How many threads: 1000"))

while True:
    if threading.active_count() <= threads:
        threading.Thread(target=groupfinder).start()
