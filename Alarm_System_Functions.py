from gpiozero import MotionSensor, LED
import lcd_drivers
from signal import pause
from time import sleep

def arming_alarm_system():

    display = lcd_drivers.Lcd()
    display.lcd_clear()

    sleep(1)
    display.lcd_display_string("Starting", 1)
    display.lcd_display_string("Alarm System..", 2)
    sleep(2)

    display.lcd_clear()
    display.lcd_display_string("System armed in", 1)
    display.lcd_display_string("3", 2)
    print("System armed in 3")
    sleep(1)

    display.lcd_clear()
    display.lcd_display_string("System armed in", 1)
    display.lcd_display_string("2", 2)
    print("System armed in 2")
    sleep(1)

    display.lcd_clear()
    display.lcd_display_string("System armed in", 1)
    display.lcd_display_string("1", 2)
    print("System armed in 1")
    sleep(1)

    display.lcd_clear()
    display.lcd_display_string("System", 1)
    display.lcd_display_string("ARMED!!", 2)
    sleep(1)


