import matplotlib.pyplot as plt
import numpy as np

def plot_volt_of_time(time, volt, max_volt):
    plt.figure(num = 1,figsize = (10, 6))
    plt.plot(time, volt, color = 'b')
    plt.xlabel("Время, с")
    plt.ylabel("напряжение, В")
    plt.xlim(0, max(time) + 0.1)
    plt.ylim(0, max_volt)
    plt.grid(linewidth = 0.5)
    plt.show(block = False)

def plot_sampl_T_hist(time):
    time_1 = np.array(time[1:])
    time_2 = np.array(time[:-1])
    delta_t = time_1 - time_2
    plt.figure(num = 2,figsize = (10, 6))
    plt.hist(delta_t)
    plt.xlim(0, 0.06)
    plt.grid(linewidth = 0.5)
    plt.show()
