from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
2. Zmodyfikować program tak aby na przemian zapalał diodę 0 i 1 (01,10,01…)
"""

try:
	open()

	while(True):
		led(1)
		time.sleep(1)
		led(2)
		time.sleep(1)
finally:
	close()