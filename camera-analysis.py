from objectdetection import *
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

fileName = 'image.jpg'
pathToWeights =  c_char_p(bytes("/home/pi/python/packages/darknet/tiny-yolo-voc.weights", 'utf-8'))
pathToConfig =  c_char_p(bytes('/home/pi/python/packages/darknet/cfg/tiny-yolo-voc.cfg', 'utf-8'))
pathToData = c_char_p(bytes('/home/pi/python/packages/darknet/cfg/voc.data', 'utf-8'))
neuralNet = load_net(pathToConfig, pathToWeights, 0)
metaData = load_meta(pathToData)
    

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)
try:
  #  for frame in range(10):
        camera.capture(fileName, resize=(400,300))
        results = detect(neuralNet, metaData, c_char_p(bytes(fileName, 'utf-8')))
        for result in results:
            if b'person' in result:
                print("THERE'S A PERSON!")
finally:
    camera.close()
    


