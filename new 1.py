

import RPi.GPIO as GPIO
from time import sleep

LED_PIN = 18
fadePercent = 5
brightness = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 1000)  # فرێکوانسی 1000Hz
pwm.start(0)

try:
    while True:
        pwm.ChangeDutyCycle(brightness)
        brightness += fadePercent  # زیادکردنی باشتر
        
        # ر ئاراستەکە کاتێک ڕەنگەکە دەگاتە سنوورەکان
        if brightness <= 0 or brightness >= 100:
            fadePercent = -fadePercent
            # ڕێگری لەدەرچوون لە [0, 100] دەکات
            brightness = max(0, min(brightness, 100))
        
        sleep(0.03)  # 30ms
        
except KeyboardInterrupt:
    print("\nبەکارهێنەر کۆتایی پێهێنا")
    
finally:
    pwm.stop()
    GPIO.cleanup()
    print("پاککردنەوەی GPIO")
