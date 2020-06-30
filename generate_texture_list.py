  
import os
import glob
import initialize_database as tdb
import numpy as np


imageList = np.asarray(tdb.getImageList())
for i in range(imageList.shape[0]):
	tdb.generate_textures_ini(imageList[i])
	#tdb.organize(imageList[imgcnt])


