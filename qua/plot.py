import matplotlib.pyplot as plt
import matplotlib.projections.polar
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


def read_polar_data(path):
	df = pd.read_csv('./resources/' + path, sep=' ', decimal='.')
	return df


def show_spec(path, labels):
	if path is list:
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

	else:
		frequence = read_data(path)[:, 0]
		amplitude = read_data(path)[:, 1]

		fig, axes = plt.subplots()
		axes.plot(frequence, amplitude, color=TEAL, marker='+', label=labels)
		axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
		axes.set_xlabel('frequence in Hz')
		axes.set_ylabel(r'amplitude')
		axes.legend(loc='best')
	plt.show()


def peak_alpha_plot(path):
	# for path in path:
	# 	indices, _ = find_peak(read_data(path)[:, 1], 10)
	# 	peak_values = read_data(path)[indices, :]
	# 	print(peak_values)
	peak1 = np.array([39.938, 33.978, 32.498, 33.404, 28.64, 18.582, 12.634, 27.43, 42.152, 53.847])
	peak2 = np.array([17.01, 20.806, 20.781, 24.253, 27.508, 28.312, 25.302, 26.384, 52.119, 58.032])
	alpha = pd.DataFrame([0, 10, 30, 50, 70, 90, 110, 130, 150, 180])  # TODO: edit alpha to theta
	alpha[0] = np.arccos(1 / 2 * (np.cos(alpha[0]) - 1))
	fig, axes = plt.subplots()
	axes.plot(alpha[0], peak1, color=TEAL, marker='+')
	axes.plot(alpha[0], peak2, color=RED, marker='*')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$\alpha$ in $\degree$')
	axes.set_ylabel(r'amplitude')
	plt.show()


def show_polar_plots(path, labels):
	m = 1 # index for the plots
	fig = plt.figure()
	for i in range(5):
		try:
			data = read_polar_data(path[i])
		except:
			break
		alpha = data['Theta']*np.pi/180
		amplitude = data['Amplitude']
		axes = fig.add_subplot(2, 3, m, projection='polar')
		axes.plot(alpha, amplitude, color=TEAL, marker='+', label=labels[i])
		axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
		axes.set_xlabel(r'$\alpha$')
		axes.set_ylabel(r'amplitude')
		axes.fill_between(alpha, amplitude)
		axes.legend(loc='best')
		m = m + 1
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

polar_plot_list = ['erste_resoananz_polar_2308_764.dat',
				   'zweite_resoananz_polar_3700_879.dat',
				   'dritte_resoananz_polar_4948_930.dat',
				   'vierte_resoananz_polar_6237_197.dat',
				   'fünfte_resoananz_polar_6567_745.dat']
polar_plot_labels = ['erste Resoananz 2308.764Hz',
					 'zweite Resoananz 3700.879Hz',
					 'dritte Resoananz 4948.930Hz',
					 'vierte Resoananz 6237.197Hz',
					 'fünfte Resoananz 6567.745Hz']

def test():
	# Fixing random state for reproducibility
	np.random.seed(19680801)

	# Compute areas and colors
	N = 150
	r = 2 * np.random.rand(N)
	theta = 2 * np.pi * np.random.rand(N)
	area = 200 * r ** 2
	colors = theta

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='polar')
	c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
	plt.show()


# Aufgabe 1
# show_spec('aufgabe1.dat', r'spectrum')
# show_spec(task1_2_data_list) # peak control
# peak_alpha_plot(task1_2_data_list) #TODO: correct alpha

# Aufgabe 2
# show_spec(task2_list, task2_labels)
#show_spec('alpha_0_5000.dat', r'$\alpha=0\degree$' '\nhigh reslution')

# Aufgabe 3
#show_polar_plots(polar_plot_list, polar_plot_labels) #TODO: rotate, order

# Aufgabe 4
