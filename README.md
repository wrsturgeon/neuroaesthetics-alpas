# Penn Center for Neuroaesthetics Ambient Light Sensor

Written in **CircuitPython** for ease of use and maintenance. Currently tested on an **Unexpected Maker Feather S3** with an **Adafruit BH1750** soldered such that `VIN 3Vo GND SCL SDA` on the BH1750 lines up with `1 38 33 SCL SDA` on the Feather. Note that `ADDR` is left unsoldered and `3Vo`/`38` is unused and can also be left unsoldered, but that might be more of an inconvenience than just soldering it anyway.
