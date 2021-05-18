import wx
import os


#import ht newly generated GUI file
import yt_dl

class CalcFrame(yt_dl.MyFrame):
    def __init__(self,parent):
        yt_dl.MyFrame.__init__(self,parent)

    def video_dl(self, event):

        if self.quality_selection_drop_down.GetSelection() == 0:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=640]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-360p.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f 22 '+ link + ' -o "' + directory + '\%(title)s-%(id)s.%(ext)s" '  )
        
        elif self.quality_selection_drop_down.GetSelection() == 1:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=854]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-480p.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f 22 '+ link + ' -o "' + directory + '\%(title)s-%(id)s.%(ext)s" '  )
        
        elif self.quality_selection_drop_down.GetSelection() == 2:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=1280]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-720p.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f 22 '+ link + ' -o "' + directory + '\%(title)s-%(id)s.%(ext)s" '  )
        
        elif self.quality_selection_drop_down.GetSelection() == 3:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=1920]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-1080p.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f bestvideo(height=1080p)+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args)
        
        elif self.quality_selection_drop_down.GetSelection() == 4:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=2560]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-1440p.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f 22 '+ link + ' -o "' + directory + '\%(title)s-%(id)s.%(ext)s" '  )
        
        elif self.quality_selection_drop_down.GetSelection() == 5:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -f bestvideo[width=3840]+bestaudio '+ link + ' -o "' + directory + '/%(title)s-%(id)s-4k.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -f 22 '+ link + ' -o "' + directory + '\%(title)s-%(id)s.%(ext)s" '  )
        
        elif self.quality_selection_drop_down.GetSelection() == 6:
            link = str(self.link_box.GetValue())
            directory = str(self.m_dirPicker1.GetPath())
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v -x --audio-format mp3 --audio-quality 2 ' + link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v -x --audio-format mp3 --audio-quality 2 ' + link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ')

        elif self.quality_selection_drop_down.GetSelection() == 7:
            link = str(self.link_box.GetValue())
            directory = self.m_dirPicker1.GetPath()
            args = str(self.m_custom_args.GetValue())
            os.system('youtube_dl\__main__.py -v  '+ link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args)
            #test
            #print('youtube-dl -v  '+ link + ' -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ')
        
        else:
            pass

    def clip_dl(self, event):

        link = str(self.link_box.GetValue())
        directory = str(self.m_dirPicker1.GetPath())
        args = str(self.m_custom_args.GetValue())
        startTimeRaw = str(self.clip_start_box.GetValue())
        endTimeRaw = str(self.clip_end_box.GetValue())

        ##converts for starttime
        minute2sec1 = startTimeRaw[0] + startTimeRaw[1]
        sec1 = startTimeRaw[3] + startTimeRaw[4]
        startTime = int(minute2sec1) * int(60) + int(sec1)

        #conversion for endtime
        minute2sec2 = endTimeRaw[0] + endTimeRaw[1]
        sec2 = endTimeRaw[3] + endTimeRaw[4]
        endTime = int(minute2sec2) * int(60) + int(sec2)

        #run command to download clip
        os.system('youtube_dl\__main__.py -v '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args)
        #test
        #print('youtube-dl -v -f 22 '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ')

    def clip_dl_mp3(self, event):

        link = str(self.link_box.GetValue())
        directory = str(self.m_dirPicker1.GetPath())
        args = str(self.m_custom_args.GetValue())
        startTimeRaw = str(self.clip_start_box.GetValue())
        endTimeRaw = str(self.clip_end_box.GetValue())

        ##converts for starttime
        minute2sec1 = startTimeRaw[0] + startTimeRaw[1]
        sec1 = startTimeRaw[3] + startTimeRaw[4]
        startTime = int(minute2sec1) * int(60) + int(sec1)

        #conversion for endtime
        minute2sec2 = endTimeRaw[0] + endTimeRaw[1]
        sec2 = endTimeRaw[3] + endTimeRaw[4]
        endTime = int(minute2sec2) * int(60) + int(sec2)

        #run command to download clip
        os.system('youtube_dl\__main__.py -v -f bestaudio '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ' + args)
        #test
        #print('youtube-dl -v -f bestaudio '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + directory + '/%(title)s-%(id)s.%(ext)s" ')



app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()