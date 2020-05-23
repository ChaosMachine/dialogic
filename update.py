import requests as rq

def update(url):
	r = rq.get(url)
	#print(r.content)
	
	with open("dialogic.exe","wb") as f:
		f.write(r.content)
		
if __name__ == "__main__":
	update("https://github.com/GandelXIV/dialogic/blob/master/exe/dialogic.exe?raw=true")