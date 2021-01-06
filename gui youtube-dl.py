import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory


if os.path.isfile('customArgs.txt'):
    file = open('customArgs.txt', 'r')
    args = str(file.read())


def arguments():
    if len(argentry.get()) > 1:
        args = argentry.get()
    else:
        file = open('customArgs.txt', 'r')
        args = str(file.read())


def save_args():
    file = open('customArgs.txt', 'w')
    file.write(str(argentry.get()))


#code to download clips
def clip_dl():

    dl_path = askdirectory(title='Select Folder to Save File')
    #input for links / starttime / endtime
    link = str(E1.get())
    startTimeRaw = str(E2.get())
    endTimeRaw = str(E3.get())

    ##converts for starttime
    minute2sec1 = startTimeRaw[0] + startTimeRaw[1]
    sec1 = startTimeRaw[3] + startTimeRaw[4]
    startTime = int(minute2sec1) * int(60) + int(sec1)

    #conversion for endtime
    minute2sec2 = endTimeRaw[0] + endTimeRaw[1]
    sec2 = endTimeRaw[3] + endTimeRaw[4]
    endTime = int(minute2sec2) * int(60) + int(sec2)

    #run command to download clip
    os.system('youtube-dl -v -f 22 '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -f 22 '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)

def clip_dl_audio():

    dl_path = askdirectory(title='Select Folder to Save File')
    #input for links / starttime / endtime
    link = str(E1.get())
    startTimeRaw = str(E2.get())
    endTimeRaw = str(E3.get())

    ##converts for starttime
    minute2sec1 = startTimeRaw[0] + startTimeRaw[1]
    sec1 = startTimeRaw[3] + startTimeRaw[4]
    startTime = int(minute2sec1) * int(60) + int(sec1)

    #conversion for endtime
    minute2sec2 = endTimeRaw[0] + endTimeRaw[1]
    sec2 = endTimeRaw[3] + endTimeRaw[4]
    endTime = int(minute2sec2) * int(60) + int(sec2)

    #run command to download clip
    os.system('youtube-dl -v -f bestaudio '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -f 22 '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)


#code to download mp3
def mp3_dl():

    dl_path = askdirectory(title='Select Folder to Save File')
    link = str(E1.get())
    os.system('youtube-dl -v -x --audio-format mp3 --audio-quality 2 ' + link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -x --audio-format mp3 --audio-quality 2 ' + link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)

#code to download highest quality
def max_dl():
    dl_path = askdirectory(title='Select Folder to Save File')
    link = str(E1.get())
    os.system('youtube-dl -v -f bestvideo+bestaudio '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -f bestvideo+bestaudio '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)

#code to download 720p
def hd_dl():
    dl_path = askdirectory(title='Select Folder to Save File')
    link = str(E1.get())
    os.system('youtube-dl -v -f 22 '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -f 22 '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)

def non_youtube_dl():
    dl_path = askdirectory(title='Select Folder to Save File')
    link = str(E1.get())
    os.system('youtube-dl -v  '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)
    #test
    #print('youtube-dl -v -f 22 '+ link + ' -o "' + str(dl_path) + '/%(title)s-%(id)s.%(ext)s" ' + args)

def video_dl():
    hddl = (var1.get())
    maxdl = (var2.get())
    mp3dl = (var3.get())
    non = (var4.get())

    if hddl == 1:
        hd_dl()
    else:
        pass

    if maxdl == 1:
        max_dl()
    else:
        pass

    if mp3dl == 1:
        mp3_dl()
    else:
        pass

    if non == 1:
        non_youtube_dl()
    else:
        pass



#start of gui
root = tk.Tk()
root.title('Youtube Downloader')
#window_logo = PhotoImage(file = 'logo.png')
#root.iconphoto(False, window_logo)

#heading
canvas = tk.Canvas(root, height=100, width=490, bg="#4c5778")
Title = Label(canvas, text="Youtube Downloader",bg="#4c5778", fg = "black", padx =78, font = "arial 36 bold ").pack(side = LEFT)
canvas.pack()

frame = tk.Frame(root, bg="#4c5778",padx = 0, pady = 9)

"""
#button for download
direcbutton = tk.Button(frame, padx=30, pady=0, text="Set Download Folder", font = "arial 16 bold ", bg="#4c5778", fg="black", command = set_dl_path)
direcbutton.pack(side = RIGHT)
frame.pack(side = TOP)
frame.pack()
"""

#Paste link
frame = tk.Frame(root, bg="#4c5778",padx =110, pady = 9)
L1 = Label(frame,pady=2, padx=4, text="Paste Link : ", font = "arial 20 bold ", bg="#4c5778", fg="black" )
L1.pack(side = LEFT)
E1 = Entry(frame, bd =2, bg="#4c5778", font = "arial 16 bold ", fg="black")
E1.pack(side = LEFT)
frame.pack(side = TOP)

#checkboxes
frame = tk.Frame(root, bg="#4c5778",padx = 27, pady = 9)
var1 = IntVar()
Checkbutton(frame, text="HD(720p)", bg = "#4c5778", activebackground ="#4c5778",  font = "arial 15 bold ", fg="black", activeforeground="black", variable=var1).grid(row=0, column = 0, sticky=W)
var2 = IntVar()
Checkbutton(frame, text="Highest Quality", bg = "#4c5778", activebackground ="#4c5778",  font = "arial 15 bold ", fg="black", variable=var2).grid(row=0, column = 1, sticky=W)
var3 = IntVar()
Checkbutton(frame, text="Audio(mp3)", bg = "#4c5778", activebackground ="#4c5778",  font = "arial 15 bold ", fg="black", variable=var3).grid(row=0, column = 2, sticky=W)
var4 = IntVar()
Checkbutton(frame, text="non-youtube", bg = "#4c5778", activebackground ="#4c5778",  font = "arial 15 bold ", fg="black", variable=var4).grid(row=0, column = 3, sticky=W)
frame.pack()


frame = tk.Frame(root, bg="#4c5778",padx =55, pady = 9)
arglabel = Label(frame,pady=2, padx=4, text="Custom Arguments : ", font = "arial 14 bold ", bg="#4c5778", fg="black" )
arglabel.pack(side = LEFT)
argentry = Entry(frame, bd =2, bg="#4c5778", font = "arial 14 bold ", fg="black")
argentry.pack(side = LEFT)
argbutton = tk.Button(frame, padx=5, pady=0, text="save args", font = "arial 12 bold ", bg="#4c5778", fg="black", command = save_args)
argbutton.pack()
frame.pack()

if len(args) > 1:
    frame = tk.Frame(root, bg="#4c5778",padx =33, pady = 9)
    labelforargs = Label(frame,pady=2, padx=2, text="custom args : ", font = "arial 12 bold", bg="#777e91", fg="black" )
    labelforargs.pack(side = LEFT)
    argumentlabels = Label(frame,pady=2, padx=2, text=args, font = "arial 12 bold", bg="#777e91", fg="black", width = 45 )
    argumentlabels.pack(side = LEFT)
    frame.pack()
else:
    pass

"""
if len(argentry.get()) > 1:
    args = argentry.get()
else:
    gamer
"""

#buttons for mp3 and video download
frame = tk.Frame(root, bg="#4c5778",padx =18, pady = 9)
#button for download
B2 = tk.Button(frame, padx=234, pady=0, text="Download", font = "arial 18 bold ", bg="#4c5778", fg="black", command = video_dl)
B2.pack(side = RIGHT)
frame.pack(side = TOP)

#clip start and end
frame = tk.Frame(root, bg ="#4c5778", pady=15,padx=7)

#clip start time
L2 = Label(frame,pady=0, padx=0, text="Clip Start (00:00) : ", font = "arial 16 bold ", bg="#4c5778", fg="black")
L2.pack(side = LEFT)
E2 = Entry(frame, bd =2, bg="#4c5778", font = "arial 16 bold ", fg="black", width=10)
E2.pack(side = LEFT)


#clip end time

L3 = Label(frame, text="Clip End (00:00) : ", font = "arial 16 bold ", bg="#4c5778", fg="black")
L3.pack(side = LEFT)
E3 = Entry(frame, bd =2, bg="#4c5778", font = "arial 16 bold ", fg="black", width=10)
E3.pack(side = LEFT)
frame.pack()

#button for clipdl
frame = Frame(root, padx = 20, pady=5, bg = "#4c5778")
B1 = tk.Button(frame, padx=64, pady=2, text="Download Clip", font = "arial 14 bold ", bg="#4c5778", fg="black", command = clip_dl)
B1.pack(side= LEFT)

mp3button = tk.Button(frame, padx=64, pady=2, text="Download Clip mp3", font = "arial 14 bold ", bg="#4c5778", fg="black", command = clip_dl_audio)
mp3button.pack(side = LEFT)

frame.pack(side = BOTTOM)

"""
#button for test
frame = Frame(root, padx = 19, pady=5, bg = "#4c5778")
B1 = tk.Button(frame, padx=205, pady=2, text="Test", font = "arial 18 bold ", bg="#4c5778", fg="black", command = set_dl_path)
B1.pack()
frame.pack(side = BOTTOM)
"""

root.mainloop()
