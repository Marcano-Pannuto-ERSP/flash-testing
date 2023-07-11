# flash-testing

## Embedded Device Drivers
Uses a Raspberry Pi Pico to write/read/erase from flash chip MX25V16066M2I02 and to communicate with the RTC AM1815.

`flash.py` contains functions to initialize the flash chip and use the read, page program, and sector erase commands. 

**NOTICE:** Before using any of the functions you will have to upload `rtc.py` and `flash.py` on the Rasberry Pi Pico.

`flash-testing.py` contains a test example of how to use the functions.

Here is the datasheet of the flash chip for more details: https://www.macronix.com/Lists/Datasheet/Attachments/8879/MX25V16066,%202.5V,%2016Mb,%20v1.4.pdf

**NOTICE:** The RTC is on pin 10 and the flash chip is on pin 5