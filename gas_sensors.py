import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

# Set up I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS object
ads = ADS.ADS1015(i2c)

# Create analog input channels
channels = [AnalogIn(ads, ADS.P0),  # NH3
            AnalogIn(ads, ADS.P1),  # NOx
            AnalogIn(ads, ADS.P2),  # Alcohol
            AnalogIn(ads, ADS.P3)]  # Benzene, Smoke, CO2

# Calibration values
ZERO_NH3 = 500  # Replace with your own calibration value
ZERO_NOX = 500  # Replace with your own calibration value
ZERO_ALCOHOL = 500  # Replace with your own calibration value
ZERO_BENZENE = 500  # Replace with your own calibration value
ZERO_SMOKE = 500  # Replace with your own calibration value
ZERO_CO2 = 500  # Replace with your own calibration value

# Main loop
while True:
    # Read the sensor values
    nh3 = channels[0].value
    nox = channels[1].value
    alcohol = channels[2].value
    benzene = channels[3].value
    smoke = channels[3].value
    co2 = channels[3].value

    # Convert sensor values to gas concentrations
    nh3_conc = (nh3 - ZERO_NH3) / 10.0
    nox_conc = (nox - ZERO_NOX) / 10.0
    alcohol_conc = (alcohol - ZERO_ALCOHOL) / 10.0
    benzene_conc = (benzene - ZERO_BENZENE) / 10.0
    smoke_conc = (smoke - ZERO_SMOKE) / 10.0
    co2_conc = (co2 - ZERO_CO2) / 10.0

    # Print the gas concentrations
    print('NH3 Concentration: {:.2f} ppm'.format(nh3_conc))
    print('NOx Concentration: {:.2f} ppm'.format(nox_conc))
    print('Alcohol Concentration: {:.2f} ppm'.format(alcohol_conc))
    print('Benzene Concentration: {:.2f} ppm'.format(benzene_conc))
    print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))
    print('CO2 Concentration: {:.2f} ppm'.format(co2_conc))

    # Wait for some time before taking the next reading
    time.sleep(1)
