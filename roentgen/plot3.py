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

	fig, axes = plt.subplots()
	for j in range(0, 8):
		axes.plot(theta[j], n[j], color=color_spec[j], label=energy_duane[j] + ' keV')
	# axes.plot(theta30, n30, color='TEAL', label=r'$SF_6$')
	# axes.plot(peak_u, peak_i, color='RED', linestyle='None', marker='+')
	axes.grid(True, color='black', linestyle='dashed', alpha=0.2)
	axes.set_xlabel(r'$\theta$ in °')
	axes.set_ylabel(r'Impulse')
	axes.legend(loc='best')
	plt.show()


show_all()
