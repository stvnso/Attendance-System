from gpiozero import MotionSensor, LED
import lcd_drivers
from signal import pause
from time import sleep


# --------------------------------
display = lcd_drivers.Lcd()
sirene = LED(12)

pir_room1 = MotionSensor(21)
led_room1 = LED(26)

pir_room2 = MotionSensor(20)
led_room2 = LED(23)

   # -------------------------------

def motion_room1():
    print("Motion detected")
    print("Room 1")
    display.lcd_clear()
    display.lcd_display_string("Motion detected!", 1)
    display.lcd_display_string("Room 1", 2)
    led_room1.on()
    sirene.on()
    sleep(3)
    led_room1.off()
    sirene.off()
    display.lcd_clear()

def motion_room2():
    print("Motion detected")
    print("Room 2")
    display.lcd_clear()
    display.lcd_display_string("Motion detected!", 1)
    display.lcd_display_string("Room 2", 2)
    led_room2.on()
    sirene.on()
    sleep(3)
    led_room2.off()
    sirene.off()
    display.lcd_clear()

pir_room1.when_motion = motion_room1
pir_room1.wait_for_no_motion
pir_room2.when_motion = motion_room2
pause()

