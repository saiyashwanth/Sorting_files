import os                          
import shutil                      #To do operations like moving files into folder

#path = '/home/mlritm/Downloads/' 
path = os.getcwd()                  #Declaring the path of the folder where you want to do sorting

names = os.listdir(path)

folder = ['PDF','PPT','Image']							#We are specifying Folder names

for x in range(0,3):
	if not os.path.exists(path + folder[x]):			#To check whether the foldewr is already exist or not
		os.makedirs(path + folder[x])					#Making Folders

for files in names:
	if ".png" in files and not os.path.exists(path + 'Image/' + files):   #to avoid to prevent copying same files multiple time
		shutil.move(path + files, path + 'Image/' + files)
	if ".pdf" in files and not os.path.exists(path + 'PDF/' + files):
		shutil.move(path + files, path + 'PDF/' + files)
	if ".ppt" in files and not os.path.exists(path + 'PPT/' + files):
		shutil.move(path + files, path + 'PPT/' + files)