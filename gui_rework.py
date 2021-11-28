import wx
import os
import platform
from os import path
from pathlib import Path
import sys

from wx.core import Panel
sys.path.insert(1, 'gui_files')
sys.path.insert(1, 'download_scripts')
sys.path.insert(1, 'multi_download_files')

import noname
import video_dl
import multi_video_dl
import add_link
import clip_dl
import add_clip
import mul_clip_dl
import audio_dl
import multi_audio_dl

IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

HOME = Path().home() / Path("Videos")


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

class vid(noname.vid_frame):
    def __init__(self, parent):
        noname.vid_frame.__init__(self, parent)
    
    def vid_dl(self, event):
        video_dl.video_dl(self, event)

class mul_vid(noname.mul_vid_frame):
    def __init__(self, parent):
        noname.mul_vid_frame.__init__(self, parent)
        add_link.clear_link_func(self, 0)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))

    def add_link_func(self, event):
        add_link.append_link(self, event)
        self.m_textCtrl2.SetValue("")

    def mul_vid_dl(self, event):
        multi_video_dl.multi_video_dl(self, event)

    def clear_links(self, event):
        add_link.clear_link_func(self, event)

class clip(noname.clip_frame):
    def __init__(self, parent):
        noname.clip_frame.__init__(self, parent)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))
        self.m_timePicker2.SetTime(0, 0, 0)
        self.m_timePicker3.SetTime(0, 0, 0)

    def clip_dl(self, event):
        clip_dl.clip_dl_func(self, event)

class multi_clip(noname.mul_clip_frame):
    def __init__(self, parent):
        noname.mul_clip_frame.__init__(self, parent)
        add_clip.clear_link_func(self, 0)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))
        self.m_timePicker3.SetTime(0, 0, 0)
        self.m_timePicker4.SetTime(0, 0, 0)

    def add_clip_func(self, event):
        add_clip.append_link(self, event)

    def clear_links(self, event):
        add_clip.clear_link_func(self, event)

    def mul_clip_dl(self, event):
        mul_clip_dl.mul_clip_dl_func(self, event)

class single_audio(noname.aud_frame):
    def __init__(self, parent):
        noname.aud_frame.__init__(self, parent)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker5.GetTextCtrl()
            text_ctr.AppendText(str(HOME))

    def audio_dl(self, event):
        audio_dl.audio_dl_func(self, event)

class multi_audio(noname.mul_aud_frame):
    def __init__(self, parent):
        noname.mul_aud_frame.__init__(self, parent)
        add_link.clear_link_func(self, 0)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))
    
    def add_link_func(self, event):
        add_link.append_link(self, event)
        self.m_textCtrl2.SetValue("")

    def clear_links(self, event):
        add_link.clear_link_func(self, event)

    def mul_aud_dl(self, event):
        multi_audio_dl.multi_audio_dl(self, event)



app = wx.App(False)
frame =  MainWindow(None)
frame.Show(True)

app.MainLoop()
