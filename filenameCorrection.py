import os
from xml.etree import ElementTree as et

sourcepath = os.listdir('C:/Users/suzan/Downloads/VOC2028/partbannot/')


for file in sourcepath:
    inputfile = 'C:/Users/suzan/Downloads/VOC2028/partbannot/'+file
    
    tree = et.parse(inputfile)
    print('Conversion is ongoing for:'+ inputfile)

    filename, extension = os.path.splitext(file)

    tree.find('.//filename').text = filename + '.jpg'
    tree.write(inputfile)
    
    print('Replaced!')