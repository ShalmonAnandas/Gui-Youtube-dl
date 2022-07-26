import sys
import wx
import platform
import requests

if(platform.system() == "Windows"):
    os = "win64"
elif(platform.system() == "Linux"):
    os = "lin64"

def Update_check():
    response = requests.get('https://github.com/yt-dlp/yt-dlp/releases/latest/')
    
    
def Update():

    if(os == "win64"):
        url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_x86.exe'
        r = requests.get(url, allow_redirects=True)

        open('yt-dlp.exe', 'wb').write(r.content)
    elif(os == "lin64"):
        url = 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux'
        r = requests.get(url, allow_redirects=True)

        open('yt-dlp_linux', 'wb').write(r.content)