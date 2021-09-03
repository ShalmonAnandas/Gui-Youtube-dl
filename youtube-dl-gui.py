import os
from os import path
import platform
import sys
sys.path.insert(1, 'gui_files')
from pathlib import Path
import wx
from wx.core import Dialog


import yt_dl
import unknown_os_popup


IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

#Changed it so it works well with cloning straight out of the box
win_dl = "yt-dlp.exe -v "
lin_dl = "yt-dlp -v "
if IS_WINDOWS == True:
    uni_dl = "yt_dlp\\__main__.py -v "
else:
    uni_dl = "yt_dlp/__main__.py -v "

if IS_WINDOWS:
    if path.exists("yt-dlp.exe"):
        YOUTUBEDL_MAIN = win_dl
    else:
        YOUTUBEDL_MAIN = uni_dl
elif IS_LINUX:
    if path.exists("yt-dlp"):
        YOUTUBEDL_MAIN = lin_dl
    else:
        YOUTUBEDL_MAIN = uni_dl
else:
    #popup for unknown os
    class CalcFrame(unknown_os_popup.MyDialog1):
        def __init__(self, parent):
            unknown_os_popup.MyDialog1.__init__(self, parent)

        def exit(self, event):
            sys.exit()

    app = wx.App(False)
    frame = CalcFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()

    


HOME = Path().home() / Path("Videos")

if not HOME.exists():
    os.makedirs(HOME)


def run_youtube_dl(args: str) -> None:
    """Run youtube-dl commands on platform"""
    # TODO: Change for subprocess module
    os.system(YOUTUBEDL_MAIN + args)
    # Logs (can use logging module)
    # print(YOUTUBEDL_MAIN + args)


class CalcFrame(yt_dl.MyFrame):
    def __init__(self, parent):
        yt_dl.MyFrame.__init__(self, parent)
        if IS_WINDOWS:
            text_ctr: wx.TextCtrl = self.m_dirPicker1.GetTextCtrl()
            text_ctr.AppendText(str(HOME))
        else: pass
        self.m_checkBox2.Hide()


    @staticmethod
    def convert2seconds(raw_time: str) -> int:
        """Convert raw text in format 00:00 to seconds"""
        minutes, seconds = raw_time.split(":", maxsplit=1)
        return int(minutes) * 60 + int(seconds)

    def video_dl(self, event):
        link: str = self.link_box.GetValue()
        directory: str = self.m_dirPicker1.GetPath()
        args: str = self.m_custom_args.GetValue()

        # Audio/Quality/Video
        # TODO: Refactor by Video Quality
        if self.m_checkBox1.GetValue() == 1:
            cmd_args = (
                "-x --audio-format mp3 --audio-quality 2 "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 7:
            cmd_args = (
                "-f bestvideo[width=256]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-144p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 6:
            cmd_args = (
                "-f bestvideo[width=426]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-240p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 5:
            cmd_args = (
                "-f bestvideo[width=640]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-360p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 4:
            cmd_args = (
                "-f bestvideo[width=854]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-480p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 3:
            cmd_args = (
                "-f bestvideo[width=1280]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-720p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 2:
            cmd_args = (
                "-f bestvideo[width=1920]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-1080p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 1:
            cmd_args = (
                "-f bestvideo[width=2560]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-1440p.%(ext)s" '
                + args
            )
        elif self.quality_selection_drop_down.GetSelection() == 0:
            cmd_args = (
                "-f bestvideo[width=3840]+bestaudio "
                + link
                + ' -o "'
                + directory
                + '/%(title)s-%(id)s-4k.%(ext)s" '
                + args
            )
        else:
            cmd_args = link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args

        run_youtube_dl(cmd_args)

    def clip_dl(self, event):
        link: str = self.link_box.GetValue()
        directory: str = self.m_dirPicker1.GetPath()
        args: str = self.m_custom_args.GetValue()
        startTimeRaw: str = self.clip_start_box.GetValue()
        endTimeRaw: str = self.clip_end_box.GetValue()

        # converts for starttime
        startTime = self.convert2seconds(startTimeRaw)
        # conversion for endtime
        endTime = self.convert2seconds(endTimeRaw)
        # run command to download clip
        cmd_args = (
            link
            + ' --external-downloader ffmpeg --external-downloader-args "-ss '
            + str(startTime)
            + " -to "
            + str(endTime)
            + '" -o "'
            + directory
            + '/%(title)s-%(id)s.%(ext)s" '
            + args
        )
        run_youtube_dl(cmd_args)

    def clip_mp3_dl(self, event):

        link = self.link_box.GetValue()
        directory = self.m_dirPicker1.GetPath()
        args = self.m_custom_args.GetValue()
        startTimeRaw = self.clip_start_box.GetValue()
        endTimeRaw = self.clip_end_box.GetValue()

        # converts for starttime
        startTime = self.convert2seconds(startTimeRaw)
        # conversion for endtime
        endTime = self.convert2seconds(endTimeRaw)

        # run command to download clip
        cmd_args = (
            "-f bestaudio "
            + link
            + ' --external-downloader ffmpeg --external-downloader-args "-ss '
            + str(startTime)
            + " -to "
            + str(endTime)
            + '" -o "'
            + directory
            + '/%(title)s-%(id)s.%(ext)s" '
            + args
        )
        run_youtube_dl(cmd_args)


app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()
