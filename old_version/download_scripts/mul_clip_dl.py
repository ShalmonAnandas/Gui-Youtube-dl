import os
import sys
sys.path.insert(1, 'gui_files')

import noname
multi_clip = os.path.join('multi_download_files', 'multi_clip.txt')


def mul_clip_dl_func(self, event):

    cookies: str = self.cookie_picker.GetPath()
    args: str =  self.custom_args.GetValue()


    test = open(multi_clip, 'r')
    counter = 0

    content = test.read()
    content_list = content.split("\n")

    for i in content_list:
        if i:
            counter += 1

    print(counter)


    for i in range(counter):
        link = content_list[i]
        directory: str = self.m_dirPicker1.GetPath()

        os.system(
                "yt-dlp -f best*+bestaudio --cookies "
                + cookies
                + ' '
                + link
                + "\" -o \""
                + directory
                + '/%(title)s-%(id)s-clip'+str([i])+'.%(ext)s" '
                + args
                )
