import easyocr
import os
import cv2 

def perform_ocr(): 
    im_dir = './images/' 
    reader = easyocr.Reader(['en'])
    fnames = os.listdir(im_dir)
    result_set = []
    for name in fnames:
        print(name)
        im = cv2.imread(im_dir+name)
        result = reader.readtext(im, paragraph="False")
        try:
            result = result[0][-1].replace(" ", '').upper()
            result_set.append([name, result])
            
        except:
            continue
        
    return result_set