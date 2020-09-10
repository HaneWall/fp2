import matplotlib.pyplot as plt
from scipy.integrate import trapz
import pandas as pd
import numpy as np

BLUE = '#0077BB'
CYAN = '#33BBEE'
TEAL = '#009988'
ORANGE = '#EE7733'
RED = '#CC3311'
MAGENTA = '#EE3377'
GREY = '#BBBBBB'

color_spec = [BLUE, CYAN, TEAL, ORANGE, RED, MAGENTA, GREY, 'black', 'green']

paths_Si = ['Data_17_0.txt', 'Data_17_1.txt', 'Data_17_2.txt', 'Data_17_3.txt', 'Data_17_4.txt']

paths_poly = ['Data_18_0.txt', 'Data_19_0.txt', 'Data_20_0.txt', 'Data_21_0.txt', 'Data_22_0.txt', 'Data_23_0.txt', 'Data_24_0.txt', 'Data_24_1.txt', 'Data_24_2.txt',
       'Data_24_3.txt', 'Data_24_4.txt', 'Data_24_5.txt']

paths_poly_right= ['Data_24_1.txt', 'Data_24_2.txt',
       'Data_24_3.txt', 'Data_24_4.txt', 'Data_24_5.txt']

def read_data(paths):
    if isinstance(paths, list):
        df_list = []
        for path in paths:
            df_list.append(pd.read_csv('./ww/' + path, sep='\t', decimal=',', header=None, skiprows=[0, 1]))
        return df_list
    else:
        df = pd.read_csv('./ww/' + paths, sep='\t', decimal=',', header=None, skiprows=[0, 1])
        return df


def calculate_work(df):
    k_s = 1371.6
    x = np.array(df[0])
    y_1 = k_s * np.array(df[1])
    y_2 = k_s * np.array(df[3])
    diff = y_1 - y_2
    work = trapz(y=diff, x=x)
    return work

def plot(df_list):
    fig, axes = plt.subplots()
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel('Höhe in m')
    axes.set_ylabel('DFL-Strom in Ampere')

    for df, ind in zip(df_list, range(len(df_list))):
        axes.plot(df[0], df[1], color=color_spec[ind], label=' ')
        axes.plot(df[2], df[3], color=color_spec[ind], linestyle='dashed')
    plt.figlegend(loc='upper center', ncol=len(df_list), title='Verschiedene Versuche', edgecolor='black', fancybox=False)
    plt.show()


def plot_work(df_list):
    k_s = 1371.6
    fig, axes = plt.subplots()
    axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
    axes.set_xlabel('Höhe in m')
    axes.set_ylabel('F in N')

    for df, ind in zip(df_list, range(len(df_list))):
        axes.plot(df[0], k_s*df[1], color=color_spec[ind], label='Arbeit {}'.format(calculate_work(df)))
        axes.plot(df[2], k_s*df[3], color=color_spec[ind], linestyle='dashed')
    plt.figlegend(loc='upper center', ncol=len(df_list), title='Verrichtete Arbeiten in J', edgecolor='black', fancybox=False)
    plt.show()

plot_data = read_data(paths_poly_right)
#plot(plot_data)
plot_work(plot_data)