from pytube import YouTube
import sys

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
yd.download('./YTfolder')
