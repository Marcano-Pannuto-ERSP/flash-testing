from flash import *
flash = Flash()
print("read before: " + str(flash.read_data(4,2)))
print("return: " + str(flash.page_program(4,"hi")))
print("read after: " + str(flash.read_data(4,2)))