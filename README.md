# micropython-mfrc522-ESP32
(Micro)Python class to access the MFRC522 RFID reader, now with support to ESP32 Boards

Basic class to access RFID readers of the type [MFRC522](http://www.nxp.com/documents/data_sheet/MFRC522.pdf).
This is a fork of [wendlers](https://github.com/wendlers/micropython-mfrc522) that did a great job.

I've trying all this stuff on ESP32 (WROOM-32) boards and [Thonny IDE](https://thonny.org/) 

## Usage

Put the modules ``mfrc522.py``, ``examples/main.py``, to the root of the flash FS on your board. 
For this purpose you can connect to serial port using PuTTY and REPL or the Micropython interpreter on Thonny IDE.
You can check this brief and useful [tutorial](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/)
I used the following pins for my setup on examples/main.py:

| Signal    | GPIO ESP32   |
| --------- | ------------ |
| sck       | 18           |
| mosi      | 23           |
| miso      | 19           |
| rst       | 21           |
| cs        | 15           |
 
Any pin that can be used to output signals can be used as a pin for SPI communication.
