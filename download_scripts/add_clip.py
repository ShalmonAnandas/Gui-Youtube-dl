import os
import sys
import wx
sys.path.insert(1, 'gui_files')

import noname
multi_clip_show = os.path.join('multi_download_files', 'multi_clip_show.txt')
multi_clip = os.path.join('multi_download_files', 'multi_clip.txt')

def append_link(self, event):
    link = self.m_textCtrl2.GetValue()
    startTimeRaw = str(self.m_timePicker3.GetValue()).split(" ")[1]
    hours, minutes, seconds = startTimeRaw.split(":", maxsplit=2)
    startTime = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)

    endTimeRaw = str(self.m_timePicker4.GetValue()).split(" ")[1]
    hours, minutes, seconds = endTimeRaw.split(":", maxsplit=2)
    endTime = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)


    batch_file_show = open(multi_clip_show, 'a')
    batch_file_show.write(link + " " + startTimeRaw + " " + endTimeRaw +"\n")
    batch_file_show.close()

    batch_file = open(multi_clip, 'a')
    batch_file.write(link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to ' + str(endTime) + "\n")
    batch_file.close()

    show_links = open(multi_clip_show, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")

def clear_link_func(self, event):
    clear_file = open(multi_clip_show, 'r+')
    clear_file.truncate(0)
    clear_file.close()

    clear_file = open(multi_clip, 'r+')
    clear_file.truncate(0)
    clear_file.close()

    show_links = open(multi_clip, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")