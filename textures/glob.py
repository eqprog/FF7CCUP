import glob

imageList = []

for png in glob.glob("*.png"):
       imageList.append(png)

print(imageList)
