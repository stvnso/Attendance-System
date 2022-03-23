from gpiozero import MotionSensor, LED
import lcd_drivers
from signal import pause
from time import sleep
from Alarm_System_Functions import *

def main_function():

    arming_alarm_system()

# --------------------------------
    display = lcd_drivers.Lcd()

    pir_room1 = MotionSensor(18)
    led_room1 = LED(12)

    pir_room2 = MotionSensor(23)
    led_room2 = LED(21)

    # -------------------------------

    def motion_room1():
        print("Motion detected")
        display.lcd_clear()
        display.lcd_display_string("Motion detected!", 1)
        display.lcd_display_string("Room 1", 2)
        led_room1.on()
        sleep(5)
        led_room1.off()
        display.lcd_clear()

    def motion_room2():
        print("Motion detected")
        display.lcd_clear()
        display.lcd_display_string("Motion detected!", 1)
        display.lcd_display_string("Room 2", 2)
        led_room2.on()
        sleep(5)
        led_room2.off()
        display.lcd_clear()


    pir_room1.when_motion = motion_room1
    pir_room2.when_motion = motion_room2
    

    pause()


 
        


