with open("1.txt") as file:
	# join lines with '+' and remove \n
	cont = "+".join(file.readlines()).replace('\n', "")

# when "++", split
cont = cont.replace("++", ",")[:-1]

elfs = sorted(eval(cont))[::-1]

print("top:", elfs[0])
print("top 3:", sum(elfs[0:3]))


