import urllib.request
import requests
import os
import random
import sys
from bs4 import BeautifulSoup

#Globals
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
file_ext_types = ['png', 'jpg', 'jpeg', 'gif', 'tiff']

# Getting Thread Name
def getThreadName(soup):
    ThreadName = soup.find("span", class_= "subject").get_text().strip()
    if ThreadName == "":
        ThreadName = f"Thread_{random.randint(0,100000)} "
    ThreadName = ThreadName.replace(" ", "_")
    ThreadName = ThreadName.replace("/","_")
    ThreadName = ThreadName.replace("'\'","-")
    return ThreadName

# getting path
def getPath():
    while True:
        path = input("\nEnter Path: ")if int(input("1 for Custom path\n2 For Current Path: ")) == 1 else os.getcwd()
        if os.path.exists(path):
            break
        else:
            print("Directory does not exist")
    return path

# Downloading Images
def downloadImage(img, filename,path):
    urllib.request.urlretrieve(img, f"{path}/{filename}")
    print(filename)

# Start Point
def main():
    global header, file_ext_types
    url = input("Enter URL to 4chan thread: ")
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    ThreadName = getThreadName(soup)
    path = getPath()
    print(f"Thread Name - {ThreadName}\n")
    try:
        if os.path.exists(f"{path}/{ThreadName}"):
            sys.exit("Path Already Exists")
        os.mkdir(f"{path}/{ThreadName}") #Unix
        path = f"{path}/{ThreadName}"
    except:
        if os.path.exists(f"{path}\{ThreadName}"):
            sys.exit("Path Already Exists")
        os.mkdir(f"{path}\{ThreadName}") #Winbloat
        path = f"{path}\{ThreadName}"
    print(f"Saving to: {path}")
    count = 0
    for a in soup.find_all('a', class_="fileThumb", href=True):
        img = f"https:{a['href']}"
        file_ext = img[-3:]
        if file_ext not in file_ext_types:
            print("Unsupported File Extension")
            continue
        filename = f"{ThreadName}_{count}.{file_ext}"
        count += 1
        downloadImage(img, filename, path)
    print("Done..")

if __name__ == "__main__":
    main()
