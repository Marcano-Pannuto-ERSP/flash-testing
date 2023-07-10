from flash import *
import time

flash = Flash()
print("read before: " + str(flash.read_data(4,4)))
print("return: " + str(flash.page_program(4, "heyo")))
print("read after write: " + str(flash.read_data(4,4)))
print("return: " + str(flash.sector_erase(4)))

time.sleep(1)
print("read after erase: " + str(flash.read_data(4,4)))