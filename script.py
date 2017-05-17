import os
from PIL import Image

images = os.listdir(os.getcwd())
formats_list = ['jpg', 'png']
base_parameter = int(input('Enter the base parameter: '))
for i in images:
    if i[-3:] in formats_list:
        img = Image.open(i)
        current_width = img.size[0]
        current_height = img.size[1]
        if current_width >= current_height:        
            wpercent = (base_parameter / float(current_width))
            hsize = int((float(current_height) * float(wpercent)))
            new_img = img.resize((base_parameter, hsize), Image.ANTIALIAS)
            new_img.save(i, quality=100)
            img.close()
        elif current_width < current_height:
            hpercent = (base_parameter / float(current_height))
            wsize = int((float(current_width) * float(hpercent)))
            new_img = img.resize((wsize, base_parameter), Image.ANTIALIAS)
            new_img.save(i, quality=100)
            img.close() 
    else:
        continue