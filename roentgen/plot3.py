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

color_spec = [BLUE, CYAN, TEAL, ORANGE, RED, MAGENTA, GREY, 'black']
energy_duane = [str(9 + 3 * i) for i in range(8)]
d_lif = 0.4028e-09


# test
def read_data(path):
	data = pd.read_csv(path, sep='\t', decimal='.', header=None)
	return data

def read_data_theo(path):
	data = pd.read_csv(path, sep='\s+', decimal='.', header=None)
	return data

def read_data_comma(path):
	data = pd.read_csv(path, sep='\t', decimal=',', header=None)
	return data


def theta_to_lambda(thetas, gitter_distance):
	if isinstance(thetas, list):
		radians = []
		lambdas = []
		for theta in thetas:
			radians.append(theta * np.pi / 180)
		for radian in radians:
			lambdas.append(2 * gitter_distance * np.sin(radian))
		return lambdas
	else:
		return 2 * gitter_distance * np.sin(thetas * np.pi / 180)

def show_alu():
	theta_exp = read_data_comma('resources/al_34_10_02_6_.txt')[0]
	imp_exp = read_data_comma('resources/al_34_10_02_6_.txt')[1]
	theta_theo = np.array(read_data_theo('resources/Al_PowderPattern_64700.txt')[0])/2
	imp_theo = np.array(read_data_theo('resources/Al_PowderPattern_64700.txt')[1])/5000 * 175
	fig, axes = plt.subplots()
	axes.plot(theta_theo, imp_theo, color=ORANGE, label='Al normierte Theorie')
	axes.plot(theta_exp, imp_exp, color=TEAL, label='Al Exp')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.legend(loc='best')
	axes.set_xlabel(r'$\theta$ in °')
	axes.set_ylabel('Impulse')
	plt.show()



def show_all():
	theta = []
	n = []
	for i in range(9, 33, 3):
		theta.append(read_data('resources/lif_' + str(i) + '_10_01_4_.txt')[0])
		n.append(read_data('resources/lif_' + str(i) + '_10_01_4_.txt')[1])

	fig, axes = plt.subplots(ncols=4, nrows=2)
	for j in range(0, 8):
		axes[j % 2][int(j / 2)].plot(theta[j], n[j], color=color_spec[j], label=energy_duane[j] + ' keV')
		# axes.plot(theta30, n30, color='TEAL', label=r'$SF_6$')
		# axes.plot(peak_u, peak_i, color='RED', linestyle='None', marker='+')
		axes[j % 2][int(j / 2)].grid(True, color='black', linestyle='dashed', alpha=0.2)
		axes[j % 2][int(j / 2)].set_xlabel(r'$\theta$ in °')
		axes[j % 2][int(j / 2)].set_ylabel(r'Impulse')
		axes[j % 2][int(j / 2)].legend(loc='best')
	plt.show()


def model_func(u, a, b):
	return a * u + b


def show_cd():
	theta1 = read_data_comma('resources/cd_34_10_02_6_1.txt')[0]
	n1 = read_data_comma('resources/cd_34_10_02_6_1.txt')[1]
	theta2 = read_data_comma('resources/cd_34_10_02_6_2.txt')[0]
	n2 = read_data_comma('resources/cd_34_10_02_6_2.txt')[1]
	theta3 = read_data_comma('resources/cd_34_10_02_10_3ni.txt')[0]
	n3 = read_data_comma('resources/cd_34_10_02_10_3ni.txt')[1]
	theta_theo = read_data('resources/Cd_PowderPattern_98179.txt')[0]
	n_theo = read_data('resources/Cd_PowderPattern_98179.txt')[1]

	n_theo = n_theo / max(n_theo) * max(n1)

	fig, axes = plt.subplots()
	axes.plot(theta1, n1, color='red', label='Cd')
	axes.plot(theta2, n2, color='red')
	axes.plot(theta3, n3, color='grey', label='Cd mit Ni')
	axes.plot(theta_theo, n_theo, color='orange', label='Cd Theo')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$\theta$ in °')
	axes.set_ylabel(r'Streuintensität')
	axes.legend(loc='best')
	plt.show()




