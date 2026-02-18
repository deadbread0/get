import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)

leds = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setup (leds, GPIO.OUT)
GPIO.output (leds, 0)
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    return int(voltage / dynamic_range * 255)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def number_to_dac(number):
    GPIO.output(leds, decimal2binary(number))

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
            dac_bits = decimal2binary(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
