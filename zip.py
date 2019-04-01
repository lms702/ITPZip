import sys, zipfile, os, shutil
def main():
	file = sys.argv[1]
	ifile = open(file, 'r')
	for i in range(0, 3):
		line = ifile.readline()
		if i == 1:
			continue
		line = line.strip('# \n')
		lineArr = line.split()
		if i == 0:
			if len(lineArr) != 2:
				print('Name line length error')
				quit()
			fname = lineArr[0]
			lname = lineArr[1]
		elif i == 2:
			if len(lineArr) != 2:
				print('Assignment line length error')
				quit()
			if lineArr[0].lower() == 'assignment':
				filetype = 'a'
			elif lineArr[0].lower() == 'lab':
				filetype = 'l'
			else:
				print('Assignment type error')
				quit()
			assignmentNum = lineArr[1]
	ifile.close()

	newName = 'ITP115_' + filetype + assignmentNum + '_' + lname + '_' + fname
	shutil.copy(file, newName + '.py')
	ofile = zipfile.ZipFile(newName + '.zip', 'w')
	ofile.write(newName + '.py')
	for i in range(2, len(sys.argv)):
		print(str(i))
		ofile.write(sys.argv[i])
	ofile.close()
	os.remove(newName + '.py')
main()