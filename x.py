import os
import subprocess
from colorama import Fore, Back, Style, init
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PTStyle
import time
import sys

init(autoreset=True)

pt_style = PTStyle.from_dict({
    'prompt': 'bg:ansiblue fg:white bold',
})

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message, duration=2):
    for i in range(duration):
        sys.stdout.write(f"\r{message} ⣾")
        time.sleep(0.1)
        sys.stdout.write(f"\r{message} ⣽")
        time.sleep(0.1)
        sys.stdout.write(f"\r{message} ⣻")
        time.sleep(0.1)
        sys.stdout.write(f"\r{message} ⢿")
        time.sleep(0.1)
    sys.stdout.write(f"\r{message} - Done!\n")

def remove_duplicates(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        unique_lines = list(set(lines))
        
        with open(output_file, 'w') as file:
            file.writelines(unique_lines)
        
        print(Fore.GREEN + f"Duplicate entries removed. Output saved to {output_file}")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def print_menu():
    clear_screen()

    print(Fore.RED + " ██████╗██╗  ██╗██████╗ ██╗███████╗    ██████╗  ██████╗ ████████╗".replace('█', '▒'))
    print(Fore.RED + "██╔════╝██║  ██║██╔══██╗██║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝".replace('█', '▒'))
    print(Fore.YELLOW + "██║     ███████║██████╔╝██║███████╗    ██████╔╝██║   ██║   ██║   ".replace('█', '▒'))
    print(Fore.YELLOW + "██║     ██╔══██║██╔══██╗██║╚════██║    ██╔══██╗██║   ██║   ██║   ".replace('█', '▒'))
    print(Fore.GREEN + "╚██████╗██║  ██║██║  ██║██║███████║    ██████╔╝╚██████╔╝   ██║   ".replace('█', '▒'))
    print(Fore.GREEN + " ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ".replace('█', '▒'))

    print(Fore.WHITE + "coded by:t.me/CHRIScvx")

    print(Back.RED + Fore.WHITE + Style.BRIGHT + "\nMAIN MENU")
    print(Fore.RED + "1. AutoXploiter Bot")
    print(Fore.RED + "2. Splitter+Auto Run (Good For Big List)")
    print(Fore.RED + "3. Perlalfa scan+Auto upload")
    print(Fore.RED + "4. Phpunit scan+Auto upload")
    print(Fore.RED + "5. WP-CVE-2023-5630 scan+Auto upload")
    print(Fore.RED + "6. Subfinder V2 (Good Result)")

    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + "\nGRABBER MENU")
    print(Fore.GREEN + "7. Grab By Ext")
    print(Fore.GREEN + "8. Zone Xsec Grabber")
    print(Fore.GREEN + "9. Haxorid Grabber")
    print(Fore.GREEN + "10. Grabber By KeyWord")
    print(Fore.GREEN + "11. Grabber By Page V1")
    print(Fore.GREEN + "12. Grabber By A-Z 0-9")
    print(Fore.GREEN + "13. Grab Domain Per Sec")
    print(Fore.GREEN + "14. Grabber By Page V2")
    print(Fore.GREEN + "15. Grabber By Angka")

    print(Back.YELLOW + Fore.WHITE + Style.BRIGHT + "\nOTHER MENU")
    print(Fore.YELLOW + "16. Mass Subdomain Finder")
    print(Fore.YELLOW + "17. Mass Reverse Ip")
    print(Fore.YELLOW + "18. CMS Scanner")
    print(Fore.YELLOW + "19. Remove Duplicate")
    print(Fore.YELLOW + "20. Brute Force Password Webshell")

def main_menu():
    while True:
        print_menu()
        choice = prompt('PILIH MENU: ', style=pt_style)

        if choice == '1':
            current_directory = os.path.dirname(os.path.abspath(__file__))
            file_name = input("list: ")
            file_path = os.path.join(current_directory, file_name)
            if os.path.isfile(file_path):
                os.chdir('tools')
                os.system(f"python rsf.py {file_path}")
                os.chdir(current_directory)
            else:
                print(Fore.RED + f"File {file_name} tidak ditemukan.")
        elif choice == '2':
            tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
            split_script = os.path.join(tools_directory, 'split.py')
            
            if os.path.isfile(split_script):
                loading_animation("Running split.py")
                subprocess.run(['python', split_script], cwd=tools_directory)
            else:
                print(Fore.RED + "error tools")
        elif choice == '3':
            tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
            grab1_script = os.path.join(tools_directory, 'perlalfa.py')
            
            if os.path.isfile(grab1_script):
                loading_animation("Running perlalfa.py")
                subprocess.run(['python', grab1_script], cwd=tools_directory)
            else:
                print(Fore.RED + "error tools")
        elif choice == '4':
            tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
            subfind_script = os.path.join(tools_directory, 'phpunit.py')
            
            if os.path.isfile(subfind_script):
                loading_animation("Running phpunit.py")
                subprocess.run(['python', subfind_script], cwd=tools_directory)
            else:
                print(Fore.RED + "error tools")
        elif choice == '5':
            tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
            rev_script = os.path.join(tools_directory, 'wp.py')
            
            if os.path.isfile(rev_script):
                loading_animation("Running wp.py")
                subprocess.run(['python', rev_script], cwd=tools_directory)
            else:
                print(Fore.RED + "error tools")
        elif choice in ['6', '7', '8', '9', '10']:
            grabber_submenu(choice)
        elif choice in ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']:
            other_submenu(choice)
        else:
            print(Fore.RED + "Pilihan tidak valid.")
            print(Style.RESET_ALL)

