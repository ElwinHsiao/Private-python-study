#!/usr/bin/env python
#import Image
from PIL import Image
import os
import os.path
import sys
path = sys.argv[1]
small_path = (path[:-1] if path[-1]=='/' else path) +'_small'
print small_path
if not os.path.exists(small_path):
    os.mkdir(small_path)
for root, dirs, files in os.walk(path):
    for f in files:
        fp = os.path.join(root, f)
        img = Image.open(fp)
        w, h = img.size
        img.resize((w/4, h/4)).save(os.path.join(small_path, f), "JPEG")
        print fp
