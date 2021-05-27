# GUIYoutube-dl
An easy Gui to download videos and an even easy clipper!
A cross platform GUI for youtube-dl written entirely in python using the WX library.

<img src='https://github.com/Shalmon123/GUIYoutube-dl/blob/main/gui v2.0.png?raw=true'>

## Installation:
### Windows:
1) Download the Zip from releases
2) Unzip and run youtube-dl-gui.exe

### Linux:
1) Download the linux.zip from releases.
2) Extract and run "youtube-dl-gui"

### Build Instructions:
1) Install [Python](https://www.python.org/downloads/)
2) Install wxPython `pip install wxpython`
3) Install pyinstaller `pip install pyinstaller`
4) Install [Git](https://git-scm.com/downloads)
5) Clone the github repo `git clone https://github.com/ShalmonAnandas/Gui-Youtube-dl`
6) Make a new folder named "Build-Gui-Youtube-dl" anywhere on your computer.
7) In the cloned folder open a Cmd of powershell window and execute `pyinstaller youtube-dl-gui.py`
8) Move the contents of the "dist" folder that was just created automatically, into the "Build-Gui-Youtube-dl" folder
9) In the "youtube_dl" folder present open a cmd or powerhell window and execute `pyinstaller __main__.py`
10) Now Move the entire "youtube_dl" folder into the "Build-Gui-Youtube-dl" folder
11) You will also need to install ffmpeg to use the clipping feature and to download in higher resolutions.

## Usage:
1) To use the clipping feature you just have to type in the timestamp of the part you want to download like shown in the gui Itself.

