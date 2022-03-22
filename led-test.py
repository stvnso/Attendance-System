# Bibliotheken laden
from gpiozero import Button, LED
import lcd_drivers
from signal import pause
from time import sleep

display = lcd_drivers.Lcd()

led = LED(12)


led.on()
sleep(3)
led.off()

