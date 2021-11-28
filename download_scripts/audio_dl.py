import os
import sys
sys.path.insert(1, 'gui_files')

import noname

def audio_dl_func(self, event):
    link: str = self.m_textCtrl5.GetValue()
    directory: str = self.m_dirPicker5.GetPath()
    
    os.system(
            "yt-dlp -f bestaudio "
            + link
            + " -o \""
            + directory
            + '/%(title)s-%(id)s-2160p.%(ext)s" '
            )
