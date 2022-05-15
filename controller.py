import RPi.GPIO as GPIO
import socket
import csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)

GPIO.output(29,True)
GPIO.output(31,True)

UDP_IP = "192.168.43.228"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024)
  raw=data
  


  if raw== b'forward':
    print("Robot Move Forward")
    GPIO.output(35,True)
    GPIO.output(11,False)
    GPIO.output(16,True)
    GPIO.output(15,False)
  
  
  
  elif raw==b'stop':
      GPIO.output(35,False)
      GPIO.output(11,False)
      GPIO.output(16,False)
      GPIO.output(15,False)
      print ("Robot Stop")
    

  elif raw==b'backward':
      GPIO.output(35,False)
      GPIO.output(11,True)
      GPIO.output(16,False)
      GPIO.output(15,True)
      print ("Robot Move Backward")

  elif raw==b'right':
      GPIO.output(35,False)
      GPIO.output(11,True)
      GPIO.output(16,True)
      GPIO.output(15,False)	
      print ("Robot Move Left")

  elif raw==b'left':
      GPIO.output(35,True)
      GPIO.output(11,False)
      GPIO.output(16,False)
      GPIO.output(15,True)	
      print ("Robot Move Right")

  else:
      print ("STOP")
      GPIO.output(35,False)
      GPIO.output(11,False)
      GPIO.output(16,False)
      GPIO.output(15,False)
