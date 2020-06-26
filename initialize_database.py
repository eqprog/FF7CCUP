from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import sqlite3
import os
import glob
import numpy as np
import shutil



def test_db():
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    c.execute("SELECT *, filename FROM textures")
    print(c.fetchall())
    conn.close()

def initialize_db():
    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS textures (
        filename text PRIMARY KEY,
        gname text,
        width integer,
        height integer,
        category text,
        text_element integer,
        shinra_logo integer,
        use_esrgan integer,
        ignore integer
        )""")
    c.execute("""CREATE TABLE IF NOT EXISTS saved (filename text)""")

    conn.commit()
    conn.close()

def entry_exists(file=""):
    filename=file[13:-4]
    conn=sqlite3.connect('textures.db')
    c = conn.cursor()
    c.execute("SELECT * FROM textures WHERE filename=?",(filename,))
    conn.close()
    return c.fetchall()

def get(file):
    filename=file
    attributes = []
    conn=sqlite3.connect('textures.db')
    conn.row_factory = sqlite3.Row
    c=conn.cursor()
    c.execute("SELECT * FROM textures WHERE filename=?", (filename,))
    result = c.fetchone()
    conn.close()
    return result[0:11]
    """if not result:
        print("Adding file to DB: "+filename)
        my_img = ImageTk.PhotoImage(Image.open(file))
        addRecord(file)
        attributes = [file, file, my_img.width(), my_img.height(), "New", 0,0,0,0]
    else:
        print(result)
        for attr in result:
            for i in range(0, 9):
                attributes.append(attr[i])
    return attributes"""
    
def addRecord(conn, file, width, height):
    c=conn.cursor()
    try:
        c.execute("""INSERT INTO textures VALUES (:filename, :gname, :width, :height, :category,
                  :text, :shinra, :esrgan, :ignore)""",
                {
                    'filename': file,
                    'gname': file,
                    'width': width,
                    'height': height,
                    'category': "New",
                    'text': 0,
                    'shinra': 0,
                    'esrgan': 0,
                    'ignore': 0
                })
        conn.commit()
        print(file+" added to database")
    except: print("Entry exists: "+file)
    

def getNewTextures():
    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    os.chdir("./masterdumps")
    imageList=[]

    print(os.getcwd())
    for png in glob.glob("*.png"):
        imageList.append(png)
        my_img = ImageTk.PhotoImage(Image.open(png))
        addRecord(conn, png, my_img.width(), my_img.height())
    os.chdir("..")
    print(os.getcwd())
    conn.close()

def updateRecord(attr, file):
    
    filename=file[13:]
    attributes=attr
    #print(attributes)
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    c.execute("""UPDATE textures SET gname = ?, category = ?, text_element = ?, shinra_logo = ?, use_esrgan = ?,
                ignore = ? WHERE filename = ?""", attributes)
    conn.commit()
    conn.close()
    


def save(position):
    print(os.getcwd())
    filename=position

    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    try:
        c.execute("""UPDATE saved SET filename = ? WHERE oid = 1""", (filename, ))
        print("position saved @ "+filename)
    except:
        print("couldn't save")
    conn.commit()
    conn.close()
def save_init(position):
    print(os.getcwd())
    filename=position

    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    try:
        c.execute("""INSERT INTO saved SET filename = ? WHERE oid = 1""", (filename, ))
        print("position saved @ "+filename)
    except:
        print("couldn't save")
    conn.commit()
    conn.close()


def get_save():
    print(os.getcwd())
    #print("GETTING SAVE NOW")

    conn = sqlite3.connect('textures.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("""SELECT *  FROM saved WHERE oid=1""")
    #print("PRINTING FETCHED POSITION \n")
    result = c.fetchone()
    #print(result['filename'])
    conn.close()
    for item in result:
        #print("2 "+result['filename'])
        return result['filename']
def getImageList():
    tx_list =  []
    conn=sqlite3.connect('textures.db')
    conn.row_factory = sqlite3.Row
    c=conn.cursor()
    c.execute("SELECT * FROM textures")
    results = c.fetchall()
    for result in results:
        tx_list.append(result['filename'])
    conn.close()
    return tx_list
    #return result['filename']
    #conn.commit()
    #conn.close()
def convertIndex(sav_pos):
    return int(str(sav_pos[0])[1:-1])

def addDefaultPath():
    characters="./textures/characters/"
    environment="./textures/environment/"
    conn = sqlite3.connect('textures.db')
    c=conn.cursor()
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? OR  category = ? OR text_element = 1 OR shinra_logo = 1""", (("./textures/priority/", "Ground/Wall, fix trans.", "Ground/Wall, needs rivets")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", (("./gigapixel/", "New")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"aerith/", "Aerith")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"angeal/", "Angeal")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"cissnei/", "Cissnei")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"cloud/", "Cloud")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"enemy/", "Enemy")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"genesis/", "Genesis")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"hollander/", "Hollander")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"lazard/", "Lazard")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"npc/", "NPC")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"sephiroth/", "Sephiroth")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"tifa/", "Tifa")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"tseng/", "Tseng")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"yuffie/", "Yuffie")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"zack - 1st Class/", "Zack - 1st Class")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"zack - 2nd Class/", "Zack - 2nd Class")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? AND text_element = 0 AND shinra_logo = 0""", ((characters+"zack - Buster Sword/", "Zack - Buster Sword")))


    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"artwork/", "Artwork")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? OR category = ?""", ((environment+"object/", "Metallic", "Object/Prop")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"sign/", "Sign/Decal")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"ground/", "Ground")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"wall/", "Wall")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"foliage/", "Foliage")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", ((environment+"skybox/", "Skybox/BG")))


    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", (("./textures/ignore/map/", "Map")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ?""", (("./textures/ignore/effects/", "Fog, etc.")))
    c.execute("""UPDATE textures SET upPath = ? WHERE category = ? OR ignore = 1""", (("./textures/ignore/", "UI")))
    c.execute("""UPDATE textures SET initPath = upPath""", )
    conn.commit()
    conn.close()

def organize(file):
    tx_attributes = get(file)
    if tx_attributes[4] != "New" or tx_attributes[4] != "UI":
        try:
            shutil.move("./gigapixel/"+tx_attributes[0], tx_attributes[9]+tx_attributes[0])
            #print(tx_attributes[0]+" moved to "+tx_attributes[9])
        except:
            try:
                shutil.move(tx_attributes[10]+tx_attributes[0], tx_attributes[9]+tx_attributes[0])
                #print(tx_attributes[0]+" moved to "+tx_attributes[9])
            except:
                print("This file is not in its correct location, maybe! " + tx_attributes[0])
    else:
        print("!!!! WARNING IMAGE NOT CATEGORIZED !!!")

def generate_textures_ini(file):
    texturesini = open("add_textures.ini", "a")
    
    tx_attributes = get(file)
    filehash = tx_attributes[0]
    path=tx_attributes[9]
    if tx_attributes[4] !="UI" or not tx_attributes[8]:
        texturesini.write(filehash[0:24] + " = "+path[1:]+tx_attributes[0]+"\n")