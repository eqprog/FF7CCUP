import os
import glob
from pathlib import Path
import shutil
import datetime as dt

textures = open("textures.ini", "a")
wildcard = "00000000"
uFiles = glob.glob('./video_ignore/*png')

date = dt.datetime.now()
updated = "#{} @ {}#".format(date.strftime("%x")[:5],date.strftime("%I:%M%p"))
textures.write(updated)
textures.write("\n")

for uFile in uFiles:
	s=str(uFile)
	print(uFile)
	textures.write(s[15:-4]+' =')
	textures.write("\n")

print("Texture Ignore List generated")
