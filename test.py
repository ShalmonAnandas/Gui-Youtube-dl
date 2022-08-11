import os
import platform
from pathlib import Path
import sys


update_status_path = os.path.join('update_script', 'update_status.txt')
print(update_status_path)
os.system("yt-dlp.exe -U > " + update_status_path)

