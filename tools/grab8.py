import requests
from bs4 import BeautifulSoup

# Define colors
blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def greb(pagee):
    url = f'http://australianway.net/t/{pagee}.html'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        domains = [link['href'][4:].split('<')[0] for link in links if link['href'].startswith('www.')]

        if domains:
            tod = len(domains)
            with open('ressaus.txt', 'a') as file:
                file.write('\n'.join(domains) + '\n')
            with open('ressaus.txt', 'r') as file:
                todd = len(file.readlines())
            print(f"{okegreen}[{red}OK!{okegreen}]{cyan} Found {tod} Domain > Page : {pagee} > Total Di .txt : {todd}")
        else:
            print(f"{okegreen}[{red}-{okegreen}]{red} Error Woy!!")
    else:
        print(f"{okegreen}[{red}-{okegreen}]{red} Error Woy!!")

def banner():
    print("<><><><><><><><><><><><><><><><>")
    print("       Grabber by Chris")
    print("      Priv Domain Grabber")
    print("<><><><><><><><><><><><><><><><>")
    page = int(input("Halaman: "))
    pagenya = int(input("Mau Sampai Halaman: "))
    return page, pagenya

page, pagenya = banner()
for pagee in range(page, pagenya + 1):
    greb(pagee)
