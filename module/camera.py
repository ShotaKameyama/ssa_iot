'''
This is a module to support camera functions.
Use the connected USB camera and provide the following functions:
1. Take a picture and save an img file.
'''
import datetime
# Import opencv for computer vision
import cv2
from pyzbar.pyzbar import decode
from pyzbar.pyzbar import ZBarSymbol
from pyaml_env import parse_config, BaseConfig

config = BaseConfig(parse_config('./config/config.yml'))
dt_now = datetime.datetime.now()
dt_now_format = dt_now.strftime('%Y-%m-%d-%H%M%S')


def take_photo():
    '''
    This will take a picture using a USB camera
    and save an img file.
    '''
    # Connect to capture device
    cap = cv2.VideoCapture(
        config.client_camera.vid_cap
    )
    # Get a frame from the capture device
    ret, frame = cap.read()
    print(ret)
    # Save into a picture
    cv2.imwrite('static/capture/' + dt_now_format + '_capture.jpg', frame)
    # Release the connection
    cap.release()

def capture_qr_code():
    cap = cv2.VideoCapture(
        config.client_camera.vid_cap)
    if cap.isOpened() is False:
        raise("IO Error")

    while True:
        ret, frame = cap.read()
        if ret == False:
            continue
        
        #decode
        value = decode(frame, symbols=[ZBarSymbol.QRCODE])

        if value:
            for qrcode in value:
                dec_info = qrcode.data.decode('utf-8')
                break
            break
    
    return dec_info
