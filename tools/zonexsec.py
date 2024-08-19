import requests
from bs4 import BeautifulSoup
import re
import os

def is_valid_domain(domain):
    if len(domain) >= 5 and not re.search(r'\.{3,}$', domain) and not domain.endswith('.'):
        return True
    return False

def scrape_zone_xsec(category, page_number):
    base_url = f'https://zone-xsec.com/{category}/page={page_number}'
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        domains = []
        rows = soup.find_all('tr')
        for row in rows:
            if row.find('th'):  # Skip rows with <th> elements
                continue
            tds = row.find_all('td')
            if len(tds) > 9:  # Ensure there are at least 10 <td> elements to find mirror link
                mirror_link = tds[9].find('a', href=re.compile(r'/mirror/id/\d+'))
                if mirror_link:
                    mirror_url = 'https://zone-xsec.com' + mirror_link['href']
                    mirror_response = requests.get(mirror_url)
                    if mirror_response.status_code == 200:
                        mirror_soup = BeautifulSoup(mirror_response.content, 'html.parser')
                        title_tag = mirror_soup.find('title')
                        if title_tag:
                            title_text = title_tag.text.strip()
                            match = re.search(r'Defacement Details of (.+)', title_text)
                            if match:
                                valid_domain = match.group(1)
                                # Remove text after '/'
                                valid_domain = re.sub(r'\/.*$', '', valid_domain)
                                if is_valid_domain(valid_domain):
                                    domains.append(valid_domain)
            else:
                domain_text = tds[-2].text.strip()  # Get second-to-last <td> element for domain
                if domain_text.endswith('.'):
                    continue  # Skip domains ending with dot
                if is_valid_domain(domain_text):
                    domains.append(domain_text)
        
        return domains
    else:
        print(f'Failed to fetch page {page_number}. Status code: {response.status_code}')
        return []

def save_to_file(domains, page_number, category):
    parent_dir = '../'
    filename = os.path.join(parent_dir, f'{category}.txt')
    with open(filename, 'a', encoding='utf-8') as file:
        for domain in domains:
            file.write(domain + '\n')
    print(f'Got {len(domains)} domains from page {page_number}')

def menu():
    print("coded by: t.me/CHRIScvx")
    print("1. Grab by onhold")
    print("2. Grab by special")
    print("3. Grab by archive")
    print("4. Exit")
    
    choice = input("Choose: ").strip()
    
    if choice == '1':
        category = 'onhold'
    elif choice == '2':
        category = 'special'
    elif choice == '3':
        category = 'archive'
    elif choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter a valid option.")
        menu()
        return
    
    start_page = int(input('From page: '))
    end_page = int(input('To page (max 50): '))
    
    for page_number in range(start_page, min(end_page + 1, 51)):
        scraped_domains = scrape_zone_xsec(category, page_number)
        if scraped_domains:
            save_to_file(scraped_domains, page_number, category)
        else:
            print(f'No domains retrieved from page {page_number}.')
    
    print('Scraping process completed.')

if __name__ == "__main__":
    menu()
