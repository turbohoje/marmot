#!/usr/bin/env python3

#pip2 install pdf2image
#brew install poppler

import os
import glob
import tempfile
from pdf2image import convert_from_path
from PIL import Image
import re

def convert_pdf(file_path, output_path):
    # save temp image files in temp dir, delete them after we are finished
    with tempfile.TemporaryDirectory() as temp_dir:
        # convert pdf to multiple image
        images = convert_from_path(file_path, output_folder=temp_dir, dpi=60) #low quality for size
        # save images to temporary directory
        temp_images = []
        for i in range(len(images)):
            image_path = f'{temp_dir}/{i}.jpg'
            images[i].save(image_path, 'JPEG')
            temp_images.append(image_path)
        # read images into pillow.Image
        imgs = list(map(Image.open, temp_images))
    # find minimum width of images
    min_img_width = min(i.width for i in imgs)
    # find total height of all images
    total_height = 0
    for i, img in enumerate(imgs):
        total_height += imgs[i].height
    # create new image object with width and total height
    merged_image = Image.new(imgs[0].mode, (min_img_width, total_height))
    # paste images together one by one
    y = 0
    for img in imgs:
        merged_image.paste(img, (0, y))
        y += img.height
    # save merged image
    merged_image.save(output_path)
    return output_path


# pdfs_to_convert = glob.glob('./files/*.pdf')
# for f in pdfs_to_convert:
#     p = re.compile('./files/')
#     dest = p.sub('./images/files/',f)+".png"
#     print("Converting "+f)
#     convert_pdf(f, dest)

pdfs_to_convert = glob.glob('./files/permit/*.pdf')
for f in pdfs_to_convert:
    p = re.compile('./files/')
    dest = p.sub('./images/files/',f)+".png"
    print("Converting "+f+" "+dest)
    convert_pdf(f, dest)

pdfs_to_convert = glob.glob('./files/permit/owts/*.pdf')
for f in pdfs_to_convert:
    p = re.compile('./files/permit/')
    dest = p.sub('./images/files/permit/owts/',f)+".png"
    print("Converting "+f+" "+dest)
    convert_pdf(f, dest)
