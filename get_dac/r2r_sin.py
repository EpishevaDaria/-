import r2r_dac as r2r
import signal_gen as sg
import time

ampli = 3.2
signal_freq = 10
samp_freq = 1000
time = 0

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.146, True)

    while True:

        volt = sg.get_sin_ampl(signal_freq, time)
        dac.set_volt(volt)
        sg.wait_for_samp_per(samp_freq)
        time += 1/samp_freq

finally:
    dac.deinit()



