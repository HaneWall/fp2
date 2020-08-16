import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
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

def show_sf6():
    u = read_data('sf6.txt')[0]
    i = read_data('sf6.txt')[1]

    fig, axes = plt.subplots()
    axes.plot(u, i, color='TEAL')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel(r'$U$ in $V$')
    axes.set_ylabel(r'Intensität $I$')
    axes.set_title(r'$SF_6$')
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


#show_sf6()
#show_krypton()
show_both()