import RPi.GPIO as GPIO
import time

DHT_PIN = 4

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Function to read data from DHT11 sensor
def read_dht11_dat():
    hum = temp = 0
    bit_count = 0
    data = []

    # Send start signal to DHT11 sensor
    GPIO.setup(DHT_PIN, GPIO.OUT)
    GPIO.output(DHT_PIN, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(DHT_PIN, GPIO.HIGH)

    # Wait for response from DHT11 sensor
    GPIO.setup(DHT_PIN, GPIO.IN)
    while GPIO.input(DHT_PIN) == GPIO.LOW:
        pass
    while GPIO.input(DHT_PIN) == GPIO.HIGH:
        pass

    # Read data from DHT11 sensor
    while bit_count < 40:
        while GPIO.input(DHT_PIN) == GPIO.LOW:
            pass

        start = time.time()
        while GPIO.input(DHT_PIN) == GPIO.HIGH:
            pass
        end = time.time()

        duration = end - start
        if duration > 0.0001:
            data.append(1)
        else:
            data.append(0)

        bit_count += 1

    # Process data from DHT11 sensor
    hum = int.from_bytes(bytes(data[0:8]), byteorder='big')
    temp = int.from_bytes(bytes(data[16:24]), byteorder='big')
    return hum, temp

# Read data from DHT11 sensor and print to console
while True:
    humidity, temperature = read_dht11_dat()
    if humidity is not None and temperature is not None:
        print("Temperature={0:0.1f}C Humidity={1:0.1f}%".format(temperature/1.0, humidity/1.0))
    time.sleep(2) # wait for 2 seconds before next read
