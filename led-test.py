# Bibliotheken laden
from gpiozero import Button, LED
import lcd_drivers
from signal import pause

display = lcd_drivers.Lcd()

# Initialisierung von GPIO27 als Button (Eingang)
button = Button(27)

# Initialisierung von GPIO17 als LED (Ausgang)
led = LED(12)


button.wait_for_press()

button.when_pressed = led.on()
print(str(led.value))

button.when_released = led.off()
print(str(led.value))





#button.when_released = led.off

pause()


# # Warten auf Druck auf Button
# button.wait_for_press()

# def btnpress():
#     print("button pressed")
#     led.on()

# button.value()

# # Text-Ausgabe
# button.when_pressed = btnpress()

# button.when_released  = led.off


# # while True:

# #     # Wenn der Button gedrückt wird
# #     button.when_pressed = led.on()


#     led_HighLow = led.value

#     if led_HighLow == 1:
#         display.lcd_clear()
#         display.lcd_display_string("Led ON",1)
#     else:
#         display.lcd_clear()
#         display.lcd_display_string("Led OFF",1)

#     #print(str(led_HighLow))

   
   


