import sys,os
from dataprep import prepare,readFile
from threading import Thread

url = "https://github.com/GandelXIV/dialogic/tree/master/exe/dialogic.exe"

class Dialog:
	def __init__(self,dialog,blocking=True):
		self.dialog = prepare(dialog)
		if "root" not in self.dialog:
			print("[!]Internal error!")
			print("[!]Errno: 2:no @root state!")
			self.running = False
			return
		self.pos = "root"
		self.action = ""
		self.running = True
		self.blocking = blocking
	def draw(self):
		text = self.dialog[self.pos]
		jumpLines =0
		linen = 0
		for line in text:
			linen += 1
			if jumpLines == 0:
				if line[0:4] == "/ask":
					if self.blocking:
						self.act()
					else:
						while self.action == "":
							pass
				elif line[0:4] == "/if ":
					if line[4:] != self.action:
						jumpLines += 1
				elif line[0:5] == "/2if ":
					if line[5:] != self.action:
						jumpLines += 2
				elif line[0:5] == "/3if ":
					if line[5:] != self.action:
						jumpLines += 3
				elif line[0:5] == "/4if ":
					if line[5:] != self.action:
						jumpLines += 4
				elif line[0:5] == "/5if ":
					if line[5:] != self.action:
						jumpLines += 5
				elif line[0:4] == "/go ":
					dest = line[4:]
					if dest in self.dialog:
						self.pos=dest
					else:
						self.error(linen,"1:State do not exist!")
				elif line[0:4] == "/end":
					self.running = False
					return
				else:
					if line != "":
						print(line)
			else:
				jumpLines -= 1
	def error(self,linen,error):
		print("[!]Error! in",self.pos,"line",linen)
		print("[!]Errno:",error)
		self.running = False
		return
	def act(self):
		self.action = input()

def run(dg):
	while dg.running:
		dg.draw()
if __name__ == "__main__":
	while True:
		file = input("Enter file:")
		try:
			dg = Dialog(readFile(file))
			run(dg)
		except:
			print("Could not run file!")
		
