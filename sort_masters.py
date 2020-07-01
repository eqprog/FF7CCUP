import os
import glob
import initialize_database as tdb
import numpy as np
import sqlite3
import shutil


imageList = np.asarray(tdb.getImageList("textures"))

for i in range(imageList.shape[0]):
	tx_attributes = tdb.get(imageList[i])
	dest="./masterdumps/"+tx_attributes[9][11:]+tx_attributes[0]
	src="./masterdumps/"+tx_attributes[0]
	print(src+"\n")
	print(dest+"\n")
	try:
		shutil.copyfile(src, dest)
		print(tx_attributes[0]+" copied to " + dest)
	except:
		print("Could not copy "+tx_attributes[0])

