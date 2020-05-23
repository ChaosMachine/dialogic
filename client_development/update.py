import requests as rq
import base64
def update(url,file):
	r = rq.get(url)
	#print(r.content)
	
	with open(file,"wb") as f:
		f.write(r.content)

