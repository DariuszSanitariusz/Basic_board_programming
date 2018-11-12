from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
5. Zmodyfikować program tak aby korzystał z zapisu binarnego (argument funkcji „led”) 
"""

try:
    open()

    while(True): #pętla nieskończona
        led(int('1001', 2))
        time.sleep(0.25)
        led(int('110', 2))
        time.sleep(0.25)
finally:
    close()
