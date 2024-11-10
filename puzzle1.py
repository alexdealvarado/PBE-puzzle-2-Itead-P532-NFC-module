import board #permite interactuar con los pines fisicos de la raspberry
import busio #conecta con los buses I2C, SPI o UART

#permite la comunicacion entre la raspberry y el modelo PN532 a traves del protocolo I2C
from adafruit_pn532.i2c import PN532_I2C

class Rfid:
	def __init__(self):
		#configuracion de la comunicacion I2C con el modulo PN532
		i2c = busio.I2C(board.SCL, board.SDA)
		self.pn532 = PN532_I2C(i2c, debug=False)
		
		#configuramos PN532 para habilitar la comunicacion con las tarjetas
		self.pn532.SAM_configuration()
		
	def read_uid(self):
		#el codigo verifica continuamente si hay una tarjeta NFC disponible para leer
		#si detecta una, imprime su identificador, de lo contrario, sigue esperando
		#print("Waiting for a card...")
		while True:
			#intenta leer si hay alguna tarjeta accesible
			uid = self.pn532.read_passive_target(timeout=0.5)
			#print(".")
			
			if uid is not None:
				return ''.join(['{:0X}'.format(i) for i in uid])

if __name__ == "__main__":
	rf = Rfid()
	uid = rf.read_uid()
	print(f"Found card with UID: {uid}")
