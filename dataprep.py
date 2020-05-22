def readFile(filename):
	with open(filename,"r") as f:
		return f.readlines()
def parse(content):
	res = {}
	word = ""
	last = ""
	for line in content:
		if line[0] == "$":
			if last != "":
				res[last] = word
				word = ""
			last = line[1:-1]
		else:
			word += line
	res[last] = word
	return res
def cleaN(content):
	for _ in content:
		content[_] = content[_].split("\n")
	return content
def unspace(content):
	for _ in content:
		l = content[_]
		for i in range(len(l)-1):
			if l[i] == " " or l[i] == "":
				l.pop(i)
		content[_] = l
	return content

def prepare(content):
	content = parse(content)
	content = cleaN(content)
	#content = unspace(content)
	return content