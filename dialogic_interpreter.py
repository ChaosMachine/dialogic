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
		noread = 0
		for line in text:
				if line[0:5] == "/wait": # BROKEN.
					self.act()
				elif line[0:4] == "/go ":
					print(14)
					self.pos=line[4:]
				elif line[0:4] == "/end":
					self.running = False
					return
				else:
					print(line)
	def act(self):
		if self.running:
			self.action = input()
	def run(self):
		while self.running:
			self.draw()
			if not self.running:
				break
			self.act()
			if not self.running:
				break
if __name__ == "__main__":
	file = input("Enter file:")
	dg = Dialog(readFile(file))
	dg.run()
