import os
import sys
import wx
sys.path.insert(1, 'gui_files')

import noname

def append_link(self, event):
    link = self.m_textCtrl2.GetValue()

    batch_file = open('multi_download_files\\batch_file.txt', 'a')
    batch_file.write(link + "\n")
    batch_file.close()

    show_links = open('multi_download_files\\batch_file.txt', 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")

def clear_link_func(self, event):
    clear_file = open('multi_download_files\\batch_file.txt', 'r+')
    clear_file.truncate(0)
    clear_file.close()

    show_links = open('multi_download_files\\batch_file.txt', 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")