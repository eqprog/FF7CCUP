  
import os
import glob
import initialize_database as tdb
import numpy as np


imageList = np.asarray(tdb.getImageList())
for i in range(imageList.shape[0]):
	attr=tdb.get(imageList[i])
	str=attr[9]
	if not str.startswith('./textures/ignore/'):
		tdb.generate_textures_ini(imageList[i])
	else:
		pass

	#tdb.organize(imageList[imgcnt])


