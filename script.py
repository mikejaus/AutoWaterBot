import RPi.GPIO as GPIO
import time
import signal

sensor = 3
pump = 7
continue_reading = True

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(pump, GPIO.OUT)

def end_read(signal,frame):
        global continue_reading
        print "Control+C Captured, Stopping Process"
        continue_process = False
        GPIO.cleanup(sensor)
        GPIO.cleanup(pump)

signal.signal(signal.SIGINT, end_read)

while continue_reading:
        if GPIO.input(sensor)==0:
                print "Plant Dry - Activating Pump"
                GPIO.output(pump, GPIO.LOW)
                time.sleep(1)
        else:
                print "Plant does not need to be watered"
                GPIO.output(pump, GPIO.HIGH)
                time.sleep(1)
