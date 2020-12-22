from tkinter import *
import pytube
import os


def download():
    video_url=url.get()

    try:
        youtube=pytube.YouTube(video_url)
        video= youtube.streams.first()
        username = os.getlogin()
        video.download(r"C:\Users\{0}\Desktop.".format(username))
        notif.config(fg="green",text="Download Complete")

    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not downloaded")

window=Tk()
window.title("Youtube download videos")
Label(window,text="Youtube Video Converter", fg="red" , font=("Calibri",15)).grid(sticky=N,padx=100,row=0)
Label(window,text="Enter video link: ", fg="black" , font=("Calibri",12)).grid(sticky=N,row=1,pady=15)
notif=Label(window,font=("Calibri",12))
notif.grid(sticky=N,pady=1,row=4)
url=StringVar()
Entry(window,width=50,textvariable=url).grid(sticky=N,row=2)
Button(window,text="Download",width=20,font=("Calibri",12),command=download).grid(sticky=N,row=3,pady=15)
window.mainloop()