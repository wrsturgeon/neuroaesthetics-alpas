# basic imports
import board

# for the onboard light sensor
# import analogio

# for communication with the sensor
import adafruit_bh1750
import busio
import digitalio

# for running a task exactly every N minutes
import time

# for Internet capabilities
import adafruit_requests
import ipaddress
import socketpool
import ssl
import wifi

# WiFi info
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise


def wait_5m(next_time: time.struct_time) -> time.struct_time:
    # print("previous time:", next_time)
    year, mon, day, hour, min, sec, day_of_wk, day_of_yr, _ = next_time
    sec = 0
    min = ((min // 5) + 1) * 5
    next_time = time.struct_time(
        (year, mon, day, hour, min, sec, day_of_wk, day_of_yr, -1)
    )
    # print("waiting until", next_time)
    time.sleep(max(0, time.mktime(next_time) - time.mktime(time.localtime())))
    return next_time


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

gnd = digitalio.DigitalInOut(board.IO33)
gnd.direction = digitalio.Direction.OUTPUT
gnd.value = False

vin = digitalio.DigitalInOut(board.IO1)
vin.direction = digitalio.Direction.OUTPUT
vin.value = True

# onboard_amb = analogio.AnalogIn(board.AMB)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bh1750.BH1750(i2c, 0x23)

while True:
    try:
        print()
        print("Connecting to WiFi...")
        print("MAC address is", [hex(i) for i in wifi.radio.mac_address])
        print("All available WiFi networks:")
        for network in wifi.radio.start_scanning_networks():
            print(
                '    "{}" (RSSI {}, Channel {})'.format(
                    str(network.ssid, "utf-8"), network.rssi, network.channel
                )
            )
        print("    [end of list]")
        wifi.radio.stop_scanning_networks()

        print("Connecting to %s..." % secrets["ssid"])
        wifi.radio.connect(secrets["ssid"], secrets["wifi_pw"])
        print("    Done! Sensor IP address:", wifi.radio.ipv4_address)

        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())

        # see https://learn.adafruit.com/pyportal-email-display/internet-connect
        print("-" * 40)
        print(requests.get("http://wifitest.adafruit.com/testwifi/index.html").text)
        print("-" * 40)

        next_time = time.localtime()

        while True:
            next_time = wait_5m(next_time)
            led.value = True
            # print(onboard_amb.value)
            print("{:8.2f} lux".format(sensor.lux))

            next_time = wait_5m(next_time)
            led.value = False
            # print(onboard_amb.value)
            print("{:8.2f} lux".format(sensor.lux))
    except _:
        pass
