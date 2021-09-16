# GUIYoutube-dl
An easy Gui to download videos and an even easy clipper!
A cross platform GUI for youtube-dl written entirely in python using the WX library.

<img src='https://github.com/Shalmon123/GUIYoutube-dl/blob/main/gui v2.0.png?raw=true'>

## Installation:
### Windows:
- Download the win64.zip from releases
- Unzip and run youtube-dl-gui.exe

### Linux:
- Download the linux.tar.xz from releases.
- Extract and run "youtube-dl-gui"

### Build Instructions:
- Install [Python](https://www.python.org/downloads/)
- Install wxPython `pip install wxpython`
- Install pyinstaller `pip install pyinstaller`
- Install [Git](https://git-scm.com/downloads)
- Clone the github repo `git clone https://github.com/ShalmonAnandas/Gui-Youtube-dl`
- Make a new folder named "Build-Gui-Youtube-dl" anywhere on your computer.
- In the cloned folder open a Cmd of powershell window and execute `pyinstaller youtube-dl-gui.py`
- Move the contents of the "dist" folder that was just created automatically, into the "Build-Gui-Youtube-dl" folder
- In the "youtube_dl" folder present open a cmd or powerhell window and execute `pyinstaller __main__.py`
- Now Move the entire "youtube_dl" folder into the "Build-Gui-Youtube-dl" folder
- You will also need to install ffmpeg to use the clipping feature and to download in higher resolutions.

## Usage:
- To use the clipping feature you just have to type in the timestamp of the part you want to download like shown in the gui Itself.

## Known Bugs:
- If the git cloned version dosent run on linux with error 'r/python does not exist' run 'fix.py' and it should work.

