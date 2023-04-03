from zipfile import ZipFile

z=ZipFile("sample.zip",'w')

z.write("A2.py")
z.write("A3.py")
z.write("A1.txt")
z.write("A2.txt")


z.close()