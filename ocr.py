'''Scans through every file in /dev/text_seg to read Latin text.
Each page is segmented by part, saved to text_seg then deleted for the 
next page.
'''
try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract
from os import listdir
from os.path import isfile, join

#set directory
dir = './dev/text_seg/'
#get all the files in segmented text 
photos = [f for f in listdir(dir) if isfile(join(dir,f))]
print(photos)
text = []
def ocr_read(filename):
	for photo in range(len(photos)):
		text.append(pytesseract.image_to_string(Image.open(dir+photos[photo])))
	return text
print(ocr_read(dir))
