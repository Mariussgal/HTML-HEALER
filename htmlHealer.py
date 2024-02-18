import re
from bs4 import BeautifulSoup
from colorama import Fore, Style 
import sys
import textwrap
from tqdm import tqdm
import time
import shutil

columns, rows = shutil.get_terminal_size()

for i in tqdm(range(100), desc=f"{Fore.GREEN}Processing{Style.RESET_ALL}", unit="step"):
    time.sleep(0.01) 

SELF_CLOSED_TAG = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

def load_html_as_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as fichier:
            return fichier.read()
    except IOError as e: 
        print(f"{Fore.RED}Error opening file: {e}{Style.RESET_ALL}")
        sys.exit(1)

def find_unclosed_tag(html_text):    
    open_tag = re.findall(r'<([a-zA-Z]+)(\s+[^>]*)?>', html_text)
    closed_tag = re.findall(r'</([a-zA-Z]+)>', html_text)

    open_tag_dict = {}
    
    for tag, _ in open_tag:
        if tag not in SELF_CLOSED_TAG:  
            if tag not in open_tag_dict:
                open_tag_dict[tag] = 0  
            open_tag_dict[tag] += 1  
    
    for tag in closed_tag:
        if tag in open_tag_dict:
            open_tag_dict[tag] -= 1
  
    unclosed_tag = {tag: count for tag, count in open_tag_dict.items() if count > 0}
    return unclosed_tag


def find_missing_images_and_obsolete_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    missing_images = [img for img in soup.find_all('img') if not img.get('src')]
    obsolete_tags = ['applet','center', 'acronym', 'bgsound', 'dir', 'frame', 'frameset', 'noframes', 'isindex', 'listing', 'xmp']
    obsoletes_found = []
    for tag in obsolete_tags:
        if soup.find_all(tag):
            obsoletes_found.append(tag)
    return missing_images, obsoletes_found

def analyze_html(html_file_path):
    html_content = load_html_as_text(html_file_path)
    errors_tags = find_unclosed_tag(html_content)
    missing_images, obsolete_tags = find_missing_images_and_obsolete_tags(html_content)
    return errors_tags, missing_images, obsolete_tags

html_file_path = input(f"{Fore.CYAN}\nEnter the path of the HTML file : {Style.RESET_ALL} ")
errors_tags, missing_images, obsolete_tags = analyze_html(html_file_path)

if errors_tags:
    print(f"{Fore.YELLOW}\nUnclosed or malformed tags:{Style.RESET_ALL}")
    for tag, count in errors_tags.items():
        print(f" - {tag}: {count} tag(s) unclosed")
else:
    print(f"{Fore.GREEN}\nNo unclosed or malformed tags detected.{Style.RESET_ALL}")

if missing_images:
    print(f"{Fore.YELLOW}\nMissing images (empty or missing src attribute) :{Style.RESET_ALL}")
    for img in missing_images:
        img_str = str(img)
        wrapped_img = "\n".join(textwrap.wrap(img_str, width=70))
        print(f" - {wrapped_img}")
else:
    print(f"{Fore.GREEN}\nNo missing images detected.{Style.RESET_ALL}")

if obsolete_tags:
    print(f"{Fore.YELLOW}\nObsolete tags used:{Style.RESET_ALL}")
    for tag in obsolete_tags:
        print(f" - {tag}")
else:
    print(f"{Fore.GREEN}\nNo obsolete tags detected.{Style.RESET_ALL}")

print("\n\n/!\Analysis completed/!\.")
print("-" * columns)
print(f"{Fore.CYAN}\n\x1B[3mcreated by Marius GAL.\x1B[3m{Style.RESET_ALL}")
