from pytube import YouTube

# modify the path where you want the videos to be saved
PATH = "D:\pytube"

# replace the txt file depending on your choice
LINKS=open("D:\pytube\downloadlink.txt", "r")

for link in LINKS:  
    print(" - downloaded ", link )
    try:
        yt = YouTube(link)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path = PATH)
       
    except:
        print("error downloading", link)