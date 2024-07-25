import os
import sys
sys.path.insert(1, 'gui_files')

import noname
batch_file = os.path.join('multi_download_files', 'batch_file.txt')

def multi_audio_dl(self, event):
    link = batch_file
    directory: str = self.m_dirPicker1.GetPath()
    cookies: str = self.cookie_picker.GetPath()
    args: str =  self.custom_args.GetValue()

    os.system(
            'yt-dlp -x --audio-format mp3 --audio-quality 2 --cookies '
            + cookies
            + ' -a '
            + link
            + ' -o \"'
            + directory
            + '/%(title)s-%(id)s-audio.%(ext)s" '
            + args
            )
    