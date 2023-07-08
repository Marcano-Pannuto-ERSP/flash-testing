"""
Library functions in Micropython to run on the RPi Pico.
Lots copied from rtc.py
"""

from machine import Pin, SPI

class Flash:
    def __init__(self):
        self.init()

    def init(self):
        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4), baudrate=2000000, phase=0)
        self.cs = Pin(5, Pin.OUT, value=1)

    def deinit(self):
        self.spi.deinit()
        self.cs.init(Pin.IN)

    def read_byte(self, command):
        self.cs.value(0)
        self.spi.write(bytes([command]))
        data = self.spi.read(1)[0]
        self.cs.value(1)
        return data

    def write_byte(self, command, data=None):
        self.cs.value(0)
        if data == None:
            self.spi.write(bytes([command]))
        else:
            self.spi.write(bytes([command, data]))
        self.cs.value(1)

    # Write the command then read size bytes
    def read_bulk(self, command, size):
        self.cs.value(0)
        self.spi.write(bytes([command]))
        data = self.spi.read(size)
        self.cs.value(1)
        return data

    # Written for 0x03 commmand
    def read_data(self, size, addr):
        self.cs.value(0)
        toWrite = [addr >> 16 & 0xFF, addr >> 8 & 0xFF, addr & 0xFF]
        self.spi.write(bytes([0x03] + toWrite))
        data = self.spi.read(size)
        self.cs.value(1)
        return data

    # not sure abt this one
    # probably do the same thing with data=None
    def write_bulk(self, command, data):
        self.cs.value(0)
        self.spi.write(bytes([command]) + data)
        self.cs.value(1)