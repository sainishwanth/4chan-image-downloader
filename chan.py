import urllib.request
import requests
import os
from bs4 import BeautifulSoup
import random

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
while True:
    path = input("\nEnter Path: ")if int(input("1 for Custom path\n2 For Current Path: ")) == 1 else os.getcwd();
    if os.path.exists(path):
        break
    else:
        print("Directory does not exist")
file_ext_types = ['png', 'jpg', 'jpeg', 'gif', 'tiff']
url = input("Enter URL to 4chan thread: ")
page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
ThreadName = soup.find("span", class_= "subject").get_text().strip()
if ThreadName == "":
    ThreadName = f"Thread_{random.randint(0,100000)} "
ThreadName = ThreadName.replace(" ", "_")

print(f"Thread Name - {ThreadName}\n")

try:
    os.mkdir(f"{path}/{ThreadName}") #Unix
    path = f"{path}/{ThreadName}"
except:
    os.mkdir(f"{path}\{ThreadName}") #Winbloat
    path = f"{path}\{ThreadName}"

print(path)

count = 0
for a in soup.find_all('a', class_="fileThumb", href=True):
    print(f"Image Count {count}")
    count += 1
    img = f"https:{a['href']}"
    file_ext = img[-3:]
    if file_ext not in file_ext_types:
        print("Unsupported File Extension")
        continue
    filename = f"{ThreadName}_{count}.{file_ext}"
    print(filename)
    urllib.request.urlretrieve(img, f"{path}/{filename}")
