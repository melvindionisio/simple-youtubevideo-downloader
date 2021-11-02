from tkinter import *
from pytube import YouTube


# modify the path where you want the videos to be saved
PATH = "D:\pytube\downloads"

Youtube_Downloader = Tk()
Youtube_Downloader.title("Youtube Downloader")
container = Label(Youtube_Downloader, bg="black")

TITLE = Label(
    container,
    text="YOUTUBE VIDEO DOWNLOADER",
    font=("Fira Code", 14, "bold"),
    bg="black",
    foreground="white",
)
linkbox = Entry(
    container,
    font=("calibre", 12),
)

# call function when we click on entry box
# def click(*args):
#     linkbox.delete(0, 'end')

# call function when we leave entry box
# def leave(*args):
#     linkbox.delete(0, 'end')
#     linkbox.insert(0, 'Enter Video Link ')
#     container.focus()
# linkbox.bind("<Button-1>", click)
# linkbox.bind("<Leave>", leave)


def clear():
    linkbox.delete(0, "end")


def startdownload():
    link = linkbox.get()
    if link == "":
        message1 = Label(Youtube_Downloader, text="Please enter link first.")
        message1.grid()
    else:

        try:
            yt = YouTube(link)
            yt.streams.filter(progressive=True, file_extension="mp4").order_by(
                "resolution"
            ).desc().first().download(output_path=PATH)
            # print("\n", yt.streams.first().default_filename, " saved to ", PATH)
        except:
            print("error downloading", link)
        message2 = Label(
            Youtube_Downloader,
            font=("Arial", 8, "bold"),
            text=f"Download Successfully \n{yt.streams.first().default_filename} saved to {PATH}",
            justify=CENTER,
            wraplength=370,
        )
        message2.grid(row=5, column=0, columnspan=4, rowspan=2, pady=5, padx=10)


download_btn = Button(
    container,
    text="Download Video",
    height=3,
    width=20,
    bg="orange",
    command=startdownload,
)
clear_btn = Button(
    container, text="Clear", height=3, width=20, bg="orange", command=clear
)
message = Label(
    container,
    text="Start Downloading by Pasting Youtube links.",
    font=("Arial", 8, "bold"),
    bg="black",
    foreground="white",
)

# arranging
container.grid(ipadx=10, ipady=10)
TITLE.grid(row=0, column=0, columnspan=4, rowspan=2, pady=10, padx=10)
linkbox.grid(row=2, column=0, columnspan=4, padx=20, pady=5, ipadx=70, ipady=5)
clear_btn.grid(row=3, column=0, columnspan=2, sticky=E, padx=5, pady=15)
download_btn.grid(row=3, column=2, columnspan=2, sticky=W, padx=5, pady=15)
message.grid(row=4, column=0, columnspan=4, rowspan=3, pady=10, padx=10)


Youtube_Downloader.mainloop()
