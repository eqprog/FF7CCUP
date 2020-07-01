import sqlite3
import os 
categories = ["Priority", "Sign/Decal", "Artwork", "Ground", "Wall", "Metallic", "Object/Prop", "Skybox/BG", "NPC", "Enemy", "Foliage", "Zack - 1st Class", "Zack - 2nd Class", "Zack - Buster Sword", "Aerith", "Cissnei", "Tseng", "Angeal", "Genesis", "Hollander", "Lazard", "Sephiroth", "Cloud", "Tifa", "Yuffie"]

#tables = open("sql_script.txt", "a")
conn=sqlite3.connect('textures.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS saved_Priority (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_SignDecal (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Artwork (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Ground (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Wall (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Metallic (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_ObjectProp (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_SkyboxBG (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_NPC (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Enemy (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Foliage (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Zack1stClass (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Zack2ndClass (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_ZackBusterSword (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Aerith (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Cissnei (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Tseng (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Angeal (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Genesis (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Hollander (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Lazard (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Sephiroth (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Cloud (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Tifa (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Yuffie (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_New (filename text PRIMARY KEY, gname text, category text)""")
c.execute("""CREATE TABLE IF NOT EXISTS saved_Ignore (filename text PRIMARY KEY, gname text, category text)""")
conn.commit()
conn.close()

"""for category in categories:
	createsql = "\"\"\"CREATE TABLE IF NOT EXISTS "+category+" (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)\"\"\""
	conn.commit()"""


#c.execute("""CREATE TABLE IF NOT EXISTS test (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
#conn.commit()
#category = "test"
#file = "file"
#width = 128
#height = 128
#cat = "New"
#sql="""INSERT INTO """+category+""" VALUES (:filename, :gname, :width, :height, :category, :text, :shinra, :esrgan, :ignore)"""

#print(sql)
#c.execute(sql, {'filename': "foo",'gname': "foo",'width': 128,'height': 128,'category': "foo",'text': 0,'shinra': 0,'esrgan': 0,'ignore': 0})
#conn.commit()
#conn.close()