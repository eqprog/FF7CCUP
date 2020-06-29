import os
import initialize_database as tdb
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3
import os
import glob
import numpy as np
import shutil

root = Tk()

images = []

#tdb.initialize_db()

tdb.getNewTextures()
imageList = np.asarray(tdb.getImageList())

for i in range(imageList.shape[0]):
	tx_attributes = tdb.get(imageList[i])
	tdb.addCatRecord(tx_attributes)

