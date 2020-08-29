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


def show_spec_list(path, labels):
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


def show_spec_single(path, labels):
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
	alpha[0] = np.arccos(1 / 2 * (np.cos(alpha[0]) - 1)) #TODO: is wrong
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

def show_spec_with_peaks(path):
	frequence = read_data(path)[:, 0]
	amplitude = read_data(path)[:, 1]
	peak_index, _ = find_peak(amplitude, 1)

	peak_freq = [frequence[index] for index in peak_index]
	del peak_freq[0:2]
	peak_amp = [amplitude[index] for index in peak_index]
	del peak_amp[0:2]
	data_table = pd.DataFrame(peak_freq)
	data_table[0] = data_table[0] * 2 * np.pi
	data_table['k'] = data_table[0] / 340.27 #TODO: right?
	print(data_table)

	fig, axes = plt.subplots(nrows=2, ncols=1)
	axes[0].plot(frequence, amplitude, color=TEAL, marker='+', label='600mm with peaks')
	axes[0].plot(peak_freq, peak_amp, color=RED, marker='*', linestyle='None')
	axes[0].grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes[0].set_xlabel('frequence in Hz')
	axes[0].set_ylabel(r'amplitude')
	axes[0].legend(loc='best')
	axes[1].plot(data_table['k'], data_table[0], color=RED, marker='+', linestyle='None', label='Dispersionsrelation')
	axes[1].grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes[1].set_xlabel('k in 1/m')
	axes[1].set_ylabel(r'$\omega$')
	axes[1].legend(loc='best')
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

task4_1_list = ['1_4_0mm.dat',
				'1_4_3mm.dat',
				'1_4_6mm.dat',
				'1_4_9mm.dat']

task4_labels = ['0mm', '3mm', '6mm', '9mm']

task4_2_list = ['1_4_0mm_l.dat',
				'1_4_3mm_l.dat',
				'1_4_6mm_l.dat',
				'1_4_9mm_l.dat']

task5_path_list = ['2_1_300mm.dat',
				   '2_1_450mm.dat',
				   '2_1_600mm.dat']

task5_labels = ['300mm',
				'450mm',
				'600mm']

task7_path_list = ['2_3_600_16.dat',
				   '2_3_600_13.dat',
				   '2_3_600_10.dat']

task7_labels = ['Iris 16mm',
				'Iris 13mm',
				'Iris 10mm']

task9_path_list = ['2_3_600_10_75_defekt_stelle_rechts.dat',
				   '2_3_600_10_25_defekt_stelle_rechts.dat',
				   '2_3_600_10_37_5_defekt_stelle_rechts.dat',
				   '2_3_600_10_62_5_defekt_stelle_rechts.dat']

task9_labels = ['Iris 10mm Stör 75mm',
				'Iris 10mm Stör 25mm',
				'Iris 10mm Stör 37.5mm',
				'Iris 10mm Stör 62.5mm']

# Aufgabe 1
#show_spec_single('aufgabe1.dat', r'spectrum')
# show_spec_single(task1_2_data_list) # peak control
#peak_alpha_plot(task1_2_data_list) #TODO: correct alpha

# Aufgabe 2
#show_spec_list(task2_list, task2_labels)
#show_spec_single('alpha_0_5000.dat', r'$\alpha=0\degree$' '\nhigh reslution')

# Aufgabe 3
#show_polar_plots(polar_plot_list, polar_plot_labels) #TODO: rotate, order

# Aufgabe 4
#show_spec_list(task4_1_list, task4_labels)
#show_spec_list(task4_2_list, task4_labels)

# Aufgabe 5
#show_spec_list(task5_path_list, task5_labels)

# Aufgabe 6
#show_spec_with_peaks('2_2_600.dat')

# Aufgabe 7
#show_spec_list(task7_path_list, task7_labels)

# Aufgabe 8 #TODO: right?
#show_spec_with_peaks('2_3_600_16.dat')
#show_spec_with_peaks('2_3_600_13.dat')
#show_spec_with_peaks('2_3_600_10.dat')

# Aufgabe 9
#show_spec_list(task9_path_list, task9_labels)
