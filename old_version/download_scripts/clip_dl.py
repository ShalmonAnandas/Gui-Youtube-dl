import os
import sys
sys.path.insert(1, 'gui_files')

import noname


def clip_dl_func(self, event):
    link: str = self.vid_link.GetValue()
    directory: str = self.m_dirPicker1.GetPath()
    cookies: str = self.cookie_picker.GetPath()
    args: str =  self.custom_args.GetValue()

    startTimeRaw = str(self.m_timePicker2.GetValue()).split(" ")[4]
    print(startTimeRaw)
    hours, minutes, seconds = startTimeRaw.split(":", maxsplit=2)
    startTime = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)


    endTimeRaw = str(self.m_timePicker3.GetValue()).split(" ")[4]
    print(endTimeRaw)
    hours, minutes, seconds = endTimeRaw.split(":", maxsplit=2)
    endTime = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)

    if self.m_comboBox1.GetSelection() == 0:
        os.system(
                "yt-dlp -f best*+bestaudio --cookies "
                + cookies
                + ' '
                + link
                + ' --external-downloader ffmpeg --external-downloader-args ffmpeg:"-ss '
                + str(startTime)
                + ' -to '
                + str(endTime)
                + "\" -o \""
                + directory
                + '/%(title)s-%(id)s-best.%(ext)s" '
                + args
                )
    elif self.m_comboBox1.GetSelection() == 1:
        os.system(
                "yt-dlp -f worst*+bestaudio --cookies "
                + cookies
                + ' '
                + link
                + ' --external-downloader ffmpeg --external-downloader-args ffmpeg:"-ss '
                + str(startTime)
                + ' -to '
                + str(endTime)
                + "\" -o \""
                + directory
                + '/%(title)s-%(id)s-worst.%(ext)s" '
                + args
                )
    else: pass