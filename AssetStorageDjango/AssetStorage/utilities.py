import math
import os
from PIL import Image, ImageOps


def convert_size(size_bytes):
   if (size_bytes == 0):
       return '0B'
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes/p, 2)
   return '%s %s' % (s, size_name[i])

def make_thumbnail(image_file, height, width):
   print(image_file)
   save_path = append_name(image_file.path, '_sm')
   thumb_path = append_name(image_file.name, '_sm')
   size = (height,width)
   print('save path')
   print(save_path)
   print('thumb path')
   print(thumb_path)
   try:
        big = Image.open(image_file)
        print('opened image')
        thumbnail = ImageOps.fit(big, size, Image.ANTIALIAS)
        print('made thumbnail')
        thumbnail.save(save_path,big.format)
        print('saved thumbnail')
        big.close()
        thumbnail.close()
        return thumb_path
   except IOError:
       print("cannot create thumbnail for ", image_file)



def append_name(path, name):
   directory, filename = os.path.split(path)
   file, ext = os.path.splitext(filename)
   filename = file + name + ext
   newpath = os.path.join(directory, filename)
   return newpath

def rename(path, name):
   directory, filename = os.path.split(path)
   ext = os.path.splitext(filename)[1]
   filename = name + ext
   newpath = os.path.join(directory, filename)
   return newpath

