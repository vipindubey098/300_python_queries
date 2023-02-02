import os.path
import time

tim = os.path.getctime('image.png')
ctime = time.ctime(tim)
print(ctime)