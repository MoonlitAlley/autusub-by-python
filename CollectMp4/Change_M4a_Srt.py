import os, shutil

def GetFileList(dir , fileList , notdeal=[]):
	newDir = dir
	if os.path.isfile(dir):
		#only deal with the .mp4 file
		if os.path.splitext(dir)[1]==".m4a":
			fileList.append(dir)
			print "add a .m4a file to the list waiting process"
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			#if there is other file unnecessary process
			if s in notdeal:
				continue
			newDir = os.path.join(dir , s)
			GetFileList(newDir , fileList , notdeal)

	return fileList #get a list contaiin the filename and filepath

def moveFileToTargetDir(filename):
	#move the file to tempdir if noexist create it
	retname='\\\\'
	names = filename.split('\\')
	for i in range(len(names)-1):
		if names[i]=="":
			continue
		if names[i] =="gdcaudioM4adir":
			#skip the gdcaudioM4adir get the origin path
			continue
		else:
			retname = os.path.join(retname , names[i])
	if os.path.exists(retname)==False:
		return
	retname = os.path.join(retname , names[len(names)-1])
	#if there is a file of conflict name ,input /y parameter
	shutil.move(filename , retname)

def existsfile(filename):
	retname='\\\\'
	names = filename.split('\\')
	for i in range(len(names)-1):
		if names[i]=="":
			continue
		if names[i] =="gdcaudioM4adir":
			#skip the gdcaudioM4adir get the origin path
			continue
		else:
			retname = os.path.join(retname , names[i])
	retname = os.path.join(retname , names[len(names)-1])
	if os.path.isfile(retname)==False:
		return False
	return True

filepath = r'\\soft.h3d.com.cn\tac\gdc\gdcaudioM4adir'
filelists = GetFileList(filepath,[],[])
resultlists=[]
for i in range(len(filelists)):
	#to deal with the data
	#resultlists.append(filelists[i].split('.')[0]) #lists store the file's whole name, use split to get the filename without it's Extension name

	#because the server filesystem begin with soft.h3d.com.cn
	resultlists.append(filelists[i].split('.')[0]+'.'+filelists[i].split('.')[1]+'.'+filelists[i].split('.')[2]+'.'+filelists[i].split('.')[3])
	#lists store the file's whole name, use split to get the filename without it's Extension name

for i in range(len(filelists)):
	#if there is't a Srt file in the target path
	print "start to process the "+str(i)+"th .m4a to .Srt file"
	if(not existsfile(resultlists[i]+'.Srt')):
		if os.path.isfile(resultlists[i]+'.Srt') == False:
			os.system(r'autosub "%s"' %(filelists[i])) #python's format print
		#submit to Google Speech API get a .Srt file
		print filelists[i]
		#os.system(r'autosub "%s"' %(filelists[i])) #python's format print
		#move the Srt file to origin path
		moveFileToTargetDir(resultlists[i]+'.Srt')
		#remove the temp audio file
		os.remove(filelists[i])
	else:
		print "already be there"