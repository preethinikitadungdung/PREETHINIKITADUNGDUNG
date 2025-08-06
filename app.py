from document import make_doc
from detect import detect_plates
from ocr import perform_ocr 
import streamlit as st 
import os
import glob

def app():
    st.title('Real Time Helmet Detection')
    
    choice = st.selectbox('select input mode', options=['Camera', 'Video'])
    if choice=='Camera':
        if st.button('Start Camera'):
            if detect_plates(0):
                result_set = perform_ocr()
                if result_set: make_doc(result_set)
                st.warning('Completed')
            
    else:
        up_vdo = st.file_uploader('Upload a video', type=['mp4'])
        if up_vdo is not None:
            with open('./videos/input.mp4', 'wb') as f:
                f.write(up_vdo.getvalue())
                
        if st.button('Detect'):
            if detect_plates('./videos/input.mp4'):
                result_set = perform_ocr()
                make_doc(result_set)
                st.warning('Completed')
    

if __name__=='__main__':
    
    images = glob.glob('./images/*')
    challans = glob.glob('./challan/*')
    persons = glob.glob('./person/*')
    for k in images: os.remove(k)
    for i in challans: os.remove(i)
    for j in persons: os.remove(j)
    
    app()