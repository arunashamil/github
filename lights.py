from gpio import GPIO
import time
def lightUp(number, period):
    GPIO.output(number, 1)
    time.sleep(period)
    GPIO.output(number, 0)

lightUp(1,1) #ooooo 

print ("------------------------------------------------------")

def blink(number, blinkCount, blinkPeriod):
    i = 0
    while i < blinkCount:
        lightUp(number, blinkPeriod)
        time.sleep(blinkPeriod)
        i = i + 1

blink(2, 3, 1)

print("-------------------------------------------------------")   

def runningLight(count, period):
    i = 0
    j = 0
    while j < count:
        for i in range(8):
            lightUp(i, period)
            time.sleep(period)
        j = j + 1

runningLight(4, 0.5)

print("-------------------------------------------------------")
i = 0
while i < 8:
    GPIO.output(i, 1)
    i = i + 1

def runningDark(count, period):
    i = 0
    j = 0
    while j < count:
        for i in range(8):
            GPIO.output(i, 0)
            time.sleep(period)
            GPIO.output(i, 1)
            time.sleep(period)
        j = j + 1

runningDark(3, 0.5)  
