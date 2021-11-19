import wx
import os
import platform
from os import path
from pathlib import Path
import sys

from wx.core import Panel
sys.path.insert(1, 'gui_files')

import noname
import video_dl
import multi_video_dl
import add_link
import clip_dl

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

class vid(noname.vid_frame):
    def __init__(self, parent):
        noname.vid_frame.__init__(self, parent)
    
    def vid_dl(self, event):
        video_dl.video_dl(self, event)

class mul_vid(noname.mul_vid_frame):
    def __init__(self, parent):
        noname.mul_vid_frame.__init__(self, parent)
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
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))
        self.m_timePicker3.SetTime(0, 0, 0)
        self.m_timePicker4.SetTime(0, 0, 0)


app = wx.App(False)
frame =  MainWindow(None)
frame.Show(True)

app.MainLoop()
