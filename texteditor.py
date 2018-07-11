'''Simple Text Editor'''

option=input('''Please enter your choice,
1) Read a File
2) Write/Append to a File
3) Rename
4) Exit''')

redirect={1:readfile, 2:writetofile, 3: renamefile, 4:exit}
getuserin= redirect.get(option)
getuserin()

def readfile():
	'''Reads and prints the contents of given file'''
	filename= input('Enter the file name: ')
	try:
		with open("D:\Learning\Python\Basics\\new4.txt","r") as f:
			print(f.read())
	except FileNotFoundError:
		print('The file you have specified is not found.')
		
def writetofile():
	'''Writes the user given content to specified file'''
	filename= input('Enter the file name: ')
	filedata=input('Please enter the file contents. To Exit, enter :wq')
	file=open("D:\Learning\Python\Basics\\"+filename+"","a")
	flag=True
	while(flag):
		filedata=input('')
		if filedata.find(':wq')<0:
			file.writelines(filedata+'\n')
		else:
			file.writelines(filedata.strip(':wq')+'\n')
			break
	file.close()

def renamefile():
	'''Renames the given file to another'''
	oldfile=input('Enter the file  which has to be renamed ')
	newfilename= input('Enter the new file name')
	file=open()