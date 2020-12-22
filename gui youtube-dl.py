import youtube_dl
import ffmpeg
import os
import tkinter as tk
from tkinter import *

def clip_dl():
    #input for links / starttime / endtime
    link = str(E1.get())
    startTimeRaw = str(E2.get())
    endTimeRaw = str(E3.get())

    ##converts for starttime
    minute2sec1 = startTimeRaw[0] + startTimeRaw[1]
    sec1 = startTimeRaw[3] + startTimeRaw[4]
    startTime = int(minute2sec1) * int(60) + int(sec1)
    #print(startTime)

    #conversion for endtime
    minute2sec2 = endTimeRaw[0] + endTimeRaw[1]
    sec2 = endTimeRaw[3] + endTimeRaw[4]
    endTime = int(minute2sec2) * int(60) + int(sec2)
    #print(endTime)

    #run command to download clip
    os.system('youtube-dl -v -f 22 '+ link + ' --external-downloader ffmpeg --external-downloader-args "-ss ' + str(startTime) + ' -to '+ str(endTime) + '" ')

    #test
    #print(link)
    #print(startTime)
    #print(endTime)
    #input("press enter to continue")


def video_dl():
    link = str(E1.get())

    os.system('youtube-dl -v '+ link)



root = tk.Tk()
root.title('Youtube Downloader')
window_logo = PhotoImage(file = 'logo.png')
root.iconphoto(False, window_logo)

#def clip_dl():


canvas = tk.Canvas(root, height=100, width=490, bg="#d12424")
Title = Label(canvas, text="Youtube Downloader",bg="#d12424", fg = "white", padx =77, font = "Helvetica 36 bold italic").pack(side = LEFT)
#logo = Label(canvas, image=Image).pack(side =RIGHT)
canvas.pack()



frame = tk.Frame(root, bg="#d12424",padx =109, pady = 9)
L1 = Label(frame,pady=2, padx=4, text="Paste Link : ", font = "Helvetica 20 bold italic", bg="#d12424", fg="white" )
L1.pack(side = LEFT)
E1 = Entry(frame, bd =2, bg="#d12424", font = "Helvetica 16 bold italic", fg="white")
E1.pack(side = LEFT)
frame.pack(side = TOP)

frame = tk.Frame(root, bg="#d12424",padx =18, pady = 9)
"""
variable = StringVar(frame)
variable.set("one") # default value

w = OptionMenu(frame, variable, "one", "two", "three")
w.pack()
"""
B2 = tk.Button(frame, padx=196, pady=0, text="Download Video", font = "Helvetica 18 bold italic", bg="#d12424", fg="white", command = video_dl)
B2.pack(side = RIGHT)
frame.pack(side = TOP)

frame = tk.Frame(root, bg ="#d12424", pady=15,padx=72)
L2 = Label(frame,pady=0, padx=0, text="Clip Start (00:00) : ", font = "Helvetica 20 bold italic", bg="#d12424", fg="white")
L2.pack(side = LEFT)
E2 = Entry(frame, bd =2, bg="#d12424", font = "Helvetica 16 bold italic", fg="white")
E2.pack(side = LEFT)
frame.pack()

frame = tk.Frame(root, bg ="#d12424", pady=15,padx=77)
L3 = Label(frame, text="Clip End (00:00) : ", font = "Helvetica 20 bold italic", bg="#d12424", fg="white")
L3.pack(side = LEFT)
E3 = Entry(frame, bd =2, bg="#d12424", font = "Helvetica 16 bold italic", fg="white")
E3.pack(side = LEFT)
frame.pack()

frame = Frame(root, padx = 19, pady=5, bg = "#d12424")
B1 = tk.Button(frame, padx=205, pady=2, text="Download Clip", font = "Helvetica 18 bold italic", bg="#d12424", fg="white", command = clip_dl)
B1.pack()
frame.pack(side = BOTTOM)

root.mainloop()