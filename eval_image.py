from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os
import glob
import initialize_database as tdb
import numpy as np
import evaluator as e
import threading
#import selectFilter as sf

cat_filter = "Foliage"
root = Tk()
root.title("FF7CCUP Evaluator")
root.geometry("1918x1000+0+0")
splash_img = ImageTk.PhotoImage(Image.open("evaluator.png"))
def prev_image(event):
    global imgcnt
    global imageList
    global evaluator
    global cat_filter
    old_cat=tdb.defineCategory(tdb.get(imageList[imgcnt]))
    print("old category: "+old_cat)
    tdb.updateRecord(evaluator.write_record(), imageList[imgcnt])
    tdb.addDefaultPath(imageList[imgcnt])
    new_cat=tdb.defineCategory(tdb.get(imageList[imgcnt]))
    print("new category: "+new_cat)
    if (old_cat!=new_cat): 
        tdb.deleteCatRecord(tdb.get(imageList[imgcnt]), old_cat)
        tdb.addCatRecord(tdb.get(imageList[imgcnt]), new_cat)
    else:
        tdb.addCatRecord(tdb.get(imageList[imgcnt]), new_cat)
    tdb.organize(tdb.get(imageList[imgcnt]))
    
    tdb.updateInitPath()
    imageList = np.asarray(tdb.getImageList(cat_filter))
    #tdb.organize(imageList[imgcnt])
    if imgcnt > 0:
        imgcnt -= 1
        tx_attributes=tdb.get(imageList[imgcnt])
        evaluator.update_frames(imageList[imgcnt], tx_attributes)
    tdb.save(imageList[imgcnt], cat_filter)
    #print("#"+str(imgcnt)+": "+imageList[imgcnt])
    print("\n")

    
def next_image(event):
    global imgcnt
    global imageList
    global evaluator
    global cat_filter
    old_cat=tdb.defineCategory(tdb.get(imageList[imgcnt]))
    print("old category: "+old_cat)
    tdb.updateRecord(evaluator.write_record(),imageList[imgcnt])
    tdb.addDefaultPath(imageList[imgcnt])
    new_cat=tdb.defineCategory(tdb.get(imageList[imgcnt]))
    print("new category: "+new_cat)
    if (old_cat!=new_cat):
        tdb.deleteCatRecord(tdb.get(imageList[imgcnt]), old_cat)
        tdb.addCatRecord(tdb.get(imageList[imgcnt]), new_cat)
        imageList = np.asarray(tdb.getImageList(cat_filter))
        
    else:
        tdb.addCatRecord(tdb.get(imageList[imgcnt]), new_cat)
    tdb.organize(tdb.get(imageList[imgcnt]))
    #tdb.addDefaultPath(imageList[imgcnt])
    #tdb.organize(imageList[imgcnt])
    
    tdb.updateInitPath()
    if imgcnt < len(imageList)-1:
        
        imgcnt += 1
        tx_attributes=tdb.get(imageList[imgcnt])
        evaluator.update_frames(imageList[imgcnt], tx_attributes)
    tdb.save(imageList[imgcnt], cat_filter)
    #print("#"+str(imgcnt)+": "+imageList[imgcnt])
    print("\n")

    #root.update()
def goButt(category):
    print("Go!!!!!")
    return category.get()

def main():

    #thread=threading.Thread(target=splash_frame)
    #thread.start()
    #thread.join()
    ################################################## CREATE WINDOW ###############################################
    global root
    global imageList
    global imgcnt
    global evaluator
    global cat_filter
    splash_img = ImageTk.PhotoImage(Image.open("evaluator.png"))

    splashFrame = Frame(root, width = 960)
    splashFrame.pack(side=LEFT, anchor=N)
    splash_label=Label(splashFrame, image=splash_img)
    splash_label.pack(side=TOP, anchor=CENTER)
    selection_label=Label(splashFrame, text= "Select a category:")
    selection_label.pack(side=TOP, anchor=CENTER)

    optionList=["New", "Priority", "Sign/Decal", "Artwork", "Ground", "Wall", "Object/Prop", "Skybox/BG", "NPC", "Enemy", "Foliage", 
                    "Zack - 2nd Class", "Zack - 1st Class", "Zack - Buster Sword", "Aerith", "Cissnei", "Tseng", "Angeal", "Genesis", "Hollander", "Lazard", "Sephiroth", "Cloud", "Tifa", "Yuffie", "Ignore"]


    category = StringVar()
    goVar=StringVar()
    #goVar.set("New")
    category.set("New")    
        #optionconvert = (0, 0, 0, 0, i, 0, 0, 0, 0, 0)
    catLabel = OptionMenu(splashFrame, category, *optionList)
    catLabel.pack(side=TOP, anchor=CENTER, fill=X)
    #goButton = Button(splashFrame, text="GO!", width=100, pady=100, command=category.set(str(goVar.get())))
    #goButton.pack(side=BOTTOM)
    print("waiting for category selection")
    #print(goVar)
    catLabel.wait_variable(category)

    cat_filter = tdb.defineCategory([0,0,0,0,category.get(),0,0,0,0,0])
    print("cat filter: "+cat_filter)
    splashFrame.destroy()

    tdb.initialize_db()
    #tdb.getNewTextures()



    ################################################## INITIALIZE VARIABLES ########################################

    imgcnt=0

    #table attributes {filename, givename, width, height, category, text, shinra logo, use esrgan, ignore
    
    imageList = np.asarray(tdb.getImageList(cat_filter))
    #print(imageList)
    #try:
    #    tdb.get_save()
    #except:
    #    tdb.save_init(imageList[0])
    #finally:
    #    tdb.get_save()

    ############################### CHECK IF RECORD EXISTS, IF NOT ADD ENTRY ######################################

    sav_pos=np.where(imageList==tdb.get_save(cat_filter))
    print(sav_pos[0])
    print("\n")
    imgcnt=tdb.convertIndex(sav_pos)
    tx_attributes=tdb.get(tdb.get_save(cat_filter))

    ################################################# CREATE LEFT FRAME ###########################################

    evaluator = e.Evaluator(root, imageList[imgcnt], tx_attributes)

    ################################################# DISPLAY ORIGINAL TEXTURE ####################################

    evaluator.display_original()
            
    ################################################# EVALUATION FRAME ############################################

    evaluator.eval_frame()

    ################################################# DISPLAY UPSCALED ############################################

    evaluator.display_upscale()
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

if __name__ == '__main__':
    main()    

