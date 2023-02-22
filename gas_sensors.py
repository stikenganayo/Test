import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

# Set up I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS object
ads = ADS.ADS1015(i2c)

# Create an analog input channels
chan0 = AnalogIn(ads, ADS.P0)  # LPG
chan1 = AnalogIn(ads, ADS.P1)  # CO
chan2 = AnalogIn(ads, ADS.P2)  # Smoke

# Calibration values
ZERO_LPG = 500  # Replace with your own calibration value
ZERO_CO = 500  # Replace with your own calibration value
ZERO_SMOKE = 500  # Replace with your own calibration value

# Main loop
while True:
    # Read the sensor values
    lpg = chan0.value
    co = chan1.value
    smoke = chan2.value

    # Convert sensor values to gas concentrations
    lpg_conc = (lpg - ZERO_LPG) / 10.0
    co_conc = (co - ZERO_CO) / 10.0
    smoke_conc = (smoke - ZERO_SMOKE) / 10.0

    # Print the gas concentrations
    print('LPG Concentration: {:.2f} ppm'.format(lpg_conc))
    print('CO Concentration: {:.2f} ppm'.format(co_conc))
    print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))

    # Wait for some time before taking the next reading
    time.sleep(1)
