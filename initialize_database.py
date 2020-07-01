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
    return result[0:12]
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
        c.execute("""INSERT INTO textures VALUES (:filename, :gname, :width, :height, :category, :text, :shinra, :esrgan, :ignore, :upPath, :initPath)""",
                {
                    'filename': file,
                    'gname': file,
                    'width': width,
                    'height': height,
                    'category': "New",
                    'text': 0,
                    'shinra': 0,
                    'esrgan': 0,
                    'ignore': 0,
                    'upPath': "./gigapixel/",
                    'initPath': "./gigapixel/"
                })
        conn.commit()
        print(file+" added to database")
    except: pass
    

def defineCategory(attributes):
    tx_attributes=attributes
    if tx_attributes[9] == "./textures/priority/" or tx_attributes[4]=="Priority":
        category="Priority"
    elif tx_attributes[4] == "Skybox/BG":
        category="SkyboxBG"
    elif tx_attributes[4] == "Sign/Decal":
        category="SignDecal"
    elif tx_attributes[4]=="Zack - 1st Class":
        category="Zack1stClass"
    elif tx_attributes[4]=="Zack - 2nd Class":
        category="Zack2ndClass"
    elif tx_attributes[4]=="Zack - Buster Sword":
        category="ZackBusterSword"
    elif tx_attributes[4]=="Object/Prop" or tx_attributes[4]=="Metallic":
        category="ObjectProp"
    elif tx_attributes[4]=="Fog, etc." or tx_attributes[4]=="UI" or tx_attributes[8]==1 or tx_attributes[4]=="Ignore":
        category="Ignore"
    else:
        category=tx_attributes[4]
    return category



def addCatRecord(attributes, category):
    
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    sql="INSERT INTO " + category + " (filename, gname, category) VALUES (:filename, :gname, :category)"
    #print(attributes[0])
    #print(attributes[1])
    #print(category)
    #print(sql)
    try:
        c.execute(sql, {'filename': attributes[0], 'gname': attributes[1], 'category': category}) 
        conn.commit()
    except:
        print("Entry already exists in category")
        
    conn.close() 

def deleteCatRecord(attributes, category):
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    sql="DELETE From " + category + " where filename = ?"
    try:
        c.execute(sql, (attributes[0], ))
        conn.commit()
    except sqlite3.Error as error:
        print(error)
    conn.close()


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
    #print(os.getcwd())
    conn.close()

def updateRecord(attr, file):
    
    filename=file[13:]
    attributes=attr
    #addCatRecord(attributes)
    #print(attributes)
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    c.execute("""UPDATE textures SET gname = ?, category = ?, text_element = ?, shinra_logo = ?, use_esrgan = ?,
                ignore = ? WHERE filename = ?""", attributes)
    conn.commit()
    conn.close()
    


def save(position, category):
    #print(os.getcwd())
    filename=position

    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    sql="UPDATE saved_"+category+" SET filename = ? WHERE oid = 1"
    try:
        c.execute(sql, (filename, ))
        #print("position saved @ "+filename)
    except:
        print("couldn't save")
    conn.commit()
    conn.close()
def save_init(position):
    #print(os.getcwd())
    filename=position

    conn = sqlite3.connect('textures.db')
    c = conn.cursor()
    try:
        c.execute("""INSERT INTO saved SET filename = ? WHERE oid = 1""", (filename, ))
        #print("position saved @ "+filename)
    except:
        print("couldn't save")
    conn.commit()
    conn.close()


def get_save(category):
    #print(os.getcwd())
    #print("GETTING SAVE NOW")

    conn = sqlite3.connect('textures.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    sql = "SELECT * FROM saved_"+category+" WHERE oid=1"
    c.execute(sql)
    #print("PRINTING FETCHED POSITION \n")
    result = c.fetchone()
    print("get_save result: "+result['filename'])
    conn.close()
    for item in result:
        #print("2 "+result['filename'])
        return result['filename']
def getImageList(category):
    tx_list =  []
    sql = "SELECT * FROM " + category
    conn=sqlite3.connect('textures.db')
    conn.row_factory = sqlite3.Row
    c=conn.cursor()
    c.execute(sql)
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

def addDefaultPath(file):
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
    
    #
    conn.commit()
    conn.close()
    

def updateInitPath():
    conn=sqlite3.connect('textures.db')
    c=conn.cursor()
    c.execute("""UPDATE textures SET initPath = upPath""", )
    conn.commit()
    conn.close()

def organize(file):
    tx_attributes = file
    if tx_attributes[9]==tx_attributes[10]:
        print(tx_attributes[9]+" is the same as "+ tx_attributes[10]+", no action taken")
    else:
        if tx_attributes[4] != "New" or tx_attributes[4] != "UI":
            try:
                shutil.move("./gigapixel/"+tx_attributes[0], tx_attributes[9]+tx_attributes[0])
                #print("Copied upscale from gigapixel folder")
            except:
                print("trying to copy from current folder")
                
                try:
                    shutil.move(tx_attributes[10]+tx_attributes[0], tx_attributes[9]+tx_attributes[0])
                    
                except sqlite3.Error as error:
                    print("#################################################")
                    print("could not move upscaled copy from current folder")
                    print("#################################################")
                    print(error)
            try:
                shutil.move("./masterdumps/"+tx_attributes[0], "./masterdumps/"+tx_attributes[9][11:]+tx_attributes[0])
                #print("Copied master from masterdumps folder")
            except:
                try:
                    shutil.move("./masterdumps/"+tx_attributes[10]+tx_attributes[0], "./masterdumps/"+tx_attributes[9][11:]+tx_attributes[0])
                    #print("Copied master from current folder")
                except:
                    print("#################################################")
                    print("could not move upscaled copy from current folder")
                    print("#################################################")

    #else:
        #print("!!!! WARNING IMAGE NOT CATEGORIZED !!!")

def generate_textures_ini(file):
    texturesini = open("add_textures.ini", "a")
    
    tx_attributes = get(file)
    filehash = tx_attributes[0]
    path=tx_attributes[9]
    if tx_attributes[4] !="UI" or not tx_attributes[8]:
        texturesini.write(filehash[0:24] + " = "+path[1:]+tx_attributes[0]+"\n")