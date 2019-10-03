try:
	count = 0
	with open('2.ass','r',encoding='utf-8') as f1,open('2.ass.srt', 'w', encoding='utf-8') as f2:
		for line in f1.readlines():
			count = count + 1
			a = line.strip()
			f2.write(str(count) + "\n" + a[a.find(",") + 1:a.find(",") + 11] + " --> " + a[a.find(",") + 12:a.find(",") + 22] + "\n" + a[a.find("}") + 1:] + "\n\n")
	count = 0
	print("")
except:
	print("")
