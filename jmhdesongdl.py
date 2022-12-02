from yt_dlp import YoutubeDL
import urllib.request
import re
from time import sleep
import os

version = "0.1.0" #Current Application Version
versionURL = "https://raw.githubusercontent.com/VicCodezz/JMHDES-SongDL/master/VERSION.txt" #Github URL of Latest Version
urllib.request.urlretrieve(versionURL, "v") #Rerieves Latest Version
openV = open("v", "r").read() #Reads Data
if openV != version: #Quits Application if not Newest Version
    print("Please Download New Version...")
    sleep(5)
    quit()

os.remove("v") #Get rid of temporary Version Check file

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
    illegal = illegal.replace("$", "S") #Replace Dollar Sign with "S" (Used primarily for Rappers using a DOllar Sign in place of an 'S'
    illegal = illegal.replace("!", " ")
    illegal = illegal.replace("'", "") #Replace Apostrophe with Nothing
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
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode()) #Gets Video IDs As List
    video_id = video_id[0] #Gets The ID of the First Video
    vidurl = "https://www.youtube.com/watch?v=" + video_id
    del(video_id)
    del(html)
    del(urlName)

    vidinfo = YoutubeDL().extract_info(
        url = vidurl,download=False
    )

    fname = f"{songName}.mp3"
    o ={

        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':fname
    }

    with YoutubeDL(o) as ydl:
        ydl.download([vidinfo['webpage_url']])
    
