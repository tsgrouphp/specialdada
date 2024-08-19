import requests
from bs4 import BeautifulSoup

blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def greb():
    apinya = []
    url = f"https://www.statbig.com/s/{huruf}/{pagee}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            apinya.append(link.get_text())
        apinya = list(set(apinya))
        tod = len(apinya)
        with open('../ress.txt', 'a') as file:
            for domain in apinya:
                file.write(domain + '\n')
        with open('../ress.txt', 'r') as file:
            todd = len(file.readlines())
        print(f"{okegreen}[{red}OK!{okegreen}]{cyan} Found {tod} Domain > Page: {pagee} > Total in .txt: {todd}")
    else:
        print(f"{okegreen}[{red}-{okegreen}]{red} Error Woy!!")

def banner():
    print(f"{okegreen} <><><><><><><><><><><><><><><><>")
    print(f"{cyan}       Grabber by Chris")
    print(f"{cyan}      Priv Domain Grabber")
    print(f"{okegreen} <><><><><><><><><><><><><><><><>")
    print()
    print(f"{white}Masukkan Angka 1-353")
    print(f"{white}Contoh: Angka: => 1")
    print()
    global huruf
    global page
    global pagenya
    huruf = input("Angka: => ")
    page = int(input("Page: "))
    pagenya = int(input("Mau Page Berapa (Max 1000): "))

banner()
for pagee in range(page, pagenya + 1):
    greb()