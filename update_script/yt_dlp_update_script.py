import sys
import wx
import platform
import requests
from bs4 import BeautifulSoup

if(platform.system() == "Windows"):
    os = "win64"
elif(platform.system() == "Linux"):
    os = "lin64"

def Update_check():
    # import requests
    # from bs4 import BeautifulSoup

    # res = requests.get('https://github.com/yt-dlp/yt-dlp/releases/latest')

    # soup_data = BeautifulSoup(res.text, 'html.parser')

    # raw = str(soup_data.find_all('h1')).split(">")
    # data = str(raw[1]).split("<")
    # ver = str(data[0]).split(" ")
    # ver_no = ver[1]

    # f = open("update_status.txt")
    # ver_in_file = f.read()

    # if(ver_no == ver_in_file):
    #     print("Version Up to Date")
    # else:
    #     Update()
    pass
        
def Update():

    print("Updating YT-DLP.......")

    if(os == "win64"):
        url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_x86.exe'
        r = requests.get(url, allow_redirects=True)

        open('yt-dlp.exe', 'wb').write(r.content)
    elif(os == "lin64"):
        url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux'
        r = requests.get(url, allow_redirects=True)

        open('yt-dlp_linux', 'wb').write(r.content)
    
    print("Update Complete!!")

Update_check()