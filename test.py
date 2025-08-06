import cv2
import easyocr
from PIL import Image
from csv import DictWriter
import os
def perform_ocr(): 
    field_names = ['FileName', 'DetectedText', 'FineAmount']
    im_dir = './images/' 
    reader = easyocr.Reader(['en'])
    f = open('record.csv', 'a')
    fobj = DictWriter(f, fieldnames=field_names)
    fnames = os.listdir(im_dir)
    print(fnames)
    for name in fnames:
        print(name)
        im = cv2.imread(im_dir+name)
        result = reader.readtext(im, paragraph="False")
        result = result[0][-1].replace(" ", '').upper()
        fobj.writerow({'FileName':name, 'DetectedText':result, 'FineAmount':1000})
        
    f.close()
            
            
            
perform_ocr()