from gpiozero import MotionSensor, LED, Button
import lcd_drivers
from signal import pause
from time import sleep
from Alarm_System_Functions import *

# Display
display = lcd_drivers.Lcd()

# Siren
siren = LED(12)

# ROOM1
room1_GasSensor = MotionSensor(1)
room1_WindowSwitch = Button(23)
room1_LED = LED(13)

# ROOM2
room2_MotionSensor = MotionSensor(20)
room2_LED = LED(19)

# ROOM3
room3_MotionSensor = MotionSensor(21)
room3_LED = LED(22)

##############################################


def room1_Window():
    display.lcd_clear()
    display.lcd_display_string("Fenster offen", 1)
    display.lcd_display_string("Raum 1", 2)
    print("Room 1 - Window open! \n")

    room1_LED.on()
    siren.on()
    sleep(3)

    room1_LED.off()
    siren.off()

    sleep(1)
    display.lcd_clear()
    

def room1_Gas():
    display.lcd_clear()
    display.lcd_display_string("Gas !!", 1)
    display.lcd_display_string("Raum 1", 2)
    print("Room 1 - Gas detected!\n")

    room1_LED.on()
    siren.on()
    sleep(3)

    room1_LED.off()
    siren.off()

    sleep(1)
    display.lcd_clear()


def room2_Motion():
    display.lcd_clear()
    display.lcd_display_string("Bewegung!", 1)
    display.lcd_display_string("Raum 2", 2)
    print("Room 2 - Motion detected! \n")

    room2_LED.on()
    siren.on()
    sleep(3)

    room2_LED.off()
    siren.off()

    sleep(1)
    display.lcd_clear()


def room3_Motion():
    display.lcd_clear()
    display.lcd_display_string("Bewegung!", 1)
    display.lcd_display_string("Raum 3", 2)
    print("Room 3 - Motion detected! \n")

    room3_LED.on()
    siren.on()
    sleep(3)

    room3_LED.off()
    siren.off()

    sleep(1)
    display.lcd_clear()


def Alarm_Main():

    arming_alarm_system()

    # ROOM1
    room1_WindowSwitch.when_released = room1_Window
    room1_GasSensor.when_motion = room1_Gas

    # ROOM2
    room2_MotionSensor.when_motion = room2_Motion

    # ROOM3
    room3_MotionSensor.when_motion = room3_Motion

    pause()

# Alarm_Main()