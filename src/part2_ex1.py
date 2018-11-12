from board_driver_simulator_v2 import open,close,but,pot,det,led
import time
"""
1. Napisać funkcję set_point(position), 
która zaświeci diodę świecącą o zadanej pozycji(od 0 do 3). 
Pozostałe diody powinny być zgaszone. 
Podanie argumentu z poza zakresu 0-3 powinno 
skutkować zgaszeniem wszystkich diod.
Użyć sekwencji if,elif,elif..

Test:Program zapalający diodę odpowiadającą naciśnietemu przyciskowi.
UWAGA: po upewnieniu się, że funkcja set_point zapala 
tylko jedną diodę zewrzeć zworkę na płytce a następnie 
zaobserwować zachowanie się tarczy podczas naciskania 
kolejnych przycisków.

tarcza się kręci po naciskaniu przycisków po kolei
za każdym razem o jeden "stopień"
jak ma sie kręcić to lampki muszą sie zapalać po kolei
"""
try:
	open()

	def set_point(position):
		if position==0:
			led(1) #0b0001
		elif position==1:
			led(2) #0b0010
		elif position==2:
			led(4) #0b0100
		elif position==3:
			led(8) #0b1000
		else:
			led(0)
	while(True): #pętla nieskończona
		key=but()
		if key==1:
			set_point(0)
		elif key==2:
			set_point(1)
		elif key==4:
			set_point(2)
		elif key==8:
			set_point(3)
		else:
			set_point(-1)
finally:
	close()
