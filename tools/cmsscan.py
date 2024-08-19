import sys
import os
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore, init
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

print("""
  [#] Created By :: Chris Bot
""")

try:
    script_dir = os.path.dirname(__file__)
    # Mendapatkan direktori di atasnya
    parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
    
    cms_dir = os.path.join(parent_dir, 'cms')
    if not os.path.exists(cms_dir):
        os.makedirs(cms_dir)
    
    url_file = input("Masukkan list: ")
    
    list_file = os.path.join(parent_dir, url_file)
    
    if not os.path.isfile(list_file):
        exit('\n  [!] File "{}" not found.'.format(list_file))
    
    with open(list_file, mode='r') as f:
        target = [i.strip() for i in f.readlines()]
    
    if not target:
        exit('\n  [!] No URLs found in the file: ' + list_file)

except Exception as e:
    exit('\n  [!] Error: {}'.format(e))


def URL(url):
    if url[-1] == "/":
        pattern = re.compile('(.*)/')
        site = re.findall(pattern, url)
        url = site[0]
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url


def filter(site):
    pet = re.compile('<meta name="generator" content="(.*)" />')
    try:
        site = URL(site)
        
        src = requests.get(site, timeout=15, verify=False).content.decode('utf-8', 'ignore')
        
        if re.findall(pet, src):
            generator = re.findall(pet, src)[0]
            if 'WordPress' in generator:
                print(' --| ' + site + ' --> {}[WordPress]'.format(fg))
                with open(os.path.join(cms_dir, 'wordpress.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'Joomla' in generator:
                print(' --| ' + site + ' --> {}[Joomla]'.format(fg))
                with open(os.path.join(cms_dir, 'joomla.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'Drupal' in generator:
                print(' --| ' + site + ' --> {}[Drupal]'.format(fg))
                with open(os.path.join(cms_dir, 'drupal.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'PrestaShop' in generator:
                print(' --| ' + site + ' --> {}[PrestaShop]'.format(fg))
                with open(os.path.join(cms_dir, 'prestashop.txt'), mode='a') as d:
                    d.write(site + '/\n')
            else:
                if 'wp-content/themes' in src:
                    print(' --| ' + site + ' --> {}[WordPress]'.format(fg))
                    with open(os.path.join(cms_dir, 'wordpress.txt'), mode='a') as d:
                        d.write(site + '/\n')
                elif 'catalog/view/theme' in src:
                    print(' --| ' + site + ' --> {}[OpenCart]'.format(fg))
                    with open(os.path.join(cms_dir, 'opencart.txt'), mode='a') as d:
                        d.write(site + '/\n')
                elif 'sites/all/themes' in src:
                    print(' --| ' + site + ' --> {}[Drupal]'.format(fg))
                    with open(os.path.join(cms_dir, 'drupal.txt'), mode='a') as d:
                        d.write(site + '/\n')
                elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src:
                    print(' --| ' + site + ' --> {}[Joomla]'.format(fg))
                    with open(os.path.join(cms_dir, 'joomla.txt'), mode='a') as d:
                        d.write(site + '/\n')
                elif 'js/jquery/plugins/' in src:
                    print(' --| ' + site + ' --> {}[PrestaShop]'.format(fg))
                    with open(os.path.join(cms_dir, 'prestashop.txt'), mode='a') as d:
                        d.write(site + '/\n')
                else:
                    print(' --| ' + site + ' --> {}[Other]'.format(fr))
                    with open(os.path.join(cms_dir, 'other.txt'), mode='a') as d:
                        d.write(site + '/\n')
        else:
            if 'wp-content/themes' in src:
                print(' --| ' + site + ' --> {}[WordPress]'.format(fg))
                with open(os.path.join(cms_dir, 'wordpress.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'catalog/view/theme' in src:
                print(' --| ' + site + ' --> {}[OpenCart]'.format(fg))
                with open(os.path.join(cms_dir, 'opencart.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'sites/all/themes' in src:
                print(' --| ' + site + ' --> {}[Drupal]'.format(fg))
                with open(os.path.join(cms_dir, 'drupal.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif '<script type="text/javascript" src="/media/system/js/mootools.js"></script>' in src or '/media/system/js/' in src or 'com_content' in src:
                print(' --| ' + site + ' --> {}[Joomla]'.format(fg))
                with open(os.path.join(cms_dir, 'joomla.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'js/jquery/plugins/' in src:
                print(' --| ' + site + ' --> {}[PrestaShop]'.format(fg))
                with open(os.path.join(cms_dir, 'prestashop.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'osCommerce' in src:
                print(' --| ' + site + ' --> {}[osCommerce]'.format(fg))
                with open(os.path.join(cms_dir, 'osCommerce.txt'), mode='a') as d:
                    d.write(site + '/\n')
            elif 'index.php?osCsid=' in src or 'index.php/cPath' in src:
                print(' --| ' + site + ' --> {}[osCommerce]'.format(fg))
                with open(os.path.join(cms_dir, 'osCommerce.txt'), mode='a') as d:
                    d.write(site + '/\n')
            else:
                print(' --| ' + site + ' --> {}[Other]'.format(fr))
                with open(os.path.join(cms_dir, 'other.txt'), mode='a') as d:
                    d.write(site + '/\n')
    except requests.exceptions.RequestException as e:
        print(' --| ' + site + ' --> {}[Error: {}]'.format(fr, e))


mp = Pool(150)
mp.map(filter, target)
mp.close()
mp.join()