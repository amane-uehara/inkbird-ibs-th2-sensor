#!/usr/bin/python3
import bluepy
from struct import unpack
from json import dump

mac_addr = '01:23:45:67:89:AB'

def main():
  for i in range(100):
    try:
      device = bluepy.btle.Peripheral(mac_addr)
      c = device.readCharacteristic(0x24)
      device.disconnect()
      (temperature, humidity, is_sensor_external, crc16_modbus) = unpack('<hhBH', c)
      print("{},{}".format(temperature, humidity))
    except:
      continue
    else:
      break

if __name__ == "__main__":
  main()

