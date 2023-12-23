from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Downloading: ", yt.title)

ys = yt.streams.get_highest_resolution()

print("Downloading...")

ys.download('/Volumes/CT1000P3 PSSD8 Media/Youtube Videos')

print("Download completed!!")