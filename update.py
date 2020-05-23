import requests as rq

def update(url="https://github.com/GandelXIV/dialogic/blob/master/exe/dialogic.exe?raw=true"):
	r = rq.get(url)
	#print(r.content)
	
	with open("dialogic.exe","wb") as f:
		f.write(r.content)
		

