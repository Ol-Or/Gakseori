import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
StepPins=[11,13,15,16]

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    
StepCounter = 0

StepCount=4

Seq=[[0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]]

try:
    while 1:
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

except KeyboardInterrupt:
    GPIO.cleanup()
