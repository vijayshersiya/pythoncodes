# -*- coding: utf-8 -*-
"""
Created on Sat May 11 03:29:35 2019

@author: Vijay
"""
"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail â€“ Generate the thumbnail of the given image (size = 75, 75
                                                                        """
                                                                        
from PIL import Image                                                                        
img = Image.open("a.jpg")
gray= GreyScale(img)
print (img. gray )
img.show()
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show() 
 
img = Image.open("data/a.jpg")
img.thumbnail((75, 75))
print(img.width, img.height)
img.save('thumb_a.jpg')
img.show()

img = Image.open("a.jpg")                 
crop_im = img.crop(box=(340, 20, 160, 204))
crop_im.save('crop_a.jpg')
img.show()