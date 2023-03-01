import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog



def paste_button_click(event):
    entryURL.insert(0, root.clipboard_get())

def on_entry_click(event):
    if entryURL.get() == "Masukkan URL":
        entryURL.delete(0, tk.END)

def directory_button_click():
    strDirectory = filedialog.askdirectory()
    entryDirectory.insert(0, strDirectory)

def download_button_click():
    try :
        yt = YouTube(entryURL.get())
        stream = yt.streams.filter(progressive=True, file_extension='mp4', res=strVideoSize.get()).first()
        strVideoName = stream.title
        stream.download( output_path= f"{strDirectory}/{strVideoName}.mp4")
    except Exception as e :
        print(e)





root = tk.Tk()
root.title("YT Downloader")
root.geometry("640x320")

strVideoURL = StringVar()
strVideoSize = StringVar()
strDirectory = StringVar()

frameVideoSize = tk.Frame(root, pady= 5, padx=5)
frameURL = tk.Frame(root, pady= 5, padx=5)
frameDirectory = tk.Frame(root, pady= 5, padx=5)




listVideoSize = ["1080p", "720p", "480p", "360p", "240p", "144p"]

for index, size in enumerate(listVideoSize):
    radio = Radiobutton(frameVideoSize, text=size, variable=strVideoSize, value=size)
    radio.grid(row=0, column=index, sticky= "nsew")

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

buttonDownload = Button(root, text="Download", command=download_button_click)
buttonDownload.pack()

frameVideoSize.pack()
frameURL.pack()
frameDirectory.pack()

root.mainloop()