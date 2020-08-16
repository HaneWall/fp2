import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import numpy as np

# Colors
BLUE = '#0077BB'
CYAN = '#33BBEE'
TEAL = '#009988'
ORANGE = '#EE7733'
RED = '#CC3311'
MAGENTA = '#EE3377'
GREY = '#BBBBBB'



def read_data(path):
    data = pd.read_csv(path, sep='\t', decimal='.', header=None)
    return data

def show_sf6(transform_u_toggle):
    if transform_u_toggle:
        u = read_data('sf6.txt')[0]
        u = model_func(u, 115.83, -42.344, 23.003)
    else:
        u = read_data('sf6.txt')[0]
    i = read_data('sf6.txt')[1]

    fig, axes = plt.subplots()
    axes.plot(u, i, color='TEAL')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    if transform_u_toggle:
        axes.set_xlabel(r'$m/e$')
    else:
        axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.set_title(r'$SF_6$')
    plt.show()

def show_sample_1(transform_u_toggle):
    if transform_u_toggle:
        u = read_data('Probe1_2.txt')[0]
        u = model_func(u, 115.83, -42.344, 23.003)
    else:
        u = read_data('Probe1_2.txt')[0]
    i = read_data('Probe1_2.txt')[1]

    fig, axes = plt.subplots()
    axes.plot(u, i, color='TEAL')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    if transform_u_toggle:
        axes.set_xlabel(r'$m/e$')
    else:
        axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.set_title(r'Probe 1')
    plt.show()

def show_sample_2(transform_u_toggle):
    if transform_u_toggle:
        u = read_data('Probe2.txt')[0]
        u = model_func(u, 115.83, -42.344, 23.003)
    else:
        u = read_data('Probe2.txt')[0]
    i = read_data('Probe2.txt')[1]

    fig, axes = plt.subplots()
    axes.plot(u, i, color='TEAL')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    if transform_u_toggle:
        axes.set_xlabel(r'$m/e$')
    else:
        axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.set_title(r'Probe 2')
    plt.show()

def show_krypton():
    u = read_data('krypton.txt')[0]
    i = read_data('krypton.txt')[1]

    fig, axes = plt.subplots()
    axes.plot(u, i, color='TEAL')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.set_title(r'Krypton')
    plt.show()

def show_both():
    u_k = read_data('krypton.txt')[0]
    i_k = read_data('krypton.txt')[1]

    u_s = read_data('sf6.txt')[0]
    i_s = read_data('sf6.txt')[1]

    peaks_sf6_indices = find_peak(data=i_s, minimal_height=1.08)[0]
    print(peaks_sf6_indices)
    peak_i = [i_s[index] for index in peaks_sf6_indices]
    peak_u = [u_s[index] for index in peaks_sf6_indices]

    fig, axes = plt.subplots()
    axes.plot(u_k, i_k, color='GREY', label='Krypton')
    axes.plot(u_s, i_s, color='TEAL', label=r'$SF_6$')
    axes.plot(peak_u, peak_i, color='RED', linestyle='None', marker='+')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.legend(loc='best')
    plt.show()

def find_peak(data, minimal_height):
    indices = find_peaks(x=data, height=minimal_height)
    return indices

def create_peak_data(data, minimal_height, transform_u_toggle):
    if transform_u_toggle:
        u_s = read_data(data)[0]
        u_s = model_func(u_s, 115.83, -42.344, 23.003)
    else:
        u_s = read_data(data)[0]
    i_s = read_data(data)[1]

    peaks_indices = find_peak(data=i_s, minimal_height=minimal_height)[0]
    if transform_u_toggle:
        peak_u = [int(u_s[index]) for index in peaks_indices]
    else:
        peak_u = [u_s[index] for index in peaks_indices]

    peak_data = pd.DataFrame(find_peak(data=i_s, minimal_height=minimal_height)[1])
    if transform_u_toggle:
        peak_data['m/e'] = peak_u
    else:
        peak_data['U/V'] = peak_u
    return peak_data

def model_func(u,a,b,c):
    return a*u**2 + b*u + c

def fit_u_to_me(u_peak_array, me_peak_array):
    u = np.arange(0.4, 1.3, 0.01)
    popt, pcov = curve_fit(model_func, xdata=u_peak_array, ydata=me_peak_array)
    standard_deviation = np.sqrt(np.diag(pcov))
    fig, axes = plt.subplots()
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'$\frac{m}{e}$')
    axes.plot(u, model_func(u, *popt), color='TEAL', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt), linestyle='dashed')
    axes.plot(u_peak_array, me_peak_array, linestyle='None', marker='o', color='RED', label='Data')
    axes.legend(loc='best')
    print(standard_deviation)
    plt.show()


# 0.410671
# 19
u_sf6_peaks = [0.512195, 0.552439, 0.712500, 0.734451, 0.843293, 0.956707, 1.057317, 1.149695]
me_sf6_peaks = [32, 35, 51, 54, 70, 89, 108, 127]

#fit_u_to_me(u_peak_array=u_sf6_peaks, me_peak_array=me_sf6_peaks)
#peak_data  = create_peak_data(data='sf6.txt', minimal_height=1.08)
#print(peak_data.to_latex())
#show_sf6(True)
#show_krypton()
#show_both()
#show_sample_1()
#peak_data_sample_1 = create_peak_data('Probe1_2.txt', 1.08, True)
#print(peak_data_sample_1.to_latex())
#show_sample_2()
peak_data_sample_2 = create_peak_data('Probe2.txt', 1.08, True)
print(peak_data_sample_2.to_latex())
