import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
StepPins=[11,13,15,16]  #step motor GPIO

#PCF module address
address = 0x48
AIN2 = 0x42

bus=smbus.SMBus(1)

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

StepCounter = 0

StepCount=4

try:
    while True:
        bus.write_byte(address,AIN2)
        value = bus.read_byte(address)
        if value > 256: # 수위 측정한 값 쓰기!
            Seq=[[0,0,0,1],    #시계방향으로 움직임(차수판 닫힘)
                 [0,0,1,0],
                 [0,1,0,0],
                 [1,0,0,0]]
            for pin in range(0,4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin] !=0:
                    GPIO.output(xpin, True)
                else:
                     GPIO.output(xpin,False)

            StepCounter += 1

            if (StepCounter ==StepCount):
                StepCounter =0
            if (StepCounter<0):
                StepCounter = StepCount
            time.sleep(0.01)
        else :
            Seq=[[1,0,0,0],   #반시계방향으로 움직임 (차수판 올라감)
                 [0,1,0,0],
                 [0,0,1,0],
                 [0,0,0,1]]
            for pin in range(0,4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin] !=0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin,False)

            StepCounter += 1

            if (StepCounter ==StepCount):
                StepCounter =0
            if (StepCounter<0):
                StepCounter = StepCount
 
        time.sleep(0.01)
      
GPIO.cleanup()