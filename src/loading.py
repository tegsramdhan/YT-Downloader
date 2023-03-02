import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    # Disable the download button and show the progress bar
    download_button.config(state=tk.DISABLED)
    progress_bar.grid(row=3, column=0, columnspan=2, pady=10)

    # Get the YouTube video URL and download path from the entry widgets
    url = url_entry.get()
    path = path_entry.get()

    # Download the YouTube video
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download(path)

    # Hide the progress bar and enable the download button
    progress_bar.grid_forget()
    download_button.config(state=tk.NORMAL)

# Create the Tkinter window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create the input widgets
url_label = tk.Label(window, text="Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

path_label = tk.Label(window, text="Download Path:")
path_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

path_entry = tk.Entry(window, width=50)
path_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the download button and progress bar
download_button = tk.Button(window, text="Download", command=download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(window, mode="indeterminate", length=300)

# Run the Tkinter event loop
window.mainloop()
