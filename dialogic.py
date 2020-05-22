import sys,os
from dataprep import prepare,readFile
from threading import Thread

class Dialog:
	def __init__(self,dialog):
		self.dialog = prepare(dialog)
		self.pos = "init"
		self.action = ""
		self.running = True
	def draw(self):
		text = self.dialog[self.pos]
		jumpLines =0
		for line in text:
			if jumpLines == 0:
				if line[0:5] == "/wait": # BROKEN.
					self.act()
				elif line[0:4] == "/if ":
					if line[4:] != self.action:
						jumpLines += 1
				elif line[0:4] == "/go ":
					#print(14)
					self.pos=line[4:]
				elif line[0:4] == "/end":
					self.running = False
					return
				else:
					if line != "":
						print(line)
			else:
				jumpLines -= 1
	def act(self):
		self.action = input()

def run(dg):
	while dg.running:
		dg.draw()
if __name__ == "__main__":
	while True:
		file = input("Enter file:")
		dg = Dialog(readFile(file))
		print(dg.dialog)
		run(dg)
