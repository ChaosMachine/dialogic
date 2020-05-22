import sys,os
from dataprep import prepare,readFile

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
					return
				elif line[0:4] == "/go ":
					self.pos=line[4:]
				elif line[0:4] == "/end":
					running = False
				else:
					print(line)
	def act(self,action):
		self.action = str(action)
	def run(self):
		while self.running:
			self.draw()
			self.act(input(">>>"))
			print(self.action)

if __name__ == "__main__":
	file = input("Enter file:")
	dg = Dialog(readFile(file))
	dg.run()
