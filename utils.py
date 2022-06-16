import tweepy
import requests
import eventlet
eventlet.monkey_patch()
import cv2
import os
import time

def extrair_images(filename):
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("images/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1

def deleta_images():
    dir = 'images'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


def tweet_image(message, url='http://81.8.143.33/mjpg/video.mjpg'):
   
    filename = 'temp.mp4'
    request = ''
    with eventlet.Timeout(10):
        request = requests.get(url, stream=True, timeout=3)

    count = 2000
    with open(filename, 'wb') as image:
        for chunk in request:
            # print(count)
            image.write(chunk)
            count -= 1
            if(count < 0):
                extrair_images(filename)
                print("-------- Enviando")
                time.sleep(5)
                # postar(message)
                # time.sleep(10)
                # deleta_images()
                request = []
                exit(0)


try:
    tweet_image("oi")

except Exception as e:
    print("Erro ", e)
