from board_driver_simulator_v2 import open,close,but,pot,det,led
import time


try:
    open()
    led(0)
    ledy = 0
    zwrot= 0
    while(True):
        # print(zwrot)
        zwrot = but()
        if(zwrot):
            ledy = ledy ^ zwrot
            # print("zwrot: " + str(zwrot) + " ledy:" + str(ledy) + " | XOR: " + (bin(zwrot)) + " ^ " + (bin(ledy)) + " = " +  (bin(zwrot^ledy)) + " | DEC: " + (str(zwrot^ledy)))
            led(ledy)
            time.sleep(0.2)

finally:
    close()