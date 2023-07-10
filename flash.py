"""
Library functions in Micropython to run on the RPi Pico.
Lots copied from rtc.py
"""

from machine import Pin, SPI
import time

class Flash:
    def __init__(self):
        self.init()

    def init(self):
        self.spi = SPI(0, sck=Pin(2), mosi=Pin(3), miso=Pin(4), baudrate=2000000, phase=0)
        self.cs = Pin(5, Pin.OUT, value=1)

    def deinit(self):
        self.spi.deinit()
        self.cs.init(Pin.IN)

    # Write the command then read size bytes
    def read_bulk(self, command, size):
        self.cs.value(0)
        self.spi.write(bytes([command]))
        data = self.spi.read(size)
        self.cs.value(1)
        return data

    # Written for 0x03 commmand (READ)
    def read_data(self, addr, size):
        self.cs.value(0)
        toWrite = [addr >> 16 & 0xFF, addr >> 8 & 0xFF, addr & 0xFF]
        self.spi.write(bytes([0x03] + toWrite))
        data = self.spi.read(size)
        self.cs.value(1)
        return data

    # Written for the 0x02 command (PP) (writing)
    def page_program(self, addr, data):
        # enable writing
        self.cs.value(0)
        self.spi.write(bytes([0x06]))
        self.cs.value(1)

        # check read status register
        self.cs.value(0)
        self.spi.write(bytes([0x05]))
        read = self.spi.read(1)[0]
        self.cs.value(1)

        # check WEL (bit of status register)
        mask = 0b00000010
        read = int(read) & mask
        read = read >> 1

        # writing data
        if read == 1:
            lst = []
            toWrite = [addr >> 16 & 0xFF, addr >> 8 & 0xFF, addr & 0xFF]
            for i in range(len(data)):
                lst.append(ord(data[i]))
            self.cs.value(0)
            self.spi.write(bytes([0x02] + toWrite + lst))
            self.cs.value(1)
            return 1
        else:
            self.cs.value(1)
            return 0

    # Written for the 0x20 (SE) (erase)
    def sector_erase(self, addr):
        # enable writing
        self.cs.value(0)
        self.spi.write(bytes([0x06]))
        self.cs.value(1)

        # check read status register
        self.cs.value(0)
        self.spi.write(bytes([0x05]))
        read = self.spi.read(1)[0]
        self.cs.value(1)

        # check WEL (bit of status register)
        mask = 0b00000010
        read = int(read) & mask
        read = read >> 1

        # erases data
        if read == 1:
            toWrite = [addr >> 16 & 0xFF, addr >> 8 & 0xFF, addr & 0xFF]
            self.cs.value(0)
            self.spi.write(bytes([0x20] + toWrite))
            self.cs.value(1)
            return 1
        else:
            self.cs.value(1)
            return 0

