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


def show_all():
	theta = []
	n = []
	for i in range(9, 33, 3):
		theta.append(read_data('/Users/erikweilandt/Documents/University/fp2/roentgen/resources/lif_'+str(i)+'_10_01_4_.txt')[0])
		n.append(read_data('/Users/erikweilandt/Documents/University/fp2/roentgen/resources/lif_'+str(i)+'_10_01_4_.txt')[1])

	fig, axes = plt.subplots()
	for j in range(0, 8):
		axes.plot(theta[j], n[j], color='GREY', label='Krypton')
	# axes.plot(theta30, n30, color='TEAL', label=r'$SF_6$')
	# axes.plot(peak_u, peak_i, color='RED', linestyle='None', marker='+')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$U$ in $V$')
	axes.set_ylabel(r'Intensität $I$')
	axes.legend(loc='best')
	plt.show()


show_all()
