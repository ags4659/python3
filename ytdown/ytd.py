from pytube.__main__ import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
yd.download('/YoutubeDowloads')
