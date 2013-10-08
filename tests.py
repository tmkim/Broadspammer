with open('testxt') as f:
	name = []
	num = []
	for line in f:
		name.append([str(x) for x in line.split()])
		num.append([str(x) for x in line.split()])
	for x in name:
		print x[0] + " " + x[1]
