import os
import glob
from pathlib import Path
import shutil
import datetime as dt

textures = open("textures_new.ini", "a")
wildcard = "00000000"
uFiles = glob.glob('*png')
path = '../gigapixel/'

#date = dt.datetime.now()
#updated = "[{} @ {}]".format(date.strftime("%x")[:5],date.strftime("%I:%M%p"))
#textures.write(updated)
exceptions = []
for uFile in uFiles:
	s=str(uFile)
	print(uFile)
	textures.write(s[:24]+' = gigapixel/'+s)
	textures.write("\n")
	#try:
#		shutil.move(uFile, path)
#		print(uFile+" copied to upscale folder.")
	#except:
#		exceptions.append(uFile)
#
#try:
#	for exception in exceptions:
#		print(exception+" already exists.")
#except:
	#print("No duplicates found.")

#print("File copying completed")
