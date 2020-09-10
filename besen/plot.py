import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BLUE = '#0077BB'
CYAN = '#33BBEE'
TEAL = '#009988'
ORANGE = '#EE7733'
RED = '#CC3311'
MAGENTA = '#EE3377'
GREY = '#BBBBBB'

color_spec = [BLUE, CYAN, TEAL, ORANGE, RED, MAGENTA, GREY, 'black']

def read_data(path):
    df = pd.read_csv('./Besen_daten/'+path, sep=';', decimal=',')
    return df.to_numpy()

def show_spectrum_sensor():
    spectrum_sensor = np.transpose(read_data('Blatt 1-Tabelle 1.csv'))
    fig, axes = plt.subplots()
    axes.plot(spectrum_sensor[0], spectrum_sensor[1], color=TEAL, marker='+')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel('Frequenz in kHz')
    axes.set_ylabel(r'$U_{sensor}$')
    plt.show()


show_spectrum_sensor()