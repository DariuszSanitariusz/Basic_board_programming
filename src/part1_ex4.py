from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
4. Zmodyfikować program tak aby na przemian zapalał diody pierwszą i ostania oraz dwie środkowe (1001/0110) 
"""

try:
    open()

    while(True): #pętla nieskończona
        led(9)
        time.sleep(0.25)
        led(6)
        time.sleep(0.25)
finally:
    close()
