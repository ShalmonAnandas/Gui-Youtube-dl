from turtle import update
import wx
import os
import platform
from os import path
from pathlib import Path
import sys

sys.path.insert(1, 'gui_files')
sys.path.insert(1, 'download_scripts')
sys.path.insert(1, 'multi_download_files')
sys.path.insert(1, 'update_script')

import noname
import video_dl
import multi_video_dl
import add_link
import clip_dl
import add_clip
import mul_clip_dl
import audio_dl
import multi_audio_dl
import yt_dlp_update_script

# IS_WINDOWS = platform.system() == "Windows"
# IS_LINUX = platform.system() == "Linux"

exec_exists = False

if(platform.system() == "Windows"):
    update_status_path = os.path.join('update_script', 'update_status.txt')
    os.system("yt-dlp.exe -U > " + update_status_path)
    print(sys.stdout.flush())
elif(platform.system() == "Linux"):
    yt_dlp_exec = Path("yt-dlp")
    exec_exists = yt_dlp_exec.is_file()
    print(exec_exists)

if(exec_exists == True):
    print("Executable Exists")
else:
    yt_dlp_update_script.Update()

HOMEVID = Path().home() / Path("Videos")
HOMEAUD = Path().home() / Path("Music")

cookie_path = os.path.join('multi_download_files', 'default_cookies.txt')

class MainWindow(noname.home_frame):

    def __init__(self, parent):
        noname.home_frame.__init__(self, parent)

    def exit(self, event):
        sys.exit()

    def single_vid_func(self, event):
        app = wx.App(False)
        frame =  vid(None)
        frame.Show(True)
        app.MainLoop()
    
    def mul_vid_func(self, event):
        app = wx.App(False)
        frame =  mul_vid(None)
        frame.Show(True)
        app.MainLoop()
    
    def clip_func(self, event):
        app = wx.App(False)
        frame =  clip(None)
        frame.Show(True)
        app.MainLoop()
    
    def mul_clip_func(self, event):
        app = wx.App(False)
        frame =  multi_clip(None)
        frame.Show(True)
        app.MainLoop()

    def aud_func(self, event):
        app = wx.App(False)
        frame = single_audio(None)
        frame.Show(True)
        app.MainLoop()
    
    def mul_aud_func(self, event):
        app = wx.App(False)
        frame = multi_audio(None)
        frame.Show(True)
        app.MainLoop()
    
    def update_yt_dlp(self, event):
        app = wx.App(False)
        frame = update_screen(None)
        frame.Show(True)
        app.MainLoop

class update_screen(noname.update_screen):

    def __init__(self, parent):
        noname.update_screen.__init__(self, parent)
        yt_dlp_update_script.Update()
    
    def quit_update(self, event):
        wx.Exit()

class vid(noname.vid_frame):
    def __init__(self, parent):
        noname.vid_frame.__init__(self, parent)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker1.SetPath(str(HOMEVID))
    
    def vid_dl(self, event):
        video_dl.video_dl(self, event)

class mul_vid(noname.mul_vid_frame):
    def __init__(self, parent):
        noname.mul_vid_frame.__init__(self, parent)
        add_link.clear_all_links_func(self, 0)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker1.SetPath(str(HOMEVID))

    def add_link_func(self, event):
        add_link.append_link(self, event)
        self.m_textCtrl2.SetValue("")

    def mul_vid_dl(self, event):
        multi_video_dl.multi_video_dl(self, event)

    def clear_link(self, event):
        add_link.clear_link_func(self, event)
    
    def clear_all_links(self, event):
        add_link.clear_all_links_func(self, event)

class clip(noname.clip_frame):
    def __init__(self, parent):
        noname.clip_frame.__init__(self, parent)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker1.SetPath(str(HOMEVID))
        self.m_timePicker2.SetTime(0, 0, 0)
        self.m_timePicker3.SetTime(0, 0, 0)

    def clip_dl(self, event):
        clip_dl.clip_dl_func(self, event)

class multi_clip(noname.mul_clip_frame):
    def __init__(self, parent):
        noname.mul_clip_frame.__init__(self, parent)
        add_clip.clear_all_links_func(self, 0)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker1.SetPath(str(HOMEVID))
        self.m_timePicker3.SetTime(0, 0, 0)
        self.m_timePicker4.SetTime(0, 0, 0)

    def add_clip_func(self, event):
        add_clip.append_link(self, event)

    def clear_link(self, event):
        add_clip.clear_link_func(self, event)
    
    def clear_all_links(self, event):
        add_clip.clear_all_links_func(self, event)

    def mul_clip_dl(self, event):
        mul_clip_dl.mul_clip_dl_func(self, event)

class single_audio(noname.aud_frame):
    def __init__(self, parent):
        noname.aud_frame.__init__(self, parent)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker5.SetPath(str(HOMEAUD))

    def audio_dl(self, event):
        audio_dl.audio_dl_func(self, event)

class multi_audio(noname.mul_aud_frame):
    def __init__(self, parent):
        noname.mul_aud_frame.__init__(self, parent)
        add_link.clear_all_links_func(self, 0)
        self.cookie_picker.SetPath(cookie_path)
        self.m_dirPicker1.SetPath(str(HOMEAUD))
    
    def add_link_func(self, event):
        add_link.append_link(self, event)
        self.m_textCtrl2.SetValue("")

    def clear_all_links(self, event):
        add_link.clear_all_links_func(self, event)
    
    def clear_link(self, event):
        add_link.clear_link_func(self, event)

    def mul_aud_dl(self, event):
        multi_audio_dl.multi_audio_dl(self, event)
        

app = wx.App(False)
frame =  MainWindow(None)
frame.Show(True)

app.MainLoop()
