import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1015(i2c)

chan0 = AnalogIn(ads, ADS.P0)  
chan1 = AnalogIn(ads, ADS.P1) 
chan2 = AnalogIn(ads, ADS.P2) 

ZERO_LPG = 500 
ZERO_CO = 500 
ZERO_SMOKE = 500 

while True:
    lpg = chan0.value
    co = chan1.value
    smoke = chan2.value

    lpg_conc = (lpg - ZERO_LPG) / 10.0
    co_conc = (co - ZERO_CO) / 10.0
    smoke_conc = (smoke - ZERO_SMOKE) / 10.0

    print('LPG Concentration: {:.2f} ppm'.format(lpg_conc))
    print('CO Concentration: {:.2f} ppm'.format(co_conc))
    print('Smoke Concentration: {:.2f} ppm'.format(smoke_conc))
    print('\n')

    time.sleep(10)
