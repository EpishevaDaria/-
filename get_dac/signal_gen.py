import numpy as np
import time

def get_sin_ampl(freq, time):
    pi = np.pi
    faze = (time % (1/freq))/(1/freq)
    angle = 2 * pi * faze
    ampl = np.sin(angle)
    amp_cor = (ampl + 1)/2
    return(amp_cor)

def wait_for_samp_per(samp_freq):
    time.sleep(1/samp_freq)





