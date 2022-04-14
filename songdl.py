import urllib.request
import re
from time import sleep

version = "0.0.2" #Current Application Version
versionURL = "https://raw.githubusercontent.com/VicCodezz/JMHDES-SongDL/master/VERSION.txt" #Github URL of Latest Version
urllib.request.urlretrieve(versionURL, "v") #Rerieves Latest Version
openV = open("v", "r").read() #Reads Data
if openV != version: #Quits Application if not Newest Version
    print("Please Download New Version...")
    sleep(5)
    quit()

try: #Tries To Open songs.txt
    inp = open("songs.txt", "r")
    songs = inp.readlines()
except FileNotFoundError: #Quits if unable to open songs.txt
    print("No songs.txt file found.\nClosing in 10 seconds...")
    sleep(10)
    quit()



#Removes all illegal characters from filename
def removeIllegal(illegal):
    illegal = illegal.replace("#", " ")
    illegal = illegal.replace("%", " ")
    illegal = illegal.replace("&", "and")
    illegal = illegal.replace("{", " ")
    illegal = illegal.replace("}", " ")
    illegal = illegal.replace("\\", " ")
    illegal = illegal.replace("<", " ")
    illegal = illegal.replace(">", " ")
    illegal = illegal.replace("*", " ")
    illegal = illegal.replace("?", " ")
    illegal = illegal.replace("$", "S")
    illegal = illegal.replace("!", " ")
    illegal = illegal.replace("'", " ")
    illegal = illegal.replace('"', " ")
    illegal = illegal.replace(":", " ")
    illegal = illegal.replace("@", " ")
    illegal = illegal.replace("+", " ")
    illegal = illegal.replace("`", " ")
    illegal = illegal.replace("|", " ")
    illegal = illegal.replace("=", " ")
    return illegal


for i in range(0, len(songs)): #For Loop
    songName = songs[i] #Gets Current Song Name
    songName = songName.replace("\n", "") #Removes Linebreak in song name
    urlName = songName.replace(" ", "+") #Replaces Spaces with "+" (For URL reasons)
    urlName = urlName.replace("\n", "")

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + urlName) #Gets YouTube Link
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode()) #Gets Video IDs
    video_ids = "https://www.youtube.com/watch?v=" + video_ids[0] #Gets The ID of the First Video
    print(video_ids) #Prints Song Name

    #Stuff for Downloading as MP4
    from pytube import YouTube
    yt = YouTube(video_ids)
    fileName = songName + ".mp4"
    songName = yt.title
    ys = yt.streams.get_by_itag('22')
    ys.download(filename= fileName)
    
    songName = removeIllegal(songName)

    #Convert To MP3
    from moviepy.editor import *
    mp4vid = fileName
    mp3exp = songName + ".mp3"
    videoclip = VideoFileClip(mp4vid)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3exp)
    audioclip.close()
    videoclip.close()


#Delete MP4 and "v" files
import os

dir_name = "."
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".mp4"):
        os.remove(os.path.join(dir_name, item))

os.remove("v")