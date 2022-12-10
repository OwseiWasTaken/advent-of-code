PARTONE = False

with open("3.txt", "r") as file: cont = file.read().splitlines();

t = 0

from string import ascii_uppercase, ascii_lowercase

def ItemToNice(char):
	if char.islower():
		return ascii_lowercase.index(char)+1
	return ascii_uppercase.index(char)+27

def CountIn(lst, target):
	return sum([item == target for item in lst])

if PARTONE:
	for line in cont:
		a,b=line[:len(line)//2], line[len(line)//2:]

		for r in a:
			if r not in b:
				continue
			t+=ItemToNice(r)
			break
else:
	assert not len(cont)%3
	for i in range(len(cont)//3):
		lines = list(map(list, map(set, cont[i*3:i*3+3])))
		# can't use sum :(
		line = lines[0]+lines[1]+lines[2]
		ld = {}
		for char in line:
			ld[char] = ld.get(char, 0)+1
		# invert map [count]string and [3] -> group's item
		group = {v: k for k, v in ld.items()}[3]
		t+=ItemToNice(group)


print(t)
