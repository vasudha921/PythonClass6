from os import access
import cv2
import dropbox
import time
import random
start_time = time.time()
def take_snapshot():
    num = random. randint(0, 1000)
    videocaptureobj= cv2.VideoCapture(0)
    result = True
  
    while (result) :
       ret, frame = videocaptureobj.read()
       image_name = "img" + str(num) + ".png"
       cv2.imwrite(image_name, frame)
       result = False 
    
    videocaptureobj.release()
    cv2.destroyAllWindows()
    return image_name




def upload_file( file_from):
        access_token = 'lynkvfwsvRYAAAAAAAAAASbsEkYSknG7VGqeePI5YMc8fPt4_2fQY_hWOD8jnJLJ'
        file_to = "/test/" + (file_from)

        dbx = dropbox.Dropbox(access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded successfully')

def main():
    while (True) :
        if((time.time()- start_time) >= 5  ):
            name = take_snapshot()
            upload_file(name)
main()
    

    
    
