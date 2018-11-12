from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
6. Zmodyfikować program tak aby korzystał z zapisu heksadecymalnego 
"""

try:
    open()

    while(True): #pętla nieskończona
        led(int('9', 16))
        time.sleep(0.25)
        led(int('6', 16))
        time.sleep(0.25)
finally:
    close()
