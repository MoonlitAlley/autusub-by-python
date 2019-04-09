import os, shutil

def GetFileList(dir , fileList , notdeal=[]):
	newDir = dir
	if os.path.isfile(dir):
		#only deal with the .mp4 file
		if os.path.splitext(dir)[1]==".mp4":
			fileList.append(dir)
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			#if there is other file unnecessary process
			if s in notdeal:
				continue

			newDir = os.path.join(dir , s)
			GetFileList(newDir , fileList , notdeal)
	
	return fileList #get a list contaiin the filename and filepath

def moveFileToTempDir(filename):
	#move the file to tempdir if noexist create it
	retname='\\\\'
	names = filename.split('\\')
	for i in range(len(names)-1):
		if names[i]=="":
			continue
		if names[i] == "gdc":
			retname = os.path.join(retname , names[i])
			retname = os.path.join(retname , "gdcaudioM4adir")
		else:
			retname = os.path.join(retname , names[i])
	if os.path.exists(retname)==False:
		os.makedirs(retname)
	retname = os.path.join(retname , names[len(names)-1])
	#if there is a file of conflict name ,input /y parameter
	shutil.move(filename , retname)

def existsfile(filename):
	
	retname='\\\\'
	names = filename.split('\\')
	for i in range(len(names)-1):
		if names[i]=="":
			continue
		if names[i] == "gdc":
			retname = os.path.join(retname , names[i])
			retname = os.path.join(retname , "gdcaudioM4adir")
		else:
			retname = os.path.join(retname , names[i])

	retname = os.path.join(retname , names[len(names)-1])	
	if os.path.isfile(retname)==False:
		return False
	return True
	
gdclist = [
	'gdc vault 2009',
	'gdc vault 2010',
	'gdc vault 2011',
	'gdc vault 2012',
	'gdc vault 2013',
	'gdc vault 2014',
	'gdc vault 2015',
	'gdc vault 2016',
	'gdc vault 2017',
	'gdc vault 2018',
	'gdc vault 2019',
]
rootpath = r'E:\gdc'
targetpath = r'E:\gdc\gdcaudioM4adir'
for i in range(len(gdclist)):
	filepath = os.path.join(rootpath , gdclist[i])
	filelists = GetFileList(filepath,[],[])
	resultlists=[]
	for i in range(len(filelists)):
		resultlists.append(os.path.splitext(filelists[i])[0])
		resultlists[i] =resultlists[i].replace(rootpath,targetpath)
		
		if(not existsfile(resultlists[i]+'.m4a')):
			#creat a fold of resultlists
			names = resultlists[i].split('\\')
			temppath = resultlists[i].replace(names[len(names)-1] ,"")
			os.makedirs(temppath)
			os.system(r'ffmpeg -i "%s" -vn -acodec copy "%s"' %(filelists[i],resultlists[i]+'.m4a')) #python's format print
