import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
import adcplot

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.0001, verbose = False):

        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])
    def sequential_counting_adc(self):
        num = 0
        self.number_to_dac(num)
        time.sleep(self.compare_time)
        while(not GPIO.input(self.comp_gpio)):
            time.sleep(self.compare_time)
            num += 1
            if num > 255:
                break
            self.number_to_dac(num)
        self.number_to_dac(0)
        return num
    def get_sc_voltage(self):
        return self.sequential_counting_adc() * self.dynamic_range / 255

if __name__ == "__main__":
    voltage_values = []
    time_values = []
    duration = 3.0
    adc = R2R_ADC(3.300)
    try:
        time_0 = 0
        while (time_0 / 1e9 < duration):
            time_0 = time.time_ns()
            volt = adc.get_sc_voltage()
            print(volt)
            time_values.append((time_0) / 1e9)
            voltage_values.append(volt)

        adcplot.plot_voltage_vs_time(time_values, time_values, adc.dynamic_range)
        
    finally:
        adc.deinit()

