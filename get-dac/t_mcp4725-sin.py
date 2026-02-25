import mcp4725_driver as mcp
import t_signal_generator as sg

amplitude = 3.2
signal_frequency = 2
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        amplitude = float(input("Введите амплитуду: "))
        signal_frequency = float(input("Введите частоту сигнала: "))
        sampling_frequency = float(input("Введите частоту дискретизации: "))
        dac = mcp.MCP4725(4.23, verbose = False)
        k = 0
        while True:
            voltage = amplitude*sg.get_t_wave_amplitude(signal_frequency, 1/sampling_frequency*k)
            k += 1
            sg.wait_for_sampling_period(sampling_frequency)
            dac.set_voltage(voltage)
    except ValueError:
        print("Число введено неправильно!")

    finally:
        dac.deinit()