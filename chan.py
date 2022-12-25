import urllib.request
import requests
import os
import random
import sys
from bs4 import BeautifulSoup
from prettytable import PrettyTable
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

# Return a List containing Thread Names in a particular board
def getThreadList(url_list: list) -> list:
    thread_list = []
    for url in url_list:
        soup = getSoup(url)
        ThreadName = soup.find("span", class_= "subject").get_text().strip()
        if ThreadName == "":
            print("Recieved an Anonymous Thread..Naming it Randomly..") # Anonymous threads have blank text so replacing them with Text in the format of -> "Anonymous" + str(randomNumber)
            ThreadName = f"Anonymous_{random.randint(0,100000)} "
        # Thread Name cannot contain special characters such as -> '\' or '/' 
        # When creating a directory with these thread names, os library will create new directories if it enocunters a '\' or '/'
        # Replacing them with a blank char instead
        # Having spacing can cause weird file names so replacing those too.
        ThreadName = ThreadName.replace(" ", "")
        ThreadName = ThreadName.replace("/","")
        ThreadName = ThreadName.replace("'\'","")
        thread_list.append(ThreadName)
    return thread_list

# Returns Absolute path (Specific to your OS) 
def getPath(ThreadName: str) -> str:
    global glob_path
    path = os.path.abspath(f"{glob_path}/{ThreadName}")
    if os.path.exists(path):                                            # Checking if path already exists -> User is trying to re-download the same thread (Same Name at least) to the same directory as before.
        sys.exit("Path Already Exists, Please delete or update it...")
    print(f"Saving to: {path}")
    return path

# Downloading Images
def downloadImage(url_list: list, thread_list: list) -> None:
    for url, thread in zip(url_list, thread_list):
        soup = getSoup(url)
        path = getPath(thread)
        print(f"Making a dir for {thread}...")
        os.mkdir(path)
        count = 0
        for a in soup.find_all('a', class_="fileThumb", href=True):   # Finding all href's with the class "fileThumb" -> ID for images under a thread in 4chan
            img = f"https:{a['href']}"
            file_ext = img[-3:]                                       # Extracting the File Extension (Last 3 chars in a string)
            if file_ext not in ['png', 'jpg', 'jpeg', 'gif', 'tiff']: # Checking for un-supported File Extensions
                print("Unsupported File Extension")
                continue
            filename = f"{thread}_{count}.{file_ext}"
            print(f"Saving Images {filename}")
            urllib.request.urlretrieve(img, os.path.abspath(f"{path}/{filename}"))
            count += 1
        print(f"Finished {thread}..")
    print("Done..")

#Returns a List of URL's to all threads in a board (avilable on that page)
def getUrl_List(url: str, soup: BeautifulSoup) -> list:
    spans = soup.find_all("span", {"class": "summary"})     # Finding all spans with the class "summary" -> ID for Thread Expansion Button in 4chan        
    url_list = []                                            
    for span in spans:                                      
        links = span.find_all('a')
        for link in links:                                  
            url_list.append(f"{url}{link['href']}")         # Appending all href's (Under the span) to a list of URL
    return url_list

# Function to get a soup Object for a specific URL
def getSoup(url: str) -> BeautifulSoup:
    global header
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def main():
    url = input("Enter a URL or a board name (g,v,h): ")
    if len(url) == 1:
        url = f"https://boards.4channel.org/{url}/"
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    url_list = getUrl_List(url, soup)
    if not url_list:                                        # Checking if user has given a thread
        print("Received a Single Thread Link..")
        url_list.append(url)                                # Appending the only url to the url (since its empty)
    thread_list = getThreadList(url_list)                   # Generating Thread Names from the list of URLs
    table = PrettyTable(['URL', 'Thread'])                  #Creating a table to format the output better
    for url, thread in zip(url_list, thread_list):
        table.add_row([url, thread])
    print(table) 
    downloadImage(url_list, thread_list)                    # Downloading Images starts here

if __name__ == '__main__':
    count = 1
    print("Save Dir (Sub Folders with appropriate thread names will be created. Only Mention Parent Directory)..\n")
    while count < 4:
        glob_path = input("\nEnter Path: ")if int(input("1 for Custom path\n2 For Current Path: ")) == 1 else os.getcwd()
        if os.path.exists(glob_path):
            main()
            sys.exit("Exiting Successfully..") # Exiting after Completion
        else:
            count += 1 # Counting User Error
        print(f"\nTry [{count}] - Directory does not exist, Try Again..")
    sys.exit("Exceeded 3 Tries, Please Verify Your Paths and Retry") # Exiting if Error rate == 3
