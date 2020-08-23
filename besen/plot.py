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

def read_data_task3(path):
    df = pd.read_csv('./Besen_daten/' + path, sep=';', decimal=',')
    return df

def show_spectrum_sensor():
    spectrum_sensor = np.transpose(read_data('Blatt 1-Tabelle 1.csv'))
    fig, axes = plt.subplots()
    axes.plot(spectrum_sensor[0], spectrum_sensor[1], color=TEAL, marker='+')
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel('Frequenz in kHz')
    axes.set_ylabel(r'$U_{sensor}$')
    plt.show()

def show_table_task3():
    data_table = read_data_task3('Blatt 4-Tabelle 1.txt')
    U_0 = read_data_task3('Blatt 2-Tabelle 1.txt')
    for i in range(1, 4):
        data_table.loc[10, 'U_d'+str(i)] = data_table['U_d'+str(i)].mean()
    data_table['U_0'] = U_0
    data_table.loc[10, 'U_0'] = data_table['U_0'].mean()*10
    print(data_table.to_latex())
    data_table = data_table.to_numpy()
    print(data_table[-1])
    results = 20*np.log10(data_table[-1][0:3]/(10*data_table[-1][3]))
    print(results)


#show_spectrum_sensor()
show_table_task3()