from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
1. Napisać program który będzie na przemian zapalał i gasił diodę świecącą numer 0 2
"""

try:
    open()

    while(True):
        led(1)
        time.sleep(1)
        led(0)
        time.sleep(1)
finally:
    close()
