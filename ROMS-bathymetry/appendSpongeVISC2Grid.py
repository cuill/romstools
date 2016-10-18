import os
from numpy import *
from matplotlib.pyplot import *
from netCDF4 import Dataset
from pylab import *
from mpl_util import LevelColormap
import pyroms
import pyroms_toolbox
from mpl_toolkits.basemap import Basemap, shiftgrid
import mpl_toolkits.basemap as mp
from bathy_smoother import *
import mpl_util
import laplace_filter
from bathy_smoother import *

__author__   = 'Trond Kristiansen'
__email__    = 'trond.kristiansen@imr.no'
__created__  = datetime.datetime(2015, 7, 30)
__modified__ = datetime.datetime(2015, 7, 30)
__version__  = "1.0"
__status__   = "Development, 30.7.2015"



"""Get the grid file defined in /Users/trondkr/Projects/KINO/map/gridid.txt"""
grd = pyroms.grid.get_ROMS_grid('KINO1600M')

"""Append sponge visc2 application data to grid"""
nc = netCDF.Dataset(filename, 'a', format='NETCDF4')

nc.createDimension('xi_rho', np.size(grd.hgrid.mask_rho,1))
