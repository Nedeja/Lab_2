line = '"#15SecondScare\" (2015) {Who Wants to Play with the Rabbit? (#1.2)}	West Hills, California, USA	(interior scenes)'
lst = []
ind = line.find('(')
ind1 = line[ind + 1:].find('(')
line.replace(line[ind1:], "")
lst.append(line.strip().split())
print(lst)