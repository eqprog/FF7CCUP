import sqlite3
import os 
categories = ["Priority", "Sign/Decal", "Artwork", "Ground", "Wall", "Metallic", "Object/Prop", "Skybox/BG", "NPC", "Enemy", "Foliage", "Zack - 1st Class", "Zack - 2nd Class", "Zack - Buster Sword", "Aerith", "Cissnei", "Tseng", "Angeal", "Genesis", "Hollander", "Lazard", "Sephiroth", "Cloud", "Tifa", "Yuffie"]

#tables = open("sql_script.txt", "a")
conn=sqlite3.connect('textures.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Priority (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS SignDecal (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Artwork (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Ground (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Wall (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Metallic (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS ObjectProp (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS SkyboxBG (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS NPC (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Enemy (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Foliage (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Zack1stClass (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Zack2ndClass (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS ZackBusterSword (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Aerith (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Cissnei (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Tseng (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Angeal (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Genesis (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Hollander (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Lazard (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Sephiroth (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Cloud (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Tifa (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
c.execute("""CREATE TABLE IF NOT EXISTS Yuffie (filename text PRIMARY KEY, gname text, width integer, height integer, category text, text_element integer, shinra_logo integer, use_esrgan integer, ignore integer)""")
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