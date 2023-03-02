import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
import sys

root = tk.Tk()
root.title("YT Downloader")
root.geometry("640x320")

listVideoSize = []

strVideoSize = StringVar()
strDirectory = StringVar()

def paste_button_click(event):
    entryURL.delete(0, tk.END)
    entryURL.insert(0, root.clipboard_get())
    check_URL_availability()

def on_entry_click(event):
    if entryURL.get() == "Masukkan URL":
        entryURL.delete(0, tk.END)

def directory_button_click():
    strDirectory.set(filedialog.askdirectory())
    entryDirectory.delete(0, tk.END)
    entryDirectory.insert(0, strDirectory.get())

def download_button_click():
    try :
        yt = YouTube(entryURL.get(), on_progress_callback=progress_function)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=strVideoSize.get()).first()
        strVideoName = stream.title
        stream.download( output_path= strDirectory.get(), filename= strVideoName + ".mp4")
    except Exception as e :
        print(e)

def check_URL_availability() :
    if "tube.com" in entryURL.get() :
        yt = YouTube(entryURL.get())
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        if len(streams) > 0:
            for stream in streams :
                listVideoSize.append(stream.resolution)
            for index, size in enumerate(listVideoSize):
                radio = Radiobutton(frameVideoSize, text=size, variable=strVideoSize, value=size)
                radio.grid(row=0, column=index, sticky= "nsew")
            frameVideoSize.pack()
            frameDirectory.pack()
            frameDownload.pack()
        else:
            print("URL invalid")

def progress_function(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    buttonDownload.config(text=percent)



frameVideoSize = tk.Frame(root, pady= 5, padx=5)
frameURL = tk.Frame(root, pady= 5, padx=5)
frameDirectory = tk.Frame(root, pady= 5, padx=5)
frameDownload = tk.Frame(root, pady=5, padx=5)


entryURL = Entry(frameURL, width= 50)
entryURL.insert(0,"Masukkan URL")
entryURL.bind('<FocusIn>', on_entry_click)
entryURL.grid(row=0, column=0)

buttonPaste = Button(frameURL, text="Paste", width=5)
buttonPaste.bind("<Button-1>", paste_button_click)
buttonPaste.grid(row=0, column=1)

entryDirectory = Entry(frameDirectory, width= 50)
entryDirectory.insert(0,"Masukkan Directory")
entryDirectory.bind('<FocusIn>', on_entry_click)
entryDirectory.grid(row=0, column=0)

buttonDirectory = Button(frameDirectory, text="Browse", command=directory_button_click, width=5)
buttonDirectory.grid(row=0, column=1)

buttonDownload = Button(frameDownload, text="Download", command=download_button_click)
buttonDownload.grid(row=0, column=0)

frameURL.pack()

root.mainloop()