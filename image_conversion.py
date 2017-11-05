import pytesseract
import os
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = '.....\\tesseract.exe' # path of tesseract

path = 'C:.....' # path of image folder

# function to convert image to text and return type: string
def ocr(file_to_ocr):
    im = Image.open(path+"\\"+file_to_ocr)
    txt=pytesseract.image_to_string(im)
    return txt

file_list = os.listdir(path) # file names in list (not sorted)
directory = os.path.join(path) # path for storing the text file

# function to sort the file names
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

file_list.sort(key=natural_keys) # file names in list (sorted)

# for every files in the folder
for file in file_list:
	# selecting image file type
    if file.endswith(".jpg"): 
        txt=ocr(file) # calling the ocr function
	# appending the text into the file
        with open(directory+"\\"+'data'+".txt",'a+') as f:
            f.write("\n")
            f.write(file)
            f.write("\n")
            f.write('-----------------------------------------')
            f.write("\n")
            f.write('!!!Start!!!')
            f.write("\n")
            f.write(str(txt))
            f.write("\n")
            f.write('!!!End!!!')
            f.write("\n")
            f.write('-----------------------------------------')
            f.write("\n")
print("Image Conversion completed")
