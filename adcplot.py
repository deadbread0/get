import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    # plt.plot(x, y)
    # plt.xlim()
    plt.ylim(5)
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Линейный график')
    plt.show()

    