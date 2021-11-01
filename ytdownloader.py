from pytube import YouTube

# modify the path where you want the videos to be saved
PATH = "D:\pytube\downloads"

# replace the txt file depending on your choice
LINKS=open("D:\pytube\downloadlink.txt", "r")

print("Starting download. Please wait.")

for link in LINKS:  
    try:
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path = PATH)
        print("\n", yt.streams.first().default_filename, " saved to ", PATH )
       
    except:
        print("error downloading", link)