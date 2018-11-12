from board_driver_simulator_v2 import open,close,but,pot,det,led
import time
"""
3. Ponieważ trudno jest stwierdzić czy diody zapalają się na przemian 
dodać w odpowiednie miejsce wywołania funkcji wprowadzającej opóźnienie „time.sleep(0.25)” 
(funkcja „sleep” z modułu „time”, opóźnienie ¼ sekundy) 
"""
try:
	open()

	while(True):
		led(1)
		time.sleep(0.25)
		led(2)
		time.sleep(0.25)
finally:
	close()
