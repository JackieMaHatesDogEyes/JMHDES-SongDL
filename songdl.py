import urllib.request
import re
try:
    inp = open("songs.txt", "r")
    songs = inp.readlines()
except FileNotFoundError:
    from time import sleep
    print("No songs.txt file found.\nClosing in 10 seconds...")
    sleep(10)
    quit()

for i in range(0, len(songs)):
    songName = songs[i]
    songName = songName.replace("\n", "")
    urlName = songName.replace(" ", "+")
    urlName = urlName.replace("\n", "")

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + urlName)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_ids = "https://www.youtube.com/watch?v=" + video_ids[0]
    print(video_ids)

    from pytube import YouTube
    yt = YouTube(video_ids)
    fileName = songName + ".mp4"
    songName = yt.title
    ys = yt.streams.get_by_itag('22')
    ys.download(filename= fileName)
    

    from moviepy.editor import *
    mp4vid = fileName
    mp3exp = songName + ".mp3"
    videoclip = VideoFileClip(mp4vid)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3exp)
    audioclip.close()
    videoclip.close()



import os

dir_name = "."
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".mp4"):
        os.remove(os.path.join(dir_name, item))