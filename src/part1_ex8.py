from board_driver_simulator_v2 import open,close,but,pot,det,led
import time

"""
8. Zmodyfikować program tak aby wyświetlał stan przycisków w postaci binarnej a następnie heksadecymalnej 
"""

try:
    open()

    led(0)
    while(True):
        print("Binary: " + bin(but()) + " Hexadecimal: " + hex(but()))

finally:
    close()
