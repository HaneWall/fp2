import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

BLUE = '#0077BB'
CYAN = '#33BBEE'
TEAL = '#009988'
ORANGE = '#EE7733'
RED = '#CC3311'
MAGENTA = '#EE3377'
GREY = '#BBBBBB'


def read_data(path):
	df = pd.read_csv('./resources/' + path, sep=' ', decimal='.', header=None)
	return df.to_numpy()


def show_spec(path, labels):
	i = 0
	fig, axes = plt.subplots(ncols=1, nrows=len(path))
	for path in path:
		frequence = read_data(path)[:, 0]
		amplitude = read_data(path)[:, 1]

		axes[i].plot(frequence, amplitude, color=TEAL, marker='+', label=labels[i])
		axes[i].grid(True, color='black', linestyle='dashed', alpha=0.2)
		axes[i].set_xlabel('frequence in Hz')
		axes[i].set_ylabel(r'amplitude')
		axes[i].legend(loc='best')
		i = i + 1
	plt.show()

def peak_alpha_plot(path):
	# for path in path:
	# 	indices, _ = find_peak(read_data(path)[:, 1], 10)
	# 	peak_values = read_data(path)[indices, :]
	# 	print(peak_values)
	peak1 = np.array([39.938, 33.978, 32.498, 33.404, 28.64, 18.582, 12.634, 27.43, 42.152, 53.847])
	peak2 = np.array([17.01, 20.806, 20.781, 24.253, 27.508, 28.312, 25.302, 26.384, 52.119, 58.032])
	alpha = pd.DataFrame([0, 10, 30, 50, 70, 90, 110, 130, 150, 180]) #TODO: edit alpha to theta
	alpha[0] = np.arccos(1/2*(np.cos(alpha[0])-1))
	fig, axes = plt.subplots()
	axes.plot(alpha[0], peak1, color=TEAL, marker='+')
	axes.plot(alpha[0], peak2, color=RED, marker='*')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$\alpha$ in $\degree$')
	axes.set_ylabel(r'amplitude')
	plt.show()






def find_peak(data, minimal_height):
	indices = find_peaks(x=data, height=minimal_height)
	return indices

task1_2_data_list = ['aufgabe_1_2_resonanzen_0r.dat',
					 'aufgabe_1_2_resonanzen_10r.dat',
					 'aufgabe_1_2_resonanzen_30r.dat',
					 'aufgabe_1_2_resonanzen_50r.dat',
					 'aufgabe_1_2_resonanzen_70r.dat',
					 'aufgabe_1_2_resonanzen_90r.dat',
					 'aufgabe_1_2_resonanzen_110r.dat',
					 'aufgabe_1_2_resonanzen_130r.dat',
					 'aufgabe_1_2_resonanzen_150r.dat',
					 'aufgabe_1_2_resonanzen_180r.dat']

task2_list = ['alpha_0r_100_10000.dat',
			  'alpha_180_100_10000.dat']
task2_labels = [r'spectrum $\alpha=0\degree$',
				r'spectrum $\alpha=180\degree$']

#Aufgabe 1
#show_spec('aufgabe1.dat')
#show_spec(task1_2_data_list) # peak control
#peak_alpha_plot(task1_2_data_list)

#Aufgabe2
show_spec(task2_list, task2_labels)
