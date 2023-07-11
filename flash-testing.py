# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText 2023 Kristin Ebuengan
# SPDX-FileCopyrightText 2023 Melody Gill
# SPDX-FileCopyrightText 2023 Gabriel Marcano

"""
file to test the read/write/erase functions from flash.py
"""

from flash import *
from rtc import *
import time

flash = Flash(5)
rtc = RTC(10)

# write and erase timestamp to flash
print("read before write: " + str(flash.read_data(10,30)))
print("return: " + str(flash.page_program(10, str(rtc.get_time()))))
print("read after write: " + str(flash.read_data(10,30)))

print("return: " + str(flash.sector_erase(4)))

time.sleep(0.1)
print("read after erase: " + str(flash.read_data(10,30)))