from gpiozero import MotionSensor, LED, Button
from signal import pause
from time import sleep


led1 = LED(17)

while True:
	print("start")
	led1.on()
	sleep(1)
	led1.off()
	sleep(1)


