from pytube.__main__ import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
yd.download('/homyte/ags/Downloads/youdownloads')
## This programme needs an argument for example "python3 ytd.py "youtube link"