from machine import Pin
import mfrc522, time

rfid = mfrc522.MFRC522(
    18, # SCLK
    23, # MOSI
    19, # MISO
    21, # RST
    15  # SDA (CS)
)

led = Pin(1, Pin.OUT)

while True:

    led.value(0)
    stat, tag_type = rfid.request(rfid.REQIDL)

    if stat == rfid.OK:
        stat, raw_uid = rfid.anticoll()
        if stat == rfid.OK:
            led.value(1)

            
            id = "%02X%02X%02X%02X" % (raw_uid[0], raw_uid[1],
                                       raw_uid[2], raw_uid[3])
            print("ID ：", id)

            time.sleep(0.5)