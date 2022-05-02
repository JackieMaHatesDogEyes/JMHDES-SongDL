import youtube_dl
import urllib.request
import re
from pydub import AudioSegment
from time import sleep

version = "0.0.3" #Current Application Version
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

m4a = False
inp = input("Keep MP3 Format? (y/n)")
if inp == "N" or "n":
    m4a = True

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

    vidinfo = youtube_dl.YoutubeDL().extract_info(
        url = vidurl,download=False
    )

    fname = f"{vidinfo['title']}.mp3"
    o ={

        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':fname
    }

    with youtube_dl.YoutubeDL(o) as ydl:
        ydl.download([vidinfo['webpage_url']])
    
    if m4a:
        audioFile = AudioSegment.from_file(fname, format="m4a")
        audioFile.export(f"{vidinfo['title']}.m4a", format="m4a")
        print("Conversion Finished")
