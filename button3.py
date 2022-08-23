import gpiozero
import time

led = gpiozero.LED(4)
button = gpiozero.Button(17)
 

while True:
    if button.is_pressed:
        led.on()
    else:
        led.off()
