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
energy_duane = [str(9 + 3*i) for i in range(8)]
d_lif = 0.4028e-09

#test
def read_data(path):
	data = pd.read_csv(path, sep='\t', decimal='.', header=None)
	return data


def theta_to_lambda(thetas, gitter_distance):
	if isinstance(thetas, list):
		radians = []
		lambdas = []
		for theta in thetas:
			radians.append(theta * np.pi/180)
		for radian in radians:
			lambdas.append(2*gitter_distance*np.sin(radian))
		return lambdas
	else:
		return 2*gitter_distance*np.sin(thetas*np.pi/180)

def show_all():
	theta = []
	n = []
	for i in range(9, 33, 3):
		theta.append(read_data('resources/lif_'+str(i)+'_10_01_4_.txt')[0])
		n.append(read_data('resources/lif_'+str(i)+'_10_01_4_.txt')[1])

	fig, axes = plt.subplots(ncols=4, nrows=2)
	for j in range(0, 8):
		axes[j%2][int(j/2)].plot(theta[j], n[j], color=color_spec[j], label=energy_duane[j] + ' keV')
	# axes.plot(theta30, n30, color='TEAL', label=r'$SF_6$')
	# axes.plot(peak_u, peak_i, color='RED', linestyle='None', marker='+')
		axes[j % 2][int(j/2)].grid(True, color='black', linestyle='dashed', alpha=0.2)
		axes[j%2][int(j/2)].set_xlabel(r'$\theta$ in °')
		axes[j%2][int(j/2)].set_ylabel(r'Impulse')
		axes[j%2][int(j/2)].legend(loc='best')
	plt.show()

def model_func(u, a, b):
	return a*u + b


def duane_hant():
	energys = [9, 12, 15, 18, 21, 24, 27, 30]
	thetas = [20.3, 14.9, 11.8, 9.7, 8.4, 7.1, 6.3, 5.7]
	lambdas = theta_to_lambda(thetas, gitter_distance=d_lif/2)
	popt, pcov = curve_fit(model_func, xdata=1/np.array(energys), ydata=lambdas)
	standard_deviation = np.sqrt(np.diag(pcov))
	x_data = np.linspace(start=1/energys[-1], stop=1/energys[0], num=200)
	fig, axes = plt.subplots()
	print(popt)
	axes.set_ylabel(r'$\frac{a}{b} \times \lambda_{min}$', fontsize=14)
	axes.set_xlabel(r'$\frac{1}{E}$ in $\frac{1}{keV}$', fontsize=14)
	axes.plot(x_data, model_func(x_data, *popt), linestyle='dashed', color=TEAL, label='fit: a=%5.3e, b=%5.3e' % tuple(popt))
	axes.plot(1/np.array(energys), lambdas, linestyle='none', marker='o', color=RED)
	axes.legend(loc='best')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	plt.show()

duane_hant()
