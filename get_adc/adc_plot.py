import matplotlib.pyplot as plt

def plot_volt_of_time(time, volt, max_volt):
    plt.figure(figsize = (10, 6))
    plt.plot(time, volt, color = 'b')
    plt.xlabel("Время, с")
    plt.ylabel("напряжение, В")
    plt.xlim(0, max(time) + 0.1)
    plt.ylim(0, max_volt)
    plt.grid(linewidth = 0.5)
    plt.show()