def duane_hant():
	energys = [9, 12, 15, 18, 21, 24, 27, 30]
	thetas = [20.3, 14.9, 11.8, 9.7, 8.4, 7.1, 6.3, 5.7]
	lambdas = theta_to_lambda(thetas, gitter_distance=d_lif / 2)
	popt, pcov = curve_fit(model_func, xdata=1 / np.array(energys), ydata=lambdas)
	standard_deviation = np.sqrt(np.diag(pcov))
	x_data = np.linspace(start=1 / energys[-1], stop=1 / energys[0], num=200)
	fig, axes = plt.subplots()
	print(popt)
	axes.set_ylabel(r'$\frac{a}{b} \times \lambda_{min}$', fontsize=14)
	axes.set_xlabel(r'$\frac{1}{E}$ in $\frac{1}{keV}$', fontsize=14)
	axes.plot(x_data, model_func(x_data, *popt), linestyle='dashed', color=TEAL,
			  label='fit: a=%5.3e, b=%5.3e' % tuple(popt))
	axes.plot(1 / np.array(energys), lambdas, linestyle='none', marker='o', color=RED)
	axes.legend(loc='best')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	plt.show()


# duane_hant()

def show_task_one():
	theta = read_data_comma('resources/lif_34_10_02_5_.txt')[0]
	n = read_data_comma('resources/lif_34_10_02_5_.txt')[1]
	lam = theta_to_lambda(theta, 0.2014)
	fig, axes = plt.subplots()
	axes.plot(lam, n, color='red', label='CU-Spektrum')
	axes.bar(theta_to_lambda(22.5, 0.2014), 8435, color='blue',
			 label=r'$K_\alpha$ = ' + str(theta_to_lambda(22.5, 0.2014)), width=0.0005)
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$\lambda$ in nm')
	axes.set_ylabel(r'Impulse')
	axes.legend(loc='best')
	plt.show()


def n_1_task_two(lam):
	n = 158 * lam ** 3 - 40.1 * lam ** 4
	return n


def n_2_task_two(lam):
	n = 13.4 * lam ** 3 - 0.651 * lam ** 4
	return n


def show_task_two():
	theta_no_c = read_data_comma('resources/lif_34_05_01_8_.txt')[0]
	n_no_c = read_data_comma('resources/lif_34_05_01_8_.txt')[1]
	theta_c = read_data_comma('resources/lif_34_05_01_8_cu25.txt')[0]
	n_c = read_data_comma('resources/lif_34_05_01_8_cu25.txt')[1]

	n_dev = np.log(n_no_c / n_c)
	lam_theo1 = np.linspace(theta_to_lambda(18, 0.2014), 0.138043, 100)
	lam_theo2 = np.linspace(0.138043, theta_to_lambda(24.5, 0.2014), 100)

	n_theo1 = n_1_task_two(lam_theo1)
	n_theo2 = n_2_task_two(lam_theo2)

	lam_no_c = theta_to_lambda(theta_no_c, 0.2014)
	lam_c = theta_to_lambda(theta_c, 0.2014)

	fig, axes = plt.subplots(nrows=2)
	axes[0].plot(lam_c, n_c, color='red', label='CU-Filter')
	axes[0].plot(lam_no_c, n_no_c, color='blue', label='no CU-Filter')
	axes[0].grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes[0].set_xlabel(r'$\lambda$ in nm')
	axes[0].set_ylabel(r'Impulse')
	axes[0].legend(loc='best')
	axes[1].plot(lam_c, n_dev, color='red', label=r'$\log{\frac{I}{I_c}}$')
	axes[1].bar(0.138043, 2, color='blue',
				label=r'$K_{\alpha C}$ = ' + str(0.138043) + 'nm', width=0.00025)
	# axes_copy = axes[1].twinx()
	# axes_copy.plot(lam_theo1, n_theo1, color='blue', label=r'theo')
	# axes_copy.plot(lam_theo2, n_theo2, color='blue')
	axes[1].grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes[1].set_xlabel(r'$\lambda$ in nm')
	axes[1].set_ylabel(r'absorptions coefficient')
	axes[1].legend(loc='best')
	plt.show()


# show_all()
# show_task_two()
show_cd()
show_alu()
