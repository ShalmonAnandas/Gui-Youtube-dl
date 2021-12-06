import os
import sys
sys.path.insert(1, 'gui_files')

import noname

def audio_dl_func(self, event):
    link: str = self.m_textCtrl5.GetValue()
    directory: str = self.m_dirPicker5.GetPath()
    cookies: str = self.cookie_picker.GetPath()
    args: str =  self.custom_args.GetValue()
    
    os.system(
            'yt-dlp -x --audio-format mp3 --audio-quality 2 --cookies '
            + cookies
            + ' '
            + link
            + ' -o \"'
            + directory
            + '/%(title)s-%(id)s-audio.%(ext)s" '
            + args
            )
