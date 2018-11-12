from board_driver_simulator_v2 import open, close, but, pot, det, led
import time

"""
5. Funkcja get_detector() zwracająca ‘active’, 
jeżeli marker na tarczy będzie znajdował się nad detektorem krańcowym oraz ‘no_active’ w przeciwnym przypadku.
Test 1: Program obracający tarczę w prawo i jednocześnie wyświetlający wynik wywołania funkcji get_detector()
Test 2: Program, który będzie obracał tarczę w prawo do momentu aż marker osiągnie detektor.
Następnie program powinien kończyć działanie.

"""
try:
    open()

    def set_point(position):
        if position == 0:
            led(1)  # 0b0001
        elif position == 1:
            led(2)  # 0b0010
        elif position == 2:
            led(4)  # 0b0100
        elif position == 3:
            led(8)  # 0b1000
        else:
            led(0)


    def get_key():
        key = but()
        if key == 1:
            return 0
        elif key == 2:
            return 1
        elif key == 4:
            return 2
        elif key == 8:
            return 3
        else:
            return -1

    point = 0

    def step(direction):
        global point  # zmienna globalna
        if direction == 'right':
            point += 1
        elif direction == 'left':
            point -= 1
        point = point % 4
        set_point(point)


    def get_detector():
        det_state = det()
        if det_state == 1:
            return 'active'  # Uwaga: na board no_active, sim. active
        elif det_state == 0:
            return 'no_active'  # Uwaga: na board active, sim. no_active


    while (True):  # pętla nieskończona
        key = get_key()
        print(get_detector())
        if key != -1:
            print("Naciśnięto przycisk nr: ", key)
            if key == 0:
                step('left')  # to aby wyjść ze stanu  det
                while (get_detector() == 'no_active'):
                    step('left')
                    print('no_active')
            elif key == 1:
                step('right')  # to aby wyjść ze stanu det
                while (get_detector() == 'no_active'):
                    step('right')
                    print('no_active')
finally:
    close()
