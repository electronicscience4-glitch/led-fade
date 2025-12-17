

import RPi.GPIO as GPIO
from time import sleep
LED_PIN = 18
fadePercent = 5
brightness = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)
try:
    while True:
        pwm.ChangeDutyCycle(brightness)
        brightness = brightness + fadePercent;

        if brightness <= 0 or brightness >= 100:
            fadePercent = -fadePercent;
  
        sleep(0.03);
finally:
    GPIO.cleanup()
