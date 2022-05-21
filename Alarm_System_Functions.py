from gpiozero import LED
import lcd_drivers
from signal import pause
from time import sleep

# # Display
# display = lcd_drivers.Lcd()

# # Siren
# sirene = LED(12)

# # ROOM1
# room1_LED = LED(13)

# # ROOM2
# room2_LED = LED(19)

# # ROOM3
# room3_LED = LED(22)


##################################
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
    print("System ARMED!")
    sleep(1)
    display.lcd_clear()


def room1_Gas():
    display.lcd_clear()
    display.lcd_display_string("Gas erkannt!", 1)
    display.lcd_display_string("Raum 1", 2)

    room1_LED.on()
    sleep(5)
    room1_LED.off()

    display.lcd_clear()


def room1_Window():
    display.lcd_clear()
    display.lcd_display_string("Fenster offen", 1)
    display.lcd_display_string("Raum 1", 2)

    room1_LED.on()
    sleep(5)
    room1_LED.off()

    display.lcd_clear()
