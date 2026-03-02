import r2r_adc as r2r
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import adc_plot as a_plt

adc_p = r2r.R2R_ADC(3.294, comp_time = 0.0001, verbose = True)


volt_lst = []
time_lst = []
duration = 3.0
try:
    time_0 = datetime.now()
    while (datetime.now() - time_0).total_seconds() <= duration:
        volt_lst.append(adc_p.get_sc_voltage())
        time_lst.append((datetime.now() - time_0).total_seconds())
    a_plt.plot_volt_of_time(time_lst, volt_lst, adc_p.dyn_rg)
finally:
    adc_p.deinit()