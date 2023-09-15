import os
import shutil
source='C:/Users/Brandon Holman/Desktop'
files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    print('the name of the file is ', name)
    print('the name of the extension file is', ext)