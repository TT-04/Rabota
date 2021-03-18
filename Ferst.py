import RPi.GPIO as GPIO
import time 

ledPin=[24,25,8,7,12,16,20,21,10,9,11,5,6,13,19,26]
NLed = 12

def lightUp(led_number, period):
    GPIO.output(ledPin[led_number], 1)
    time.sleep(period)
    GPIO.output(ledPin[led_number], 0)



def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(0, blinkCount):
        GPIO.output(ledPin[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledPin[ledNumber], 0)
        time.sleep(blinkPeriod)

def configur():
    for i in range(0,NLed):
        GPIO.setup(ledPin[i],GPIO.OUT)

def clean():
    for i in range(0,NLed):
        GPIO.cleanup(i)


def runningLight(count, period):
    for j in range(0,count):
        for i in range(0,NLed):
            lightUp(i, period)

def lightDown(led_number, period):
    GPIO.output(ledPin[led_number], 0)
    time.sleep(period)
    GPIO.output(ledPin[led_number], 1)


def runningDark(count,period):
    for k in range(0, NLed):
        GPIO.output(ledPin[k], 1)
    for k in range(0,count):
        for i in range(0, NLed):
            lightDown(i, period)
    for k in range(0, NLed):
        GPIO.output(ledPin[k], 0)




def decToBinList(decNumber):
    bin = []
    p = 0
    for i in range(0,NLed):
        p = (decNumber%2)
        if p == 1:
            bin.append(1)
        else:
            bin.append(0)
        decNumber = (decNumber//2)
    
    return bin


def lightNumbern(number):
    binL = [] 
    binL= decToBinList(number)
    for i in range(0, NLed):
        GPIO.output(ledPin[i], binL[i])
        

def runningPattern(pattern, directtion, period, Nof):
    pattern = int (pattern)
    for i in range(Nof):
        lightNumbern(pattern)
        time.sleep(period)
        if directtion == 1: # ->
            p = pattern
            pattern = int(period)>>1
            p = p%2
            pattern = pattern + (int(p)<<NLed)
        else:
            p = int(pattern)%(1<<NLed)
            pattern = pattern<<1
            pattern +=p

        
                


GPIO.setmode(GPIO.BCM)

configur()


runningPattern(7, 1, 0.5, 100)

time.sleep(2)

lightNumbern(23)

time.sleep(1)

print(decToBinList(5))

runningDark(3, 0.1)



time.sleep(1)
runningLight(4, 0.1)
time.sleep(1)
lightUp(6, 1)
time.sleep(1)
blink(7, 4, 0.2)


clean()


