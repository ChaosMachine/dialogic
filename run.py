import update
import requests as rq
import os

v = open("version.txt","r")

#try:
version = rq.get("https://raw.githubusercontent.com/GandelXIV/dialogic/master/client/version.txt").content
if v.read() != version:
    update.update("https://github.com/GandelXIV/dialogic/blob/master/exe/dialogic.exe?raw=true","dialogic.exe")
    v.close()
    v = open("version.txt","wb")
    v.write(version)
    v.close()
"""
except:
    print("[!]Could not update!")
"""
os.startfile("dialogic.exe")
