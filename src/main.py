import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
import sys
import threading

root = tk.Tk()
root.title("YT Downloader")
root.geometry("640x320")

listVideoSize = []

strVideoSize = StringVar()
strDirectory = StringVar()

def paste_button_click(event):
    entryURL.delete(0, tk.END)
    entryURL.insert(0, root.clipboard_get())
    t = threading.Thread(target=check_URL_availability)
    t.start()

def on_entry_click(event):
    if entryURL.get() == "Masukkan URL":
        entryURL.delete(0, tk.END)

def directory_button_click():
    strDirectory.set(filedialog.askdirectory())
    entryDirectory.delete(0, tk.END)
    entryDirectory.insert(0, strDirectory.get())

def download_button_click():
    try :
        loadingBar.grid(row=1, column=0, pady= 5)
        labelPercentage.grid(row=1, column=1, padx= 5, pady= 5)
        yt = YouTube(entryURL.get(), on_progress_callback=progress_function)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=strVideoSize.get()).first()
        strVideoName = stream.title
        stream.download( output_path= strDirectory.get(), filename= strVideoName + ".mp4")
    except Exception as e :
        print(e)

def download_thread() :
    t = threading.Thread(target=download_button_click)
    t.start()

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
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloaded: {percentage:.2f}%")
    loadingBar["value"] = percentage
    labelPercentage.config(text= f"{percentage:.2f}%")



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

buttonDownload = Button(frameDownload, text="Download", command=download_thread)
buttonDownload.grid(row=0, column=0)
loadingBar = ttk.Progressbar(frameDownload, orient="horizontal",length=250, mode="determinate")
labelPercentage = Label(frameDownload, text= "0.0%")


frameURL.pack()

root.mainloop()