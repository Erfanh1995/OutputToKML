import simplekml


file = open("kharita_output.txt", 'r')
savior = []
count = 0

for line in file:
	count += 1

	if line != "\n":
		a = line.split(",")
		a[1]=a[1][:-2]
		savior.append((float(a[0]),float(a[1])))

print(savior)

kml = simplekml.Kml()
for i in range(count//2):
	kml.newlinestring(coords=[savior[i],savior[i+1]])

kml.save("output.kml")

