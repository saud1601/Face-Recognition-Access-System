import BlynkLib
import RPi.GPIO as GPIO

blynk = BlynkLib.Blynk('c2e97d056d744994b1b8073963dec4be' )
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
#sn = Blynk('00fc7672fafd447aad3ffe46d3bf89ea', pin= "V1") 
blynk.notify('Door Online')

@blynk.VIRTUAL_WRITE(1)

def Door(value):
      
    if int(format(value[0])) == 1:
        GPIO.output(20, 1)
        blynk.notify('Door Unlocked')

        
    else:             
        GPIO.output(20, 0)
        blynk.notify('Door Locked')


while True:    
    blynk.run()
