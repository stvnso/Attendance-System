# Bibliotheken laden
from gpiozero import Button, LED
import lcd_drivers
from signal import pause
from time import sleep

display = lcd_drivers.Lcd()


#button = Button(27)


led = LED(12)


btn = Button(27)

led.on()
display.lcd_display_string("Wait for press",1)

btn.wait_for_press()

display.lcd_clear()


if btn.is_pressed:
    print("button is pressed")
    led.off()

sleep(2)
led.on()
sleep(2)
led.off()
