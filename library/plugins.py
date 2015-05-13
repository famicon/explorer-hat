import time
import explorerhat

class ShiftRegister:
	def __init__(self):
		self.rclk = explorerhat.output.one
		self.srclk = explorerhat.output.two
		self.ser = explorerhat.output.three

	def toggle_pin(self, pin, state):
		self.rclk.on()
		for p in range(8):
			self.srclk.on()
			if p == pin:
				if state == 1:
					self.ser.off()
				else:
					self.ser.on()
			else:
				if state == 1:
					self.ser.on()
				else:
					self.ser.off()
			self.srclk.off()
		self.rclk.off()

	def chase(self, delay=0.2):
		for i in range(8):
			self.toggle_pin(i, 1)
			time.sleep(delay)

	def scan(self, delay=0.2):
		for i in range(8) + range(1,7)[::-1]:
			self.toggle_pin(i, 1)
                        time.sleep(delay)

	def toggle_all(self, state):
		self.rclk.on()
		for p in range(8):
			self.srclk.on()
			if state == 1:
				self.ser.off()
			else:
				self.ser.on()
			self.srclk.off()
		self.rclk.off()

	def toggle_odd(self, state):
		self.rclk.on()
                for p in range(0,8):
                        self.srclk.on()
			if p % 2 != 0:
	                        if state == 1:
        	                        self.ser.off()
        	                else:
                	                self.ser.on()
			else:
				self.ser.on()
                        self.srclk.off()
                self.rclk.off()

	def toggle_even(self, state):
                self.rclk.on()
                for p in range(0,8):
                        self.srclk.on()
                        if p % 2 == 0:
                                if state == 1:
                                        self.ser.off()
                                else:
                                        self.ser.on()
                        else:
                                self.ser.on()
                        self.srclk.off()
                self.rclk.off()

	def demo(self):
		try:
			while True:
				for i in range(5):
					for j in range(2):
						self.toggle_all(j)
						time.sleep(0.1)
				for i in range(5):
                                        self.chase(delay=0.1)
				for i in range(5):
					self.toggle_odd(0)
					self.toggle_even(1)
					time.sleep(0.1)
					self.toggle_even(0)
					self.toggle_odd(1)
					time.sleep(0.1)
				for i in range(5):
					self.scan(delay=0.1)
		except:
			pass
		finally:
			self.toggle_all(0)
