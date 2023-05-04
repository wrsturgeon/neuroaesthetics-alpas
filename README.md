# Penn Center for Neuroaesthetics Ambient Light Sensor

Written in **CircuitPython** for ease of maintenance in case something goes wrong from across the country.

Currently tested on an **Unexpected Maker Feather S3** with an **Adafruit BH1750** soldered with `VIN 3Vo GND SCL SDA` on the BH1750 connected to `1 38 33 SCL SDA` on the Feather, respectively. Note that `ADDR` is left unsoldered and `3Vo`/`38` is unused but soldered anyway to avoid having to chop header pins in half.

## Setup

Obtain a CircuitPython-compatible microcontroller and copy everything in this folder into it, overwriting where applicable. Then, add a `secrets.py` file that looks like this:
```python
secrets = {
    "ssid": "replace me with your WiFi network name",
    "password": "replace me with your WiFi password",
}
```
And everything should work! The blue light should flash on or off every five minutes, alternating with each measurement.