def grabber_submenu(choice):
    tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
    
    if choice == '6':
        if os.name == 'nt':
            go_installed = subprocess.call(["where", "go"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
        else:
            go_installed = subprocess.call(["which", "go"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0
        
        if go_installed:
            print(Fore.GREEN + "Go sudah terinstal.")
            subprocess.run(["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"])
            list_name = input("Masukkan nama list: ")
            output_name = input("Masukkan nama output: ")
            subprocess.run(["subfinder", "-dL", list_name, "-o", output_name])
        else:
            print(Fore.RED + "Golang belum terinstal. Silahkan instal Golang terlebih dahulu.")
    elif choice == '7':
        grab3_script = os.path.join(tools_directory, 'grab1.py')
        
        if os.path.isfile(grab3_script):
            loading_animation("Running grab1.py")
            subprocess.run(['python', grab3_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '8':
        grab4_script = os.path.join(tools_directory, 'zonexsec.py')
        
        if os.path.isfile(grab4_script):
            loading_animation("Running zonexsec.py")
            subprocess.run(['python', grab4_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '9':
        grab5_script = os.path.join(tools_directory, 'haxorid.py')
        
        if os.path.isfile(grab5_script):
            loading_animation("Running haxorid.py")
            subprocess.run(['python', grab5_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '10':
        grab6_script = os.path.join(tools_directory, 'grab2.py')
        
        if os.path.isfile(grab6_script):
            loading_animation("Running grab2.py")
            subprocess.run(['python', grab6_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    else:
        print(Fore.RED + "Pilihan tidak valid.")
        print(Style.RESET_ALL)

def other_submenu(choice):
    tools_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools')
    
    if choice == '11':
        grab7_script = os.path.join(tools_directory, 'grab3.py')
        
        if os.path.isfile(grab7_script):
            loading_animation("Running grab3.py")
            subprocess.run(['python', grab7_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '12':
        perlalfa_script = os.path.join(tools_directory, 'grab4.py')
        
        if os.path.isfile(perlalfa_script):
            loading_animation("Running grab4.py")
            subprocess.run(['python', perlalfa_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '13':
        phpunit_script = os.path.join(tools_directory, 'grab5.py')
        
        if os.path.isfile(phpunit_script):
            loading_animation("Running grab5.py")
            subprocess.run(['python', phpunit_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '14':
        grabberbypagev2_script = os.path.join(tools_directory, 'grab6.py')
        
        if os.path.isfile(grabberbypagev2_script):
            loading_animation("Running grab6.py")
            subprocess.run(['python', grabberbypagev2_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '15':
        grabberbyangka_script = os.path.join(tools_directory, 'grab7.py')
        
        if os.path.isfile(grabberbyangka_script):
            loading_animation("Running grab7.py")
            subprocess.run(['python', grabberbyangka_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '16':
        wp_script = os.path.join(tools_directory, 'subfind.py')
        
        if os.path.isfile(wp_script):
            loading_animation("Running subfind.py")
            subprocess.run(['python', wp_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '17':
        cmsscan_script = os.path.join(tools_directory, 'rev.py')
        
        if os.path.isfile(cmsscan_script):
            loading_animation("Running rev.py")
            subprocess.run(['python', cmsscan_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '18':
        grab7_script = os.path.join(tools_directory, 'cmsscan.py')
        
        if os.path.isfile(grab7_script):
            loading_animation("Running cmsscan.py")
            subprocess.run(['python', grab7_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    elif choice == '19':
        input_file = input("Input file: ")
        output_file = input("Output file: ")
        remove_duplicates(input_file, output_file)
    elif choice == '20':
        grab7_script = os.path.join(tools_directory, 'bfpass.py')
        
        if os.path.isfile(grab7_script):
            loading_animation("Running bfpass.py")
            subprocess.run(['python', grab7_script], cwd=tools_directory)
        else:
            print(Fore.RED + "error tools")
    else:
        print(Fore.RED + "Pilihan tidak valid.")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()