try:
  print("Convert Started\n")
	with open('1.ass','r',encoding='utf-8') as f1,open('1.ass.lrc', 'w', encoding='utf-8') as f2: //change input and output files
		for line in f1.readlines():
			a = line.strip()
			f2.write("[" + a[a.find(",") + 3:a.find(",") + 11] + "]" + a[a.find("}") + 1:] + "\n")
	print("Convert Completed\n")
except:
	print("Convert Failed")
