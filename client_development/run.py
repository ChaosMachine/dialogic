
# ALWAYS UPDATING! ERROR

print("Loading...")
import update
import requests as rq
import os
print("Searching for version.txt...")
try:
    v = open("version.txt","r")
    print("version.txt found!")
except:
    print("[!]Could not find version.txt")
try:
    print("Connecting to update server...")
    version = rq.get("https://raw.githubusercontent.com/GandelXIV/dialogic/master/client/version.txt").content
    print("Connected!")
    print(v.read())
    if v.read() != version:
        print("New version!")
        print("Downloading...")
        update.update("https://github.com/GandelXIV/dialogic/blob/master/exe/dialogic.exe?raw=true","dialogic.exe")
        print("Downloaded!")
        v.close()
        print("Updating version.txt...")
        v = open("version.txt","wb")
        v.write(version)
        print("Done!")
        v.close()
except:
    print("[!]Could not update!")
print("Starting dialogic.exe...")
os.startfile("dialogic.exe")
