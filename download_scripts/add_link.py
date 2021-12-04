import os
import sys
import wx
sys.path.insert(1, 'gui_files')

import noname
path = os.path.join('multi_download_files', 'batch_file.txt')

def append_link(self, event):
    link = self.m_textCtrl2.GetValue()

    batch_file = open(path, 'a')
    batch_file.write(link + "\n")
    batch_file.close()

    show_links = open(path, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")

def clear_all_links_func(self, event):
    clear_file = open(path, 'r+')
    clear_file.truncate(0)
    clear_file.close()

    show_links = open(path, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")

def clear_link_func(self, event):
    clear_file = open(path, 'r+')
    lines = clear_file.readlines()
    clear_file.close()

    del lines[-1]
    new_file = open(path, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

    show_links = open(path, 'r')
    links = show_links.read()
    self.m_richText2.Clear()
    self.m_richText2.WriteText(links + "\n")