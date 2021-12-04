import os
import sys
sys.path.insert(1, 'gui_files')

import noname
batch_file = os.path.join('multi_download_files', 'batch_file.txt')

def multi_video_dl(self, event):
    link = batch_file
    directory: str = self.m_dirPicker1.GetPath()
    cookies: str = self.cookie_picker.GetPath()
    args: str =  self.custom_args.GetValue()
    
    if self.m_comboBox1.GetSelection() == 0:
        os.system(
                'yt-dlp -f "best[height=2160]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-2160p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 1:
        os.system(
                'yt-dlp -f "best[height=1440]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-1440p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 2:
        os.system(
                'yt-dlp -f "best*[height=1080]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-1080p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 3:
        os.system(
                'yt-dlp -f "best*[height=720]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-720p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 4:
        os.system(
                'yt-dlp -f "best*[height=480]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-480p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 5:
        os.system(
                'yt-dlp -f "best*[height=360]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-360p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 6:
        os.system(
                'yt-dlp -f "best*[height=240]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-240p.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 7:
        os.system(
                'yt-dlp -f "best*[height=144]+bestaudio" '
                + '--cookies '
                + cookies
                + " -a "
                + link
                + " -o \""
                + directory
                + '/%(title)s-%(id)s-144p.%(ext)s" '
                + args
                )
    else:
        pass
    