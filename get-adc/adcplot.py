import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    # plt.plot(x, y)
    plt.grid(visible = True)
    # plt.xlim(3)
    # plt.ylim(max_voltage)
    plt.xlabel('t, c')
    plt.ylabel('U, B')
    plt.title('U(t)')
    plt.show()
def plot_sampling_period_hist(time):
    sampling_periods = []
    last = 0
    for i in time:
        sampling_periods.append(i - last)
        last = i

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.xlabel('t, c')
    plt.ylabel('n')
    plt.title('n(t)')
    plt.xlim(0, 0.06)
    plt.grid(visible = True)
    plt.show()

    