from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
import glob
import initialize_database as tdb
import numpy as np
import evaluator as e



"""imageList = []
for png in glob.glob("*.png"):
    imageList.append(png)"""

"""class Evaluator:
    def __init__(self, """


################################################## CREATE WINDOW ###############################################

root = Tk()

tdb.initialize_db()
tdb.getNewTextures()

root.title("FF7CCUP Evaluator")
root.geometry("1918x1000+0+0")

################################################## INITIALIZE VARIABLES ########################################

imgcnt=0

#table attributes {filename, givename, width, height, category, text, shinra logo, use esrgan, ignore
imageList = np.asarray(tdb.getImageList())
print(imageList[0])
try:
	tdb.get_save()
except:
	tdb.save_init(imageList[0])

#saveresult=tdb.get_save()


############################### CHECK IF RECORD EXISTS, IF NOT ADD ENTRY ######################################
#tx_attributes=tdb.get(imageList[imgcnt])

sav_pos=np.where(imageList==tdb.get_save())
imgcnt=tdb.convertIndex(sav_pos)
#imgcnt=int(imgcnt[1:-1])
print(imgcnt)
print(imageList[imgcnt])

tx_attributes=tdb.get(tdb.get_save())

print(tx_attributes)
#imgcnt=np.where(imageList==sav_pos)
#print(tx_attributes)

################################################# CREATE LEFT FRAME ###########################################

evaluator = e.Evaluator(root, imageList[imgcnt], tx_attributes)

################################################# DISPLAY ORIGINAL TEXTURE ####################################

evaluator.display_original()

  
        
################################################# EVALUATION FRAME ############################################

evaluator.eval_frame()

################################################# DISPLAY UPSCALED ############################################

evaluator.display_upscale()

def prev_image(event):
    global imgcnt
    tdb.updateRecord(evaluator.write_record(), imageList[imgcnt])
    tdb.save(imageList[imgcnt])
    if imgcnt > 0:
        imgcnt -= 1
        tx_attributes=tdb.get(imageList[imgcnt])
        evaluator.update_frames(imageList[imgcnt], tx_attributes)

    print("#"+str(imgcnt)+": "+imageList[imgcnt])

    
def next_image(event):
    global imgcnt
    
    tdb.save(imageList[imgcnt])
    if imgcnt < len(imageList):
        tdb.updateRecord(evaluator.write_record(),imageList[imgcnt])
        imgcnt += 1
        tx_attributes=tdb.get(imageList[imgcnt])
        evaluator.update_frames(imageList[imgcnt], tx_attributes)

    print("#"+str(imgcnt)+": "+imageList[imgcnt])
    #root.update()


#navigation buttons VVVVV

button_Prev=Button(evaluator.return_left(), text="Prev")
button_Prev.pack(side=BOTTOM, fill=X)
button_Prev.bind('<Button-1>', prev_image)
root.bind('<Left>', prev_image)

button_Next=Button(evaluator.return_left(), text="Next")
button_Next.pack(side=BOTTOM, fill=X)
button_Next.bind('<Button-1>', next_image)
root.bind('<Right>', next_image)

evaluator.drawOpen()


root.mainloop()

    

