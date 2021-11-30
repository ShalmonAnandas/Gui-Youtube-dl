import os
import sys
import wx
sys.path.insert(1, 'gui_files')

import noname
batch_file = os.path.join('multi_download_files', 'batch_file.txt')

def append_link(self, event):
    link = self.m_textCtrl2.GetValue()

    batch_file = open(batch_file, 'a')
    batch_file.write(link + "\n")
    batch_file.close()

    show_links = open(batch_file, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")

def clear_link_func(self, event):
    clear_file = open(batch_file, 'r+')
    clear_file.truncate(0)
    clear_file.close()

    show_links = open(batch_file, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")