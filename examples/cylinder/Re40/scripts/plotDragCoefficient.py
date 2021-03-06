"""
Plots the instantaneous drag coefficient between 0 and 20 time-units of flow
simulation and compares with numerical results from
Koumoutsakos and Leonard (1995).

_References:_
* Koumoutsakos, P., & Leonard, A. (1995).
  High-resolution simulations of the flow around an impulsively started
  cylinder using vortex methods.
  Journal of Fluid Mechanics, 296, 1-38.
"""

import os
import argparse

from matplotlib import pyplot

from snake.cuibm.simulation import CuIBMSimulation
from snake.solutions.koumoutsakosLeonard1995 import KoumoutsakosLeonard1995


# Parse from the command-line the directory of the runs.
parser = argparse.ArgumentParser()
parser.add_argument('--directory',
                    dest='directory',
                    default=os.getcwd(),
                    type=str,
                    help='directory of the runs')
args = parser.parse_args()
directory = args.directory

simulation = CuIBMSimulation(directory=directory,
                             description='cuIBM')
simulation.read_forces()

# Reads drag coefficient of Koumoutsakos and Leonard (1995) for Re=40.
file_name = 'koumoutsakos_leonard_1995_cylinder_dragCoefficientRe40.dat'
file_path = os.path.join(os.environ['CUIBM_DIR'], 'data', file_name)
kl1995 = KoumoutsakosLeonard1995(file_path=file_path, Re=40)

# Plots the instantaneous drag coefficients.
images_directory = os.path.join(directory, 'images')
if not os.path.isdir(images_directory):
  os.makedirs(images_directory)
pyplot.style.use('seaborn-dark')
kwargs_data = {'label': simulation.description,
               'color': '#336699',
               'linestyle': '-',
               'linewidth': 3,
               'zorder': 10}
kwargs_kl1995 = {'label': kl1995.description,
                 'color': '#993333',
                 'linewidth': 0,
                 'markeredgewidth': 2,
                 'markeredgecolor': '#993333',
                 'markerfacecolor': 'none',
                 'marker': 'o',
                 'markersize': 4,
                 'zorder': 10}
fig, ax = pyplot.subplots(figsize=(6, 6))
ax.grid(True, zorder=0)
ax.set_xlabel('non-dimensional time', fontsize=16)
ax.set_ylabel('drag coefficient', fontsize=16)
ax.plot(simulation.forces[0].times, 2.0 * simulation.forces[0].values,
        **kwargs_data)
ax.plot(kl1995.cd.times, kl1995.cd.values,
        **kwargs_kl1995)
ax.axis([0.0, 20.0, 0.0, 5.0])
ax.legend(prop={'size': 16})
pyplot.savefig(os.path.join(images_directory, 'dragCoefficient.png'))
