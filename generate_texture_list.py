  
import os
import glob
import initialize_database as tdb
import numpy as np


imageList = np.asarray(tdb.getImageList())
imgcnt=0
while imgcnt < 5120:
	tdb.generate_textures_ini(imageList[imgcnt])
	#tdb.organize(imageList[imgcnt])
	imgcnt+=1

