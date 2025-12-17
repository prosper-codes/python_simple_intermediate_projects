import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
import shutil
import os

def download():
    try:
        video_path = enter_url.get().strip()
        file_path = path_label.cget("text")
        
        # Validation
        if not video_path:
            messagebox.showerror("Error", "Please enter a video URL")
            return
        
        if file_path == "Select path to download":
            messagebox.showerror("Error", "Please select a download path")
            return
        
        # Download video
        download_button.config(state='disabled', text='DOWNLOADING...')
        root.update()
        
        yt = YouTube(video_path)
        mp4 = yt.streams.get_highest_resolution().download()
        
        # Move to selected directory
        filename = os.path.basename(mp4)
        destination = os.path.join(file_path, filename)
        shutil.move(mp4, destination)
        
        messagebox.showinfo("Success", f"Download complete!\nSaved to: {destination}")
        print("download_complete")
        
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")
    finally:
        download_button.config(state='normal', text='DOWNLOAD')

def getPath():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)

root = tk.Tk()
root.title('Video Downloader')
root.geometry('450x350')
canvas = tk.Canvas(root, width=450, height=350)
canvas.pack()

# app label
app_label = tk.Label(root, text="Video Downloader",
                     fg='black', font=('Arial', 25))
canvas.create_window(225, 40, window=app_label)

# entry point for url
enter_url_label = tk.Label(root, text="Enter Video URL",
                           fg='Navy Blue', font=('Sans', 13))
enter_url = tk.Entry(root, width=40)
canvas.create_window(225, 100, window=enter_url_label)
canvas.create_window(225, 130, window=enter_url)

# path to download videos
path_label = tk.Label(root, text="Select path to download")
path_button = tk.Button(root, text="SELECT", command=getPath)
canvas.create_window(225, 180, window=path_label)
canvas.create_window(225, 210, window=path_button)

# download button
download_button = tk.Button(root, text="DOWNLOAD", command=download, 
                            bg='green', fg='white', font=('Arial', 12))
canvas.create_window(225, 270, window=download_button)

root.mainloop()