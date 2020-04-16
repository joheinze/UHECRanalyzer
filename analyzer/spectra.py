import astropy.units as u
import numpy as np

import os.path as path
datadir = path.join(path.dirname(path.dirname(path.abspath(__file__))),'data')

# ------------------------------------------------------------------
# The Auger spectrum from ICRC 2013
# ------------------------------------------------------------------
auger2013 = np.array([
    [0  , 17.55 , 7.32870e+37 , 7.55145e+35 , 7.62995e+35],
    [1  , 17.65 , 7.02267e+37 , 8.99818e+35 , 9.11465e+35],
    [2  , 17.75 , 6.55519e+37 , 1.07012e+36 , 1.08780e+36],
    [3  , 17.85 , 6.27534e+37 , 1.31974e+36 , 1.34790e+36],
    [4  , 17.95 , 5.78717e+37 , 1.59983e+36 , 1.64484e+36],
    [5  , 18.05 , 5.08546e+37 , 8.92247e+35 , 9.01008e+35],
    [6  , 18.15 , 5.49497e+37 , 1.07240e+36 , 1.08084e+36],
    [7  , 18.25 , 4.87529e+37 , 1.08639e+36 , 1.10004e+36],
    [8  , 18.35 , 4.44016e+37 , 1.18476e+36 , 1.19708e+36],
    [9  , 18.45 , 4.37830e+37 , 2.04192e+35 , 2.05213e+35],
    [10 , 18.55 , 4.15646e+37 , 2.41129e+35 , 2.42517e+35],
    [11 , 18.65 , 3.94101e+37 , 2.69047e+35 , 2.71504e+35],
    [12 , 18.75 , 3.95467e+37 , 3.45685e+35 , 3.49789e+35],
    [13 , 18.85 , 4.28428e+37 , 4.59651e+35 , 4.66286e+35],
    [14 , 18.95 , 4.61634e+37 , 6.03035e+35 , 6.13570e+35],
    [15 , 19.05 , 5.07253e+37 , 7.98360e+35 , 8.15093e+35],
    [16 , 19.15 , 5.40973e+37 , 1.03955e+36 , 1.06670e+36],
    [17 , 19.25 , 5.52241e+37 , 1.32572e+36 , 1.36784e+36],
    [18 , 19.35 , 5.71612e+37 , 1.69746e+36 , 1.76420e+36],
    [19 , 19.45 , 5.44773e+37 , 2.08267e+36 , 2.19232e+36],
    [20 , 19.55 , 5.62200e+37 , 2.70965e+36 , 2.89345e+36],
    [21 , 19.65 , 3.87293e+37 , 2.78737e+36 , 3.08201e+36],
    [22 , 19.75 , 2.82613e+37 , 3.09966e+36 , 3.34086e+36],
    [23 , 19.85 , 2.34187e+37 , 3.49305e+36 , 4.16117e+36],
    [24 , 19.95 , 7.45881e+36 , 4.61495e+36 , 3.37345e+36],
    [25 , 20.05 , 4.68462e+36 , 2.54073e+36 , 4.53435e+36],
    [26 , 20.15 , 2.45633e+36 , 2.02806e+36 , 5.62138e+36],
]).T

auger2013 = {'energy':    (10**auger2013[1] * u.eV).to_value(u.GeV),
             'spectrum':  (auger2013[2] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'lower_err': (auger2013[3] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'upper_err': (auger2013[4] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
            }

# ------------------------------------------------------------------
# The Auger spectrum from ICRC 2015
# ------------------------------------------------------------------
# original data
auger2015 = np.array([
    [0  ,  17.55 , 7.77261e+37 , 4.95702e+35 , 4.95702e+35],
    [1  ,  17.65 , 7.35354e+37 , 6.10281e+35 , 6.10281e+35],
    [2  ,  17.75 , 6.91306e+37 , 7.48084e+35 , 7.48084e+35],
    [3  ,  17.85 , 6.52020e+37 , 9.18827e+35 , 9.18827e+35],
    [4  ,  17.95 , 5.93006e+37 , 1.10845e+36 , 1.10845e+36],
    [5  ,  18.05 , 5.23461e+37 , 1.14606e+36 , 1.14606e+36],
    [6  ,  18.15 , 5.17890e+37 , 1.24445e+36 , 1.24445e+36],
    [7  ,  18.25 , 5.02043e+37 , 1.35472e+36 , 1.35472e+36],
    [8  ,  18.35 , 4.30996e+37 , 1.33088e+36 , 1.33088e+36],
    [9  ,  18.45 , 4.25363e+37 , 1.73898e+35 , 1.73898e+35],
    [10 ,  18.55 , 4.00527e+37 , 2.14540e+35 , 2.14540e+35],
    [11 ,  18.65 , 3.85275e+37 , 2.38204e+35 , 2.38204e+35],
    [12 ,  18.75 , 3.87490e+37 , 3.03816e+35 , 3.03816e+35],
    [13 ,  18.85 , 4.30996e+37 , 4.10472e+35 , 4.10472e+35],
    [14 ,  18.95 , 4.72903e+37 , 5.45465e+35 , 5.45465e+35],
    [15 ,  19.05 , 5.19496e+37 , 7.21742e+35 , 7.21742e+35],
    [16 ,  19.15 , 5.54344e+37 , 9.36476e+35 , 9.36476e+35],
    [17 ,  19.25 , 5.64799e+37 , 1.19534e+36 , 1.19534e+36],
    [18 ,  19.35 , 5.62031e+37 , 1.50138e+36 , 1.50138e+36],
    [19 ,  19.45 , 5.62980e+37 , 1.88911e+36 , 1.88911e+36],
    [20 ,  19.55 , 5.71049e+37 , 2.40316e+36 , 2.40316e+36],
    [21 ,  19.65 , 4.16701e+37 , 2.58945e+36 , 2.58945e+36],
    [22 ,  19.75 , 3.10789e+37 , 2.70944e+36 , 2.70944e+36],
    [23 ,  19.85 , 1.98921e+37 , 3.04697e+36 , 3.04697e+36],
    [24 ,  19.95 , 5.75491e+36 , 1.81655e+36 , 1.81655e+36],
    [25 ,  20.05 , 5.07599e+36 , 3.32715e+36 , 1.98677e+36],
    [26 ,  20.15 , 1.99237e+36 , 3.31224e+36 , 1.18788e+36],
]).T

auger2015 = {'energy':    (10**auger2015[1] * u.eV).to_value(u.GeV),
             'spectrum':  (auger2015[2] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'upper_err': (auger2015[3] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'lower_err': (auger2015[4] * u.eV**2 * u.km**-2 * u.sr**-1 * u.yr**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
            }

# ------------------------------------------------------------------
# The Auger xmax distr. from ICRC 2015
# ------------------------------------------------------------------
Xmax2015 = np.array([
    [ 0, 17.80, 17.90, 17.850, 3768, 709.9, 1.2, 7.6, -10.2, 59.6,  1.7, 1.9, -1.7],
    [ 1, 17.90, 18.00, 17.949, 3383, 719.9, 1.4, 7.5, -10.2, 62.4,  2.1, 2.1, -1.8],
    [ 2, 18.00, 18.10, 18.048, 2818, 725.2, 1.5, 7.4, -10.2, 59.5,  2.0, 2.2, -1.9],
    [ 3, 18.10, 18.20, 18.148, 2425, 736.9, 1.8, 7.3, -10.1, 64.3,  2.6, 2.4, -2.1],
    [ 4, 18.20, 18.30, 18.247, 1952, 744.5, 2.0, 7.3,  -9.9, 66.4,  2.6, 2.6, -2.2],
    [ 5, 18.30, 18.40, 18.348, 1439, 748.0, 2.0, 7.3,  -9.7, 60.2,  2.8, 2.3, -2.0],
    [ 6, 18.40, 18.50, 18.447, 1139, 752.2, 2.1, 7.3,  -9.4, 53.3,  2.9, 2.1, -1.8],
    [ 7, 18.50, 18.60, 18.548,  814, 754.5, 2.2, 7.3,  -9.1, 53.5,  3.0, 1.9, -1.7],
    [ 8, 18.60, 18.70, 18.646,  575, 756.1, 2.7, 7.4,  -8.8, 54.5,  3.5, 1.7, -1.6],
    [ 9, 18.70, 18.80, 18.747,  413, 757.4, 2.8, 7.5,  -8.5, 45.8,  3.4, 1.5, -1.5],
    [10, 18.80, 18.90, 18.849,  297, 763.6, 2.9, 7.7,  -8.1, 42.8,  3.6, 1.4, -1.4],
    [11, 18.90, 19.00, 18.947,  230, 764.6, 3.2, 7.8,  -7.8, 43.4,  4.1, 1.3, -1.4],
    [12, 19.00, 19.10, 19.048,  165, 766.4, 3.3, 8.0,  -7.6, 39.0,  3.8, 1.3, -1.4],
    [13, 19.10, 19.20, 19.144,  114, 767.0, 3.6, 8.2,  -7.4, 36.7,  3.6, 1.3, -1.4],
    [14, 19.20, 19.30, 19.247,   87, 779.5, 5.1, 8.5,  -7.2, 46.4,  6.2, 1.2, -1.3],
    [15, 19.30, 19.40, 19.340,   63, 773.1, 5.0, 8.7,  -7.1, 40.1,  4.8, 1.3, -1.4],
    [16, 19.40, 19.50, 19.447,   40, 787.9, 9.6, 8.9,  -7.0, 53.2, 12.7, 1.3, -1.4],
    [17, 19.50, 20.00, 19.620,   37, 779.8, 5.0, 9.4,  -6.9, 26.5,  4.8, 1.5, -1.6],
]).T

XRMS2015 = {'energy':      (10**Xmax2015[3] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2015[3] * u.eV).to_value(u.GeV) - (10**Xmax2015[1] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax2015[2] * u.eV).to_value(u.GeV) - (10**Xmax2015[3] * u.eV).to_value(u.GeV),
            'val':        (Xmax2015[9] * u.g * u.cm**-2).value,
            'stat':    (Xmax2015[10] * u.g * u.cm**-2).value,
            'sys_Up':  (Xmax2015[11] * u.g * u.cm**-2).value,
            'sys_Low': -1*(Xmax2015[12] * u.g * u.cm**-2).value,
           }

Xmax2015 = {'energy':      (10**Xmax2015[3] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2015[3] * u.eV).to_value(u.GeV) - (10**Xmax2015[1] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax2015[2] * u.eV).to_value(u.GeV) - (10**Xmax2015[3] * u.eV).to_value(u.GeV),
            'val':         (Xmax2015[5] * u.g * u.cm**-2).value,
            'stat':        (Xmax2015[6] * u.g * u.cm**-2).value,
            'sys_Up':      (Xmax2015[7] * u.g * u.cm**-2).value,
            'sys_Low': -1* (Xmax2015[8] * u.g * u.cm**-2).value,
           }

# ------------------------------------------------------------------
# The Auger combined spectrum and xmax distr. from ICRC 2017
# downloaded from https://www.auger.org/index.php/science/data
# ------------------------------------------------------------------
auger2017 = np.loadtxt(path.join(datadir,'Combined Spectrum data 2017.txt')).T
auger2017 = {'energy': (10**auger2017[0] * u.eV).to_value(u.GeV),
             'spectrum':  (10**(2*auger2017[0]) * u.eV**2 * auger2017[1] * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'upper_err': (10**(2*auger2017[0]) * u.eV**2 * auger2017[2] * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'lower_err': (10**(2*auger2017[0]) * u.eV**2 * auger2017[3] * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
            }
Xmax2017 = np.loadtxt(path.join(datadir,'Xmax Moments ICRC 2017.txt')).T

# The Xmax bins are not contained in the file, I add them manually here
Xmax_bins=np.array([
        [17.20, 17.30],
        [17.30, 17.40],
        [17.40, 17.50],
        [17.50, 17.60],
        [17.60, 17.70],
        [17.70, 17.80],
        [17.80, 17.90],
        [17.90, 18.00],
        [18.00, 18.10],
        [18.10, 18.20],
        [18.20, 18.30],
        [18.30, 18.40],
        [18.40, 18.50],
        [18.50, 18.60],
        [18.60, 18.70],
        [18.70, 18.80],
        [18.80, 18.90],
        [18.90, 19.00],
        [19.00, 19.10],
        [19.10, 19.20],
        [19.20, 19.30],
        [19.30, 19.40],
        [19.40, 19.50],
        [19.50, 20.00],]).T

XRMS2017 = {'energy':      (10**Xmax2017[0] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2017[0] * u.eV).to_value(u.GeV) - (10**Xmax_bins[0] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax_bins[1] * u.eV).to_value(u.GeV) - (10**Xmax2017[0] * u.eV).to_value(u.GeV),
            'val':        (Xmax2017[6] * u.g * u.cm**-2).value,
            'stat':    (Xmax2017[7] * u.g * u.cm**-2).value,
            'sys_Up':  (Xmax2017[8] * u.g * u.cm**-2).value,
            'sys_Low': (Xmax2017[9] * u.g * u.cm**-2).value,
           }

Xmax2017 = {'energy':      (10**Xmax2017[0] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2017[0] * u.eV).to_value(u.GeV) - (10**Xmax_bins[0] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax_bins[1] * u.eV).to_value(u.GeV) - (10**Xmax2017[0] * u.eV).to_value(u.GeV),
            'val':         (Xmax2017[2] * u.g * u.cm**-2).value,
            'stat':        (Xmax2017[3] * u.g * u.cm**-2).value,
            'sys_Up':      (Xmax2017[4] * u.g * u.cm**-2).value,
            'sys_Low':     (Xmax2017[5] * u.g * u.cm**-2).value,
           }

# ------------------------------------------------------------------
# Auger spectrum from ICRC2019 (still inofficial)
# ------------------------------------------------------------------
import astropy.units as u

auger2019 = np.loadtxt(path.join(datadir,'Combined Spectrum data 2019.txt')).T
auger2019 = {'energy': (10**auger2019[0] * u.eV).to_value(u.GeV),
             'spectrum':  (10**(3*auger2019[0]) * u.eV**3 * auger2019[1] * u.km**-2 * u.sr**-1 * u.yr**-1 * u.eV**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'upper_err': (10**(3*auger2019[0]) * u.eV**3 * (auger2019[2]-auger2019[1]) * u.km**-2 * u.sr**-1 * u.yr**-1 * u.eV**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
             'lower_err': (10**(3*auger2019[0]) * u.eV**3 * (auger2019[1]-auger2019[3]) * u.km**-2 * u.sr**-1 * u.yr**-1 * u.eV**-1).to_value(u.GeV**2 * u.cm**-2 * u.sr**-1 * u.s**-1),
            }

Xmax2019 = np.loadtxt(path.join(datadir,'AugerICRC2019_Xmax_Moments.txt')).T

# The Xmax bins are not contained in the file, I add them manually here
Xmax_bins=np.array([
        [17.20, 17.30],
        [17.30, 17.40],
        [17.40, 17.50],
        [17.50, 17.60],
        [17.60, 17.70],
        [17.70, 17.80],
        [17.80, 17.90],
        [17.90, 18.00],
        [18.00, 18.10],
        [18.10, 18.20],
        [18.20, 18.30],
        [18.30, 18.40],
        [18.40, 18.50],
        [18.50, 18.60],
        [18.60, 18.70],
        [18.70, 18.80],
        [18.80, 18.90],
        [18.90, 19.00],
        [19.00, 19.10],
        [19.10, 19.20],
        [19.20, 19.30],
        [19.30, 19.40],
        [19.40, 19.50],
        [19.50, 19.60],
        [19.60, 20.00],]).T

XRMS2019 = {'energy':      (10**Xmax2019[0] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2019[0] * u.eV).to_value(u.GeV) - (10**Xmax_bins[0] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax_bins[1] * u.eV).to_value(u.GeV) - (10**Xmax2019[0] * u.eV).to_value(u.GeV),
            'val':        (Xmax2019[6] * u.g * u.cm**-2).value,
            'stat':    (Xmax2019[7] * u.g * u.cm**-2).value,
            'sys_Up':  (Xmax2019[8] * u.g * u.cm**-2).value,
            'sys_Low': (Xmax2019[9] * u.g * u.cm**-2).value,
           }

Xmax2019 = {'energy':      (10**Xmax2019[0] * u.eV).to_value(u.GeV),
            'energy_Low':  (10**Xmax2019[0] * u.eV).to_value(u.GeV) - (10**Xmax_bins[0] * u.eV).to_value(u.GeV),
            'energy_Up':   (10**Xmax_bins[1] * u.eV).to_value(u.GeV) - (10**Xmax2019[0] * u.eV).to_value(u.GeV),
            'val':         (Xmax2019[2] * u.g * u.cm**-2).value,
            'stat':        (Xmax2019[3] * u.g * u.cm**-2).value,
            'sys_Up':      (Xmax2019[4] * u.g * u.cm**-2).value,
            'sys_Low':     (Xmax2019[5] * u.g * u.cm**-2).value,
           }

# ------------------------------------------------------------------
# TA spectrum from ICRC 2015 (combined spectrum)
# ------------------------------------------------------------------
import astropy.units as u
# original data
TA2015 = np.array([
    [15.65, 3.706e-23, 5.360e-25, 5.360e-25],
    [15.75, 1.893e-23, 2.535e-25, 2.535e-25],
    [15.85, 8.945e-24, 1.233e-25, 1.233e-25],
    [15.95, 4.393e-24, 6.369e-26, 6.369e-26],
    [16.05, 2.142e-24, 3.368e-26, 3.368e-26],
    [16.15, 1.041e-24, 1.813e-26, 1.813e-26],
    [16.25, 4.925e-25, 9.766e-27, 9.766e-27],
    [16.35, 2.468e-25, 5.478e-27, 5.478e-27],
    [16.45, 1.234e-25, 3.100e-27, 3.100e-27],
    [16.55, 6.363e-26, 1.333e-27, 1.333e-27],
    [16.65, 3.259e-26, 7.823e-28, 7.823e-28],
    [16.75, 1.549e-26, 4.440e-28, 4.440e-28],
    [16.85, 8.292e-27, 2.675e-28, 2.675e-28],
    [16.95, 4.138e-27, 1.576e-28, 1.576e-28],
    [17.05, 2.088e-27, 9.542e-29, 9.542e-29],
    [17.15, 1.102e-27, 5.787e-29, 5.787e-29],
    [17.25, 5.804e-28, 3.067e-29, 3.067e-29],
    [17.35, 2.594e-28, 1.378e-29, 1.378e-29],
    [17.45, 1.300e-28, 5.746e-30, 5.746e-30],
    [17.55, 6.221e-29, 2.262e-30, 2.262e-30],
    [17.65, 3.045e-29, 8.793e-31, 8.793e-31],
    [17.75, 1.394e-29, 3.528e-31, 3.528e-31],
    [17.85, 6.718e-30, 1.559e-31, 1.559e-31],
    [17.95, 3.178e-30, 7.435e-32, 7.435e-32],
    [18.05, 1.538e-30, 4.466e-32, 4.466e-32],
    [18.15, 6.909e-31, 2.501e-32, 2.501e-32],
    [18.25, 3.502e-31, 6.350e-33, 6.350e-33],
    [18.35, 1.630e-31, 2.691e-33, 2.691e-33],
    [18.45, 7.642e-32, 1.266e-33, 1.258e-33],
    [18.55, 3.569e-32, 6.481e-34, 6.481e-34],
    [18.65, 1.737e-32, 3.492e-34, 3.408e-34],
    [18.75, 8.397e-33, 1.976e-34, 1.976e-34],
    [18.85, 4.675e-33, 1.217e-34, 1.217e-34],
    [18.95, 2.520e-33, 7.633e-35, 7.633e-35],
    [19.05, 1.410e-33, 5.247e-35, 5.247e-35],
    [19.15, 7.511e-34, 3.429e-35, 3.429e-35],
    [19.25, 4.110e-34, 2.157e-35, 2.149e-35],
    [19.35, 2.196e-34, 1.383e-35, 1.392e-35],
    [19.45, 1.104e-34, 8.727e-36, 8.809e-36],
    [19.55, 5.769e-35, 5.624e-36, 5.624e-36],
    [19.65, 2.689e-35, 3.514e-36, 3.514e-36],
    [19.75, 1.874e-35, 2.651e-36, 2.642e-36],
    [19.85, 8.086e-36, 1.445e-36, 1.445e-36],
    [19.95, 1.515e-36, 5.128e-37, 7.453e-37],
    [20.05, 1.627e-36, 5.202e-37, 6.256e-37],
    [20.15, 1.615e-37, 9.838e-38, 2.719e-37],
    [20.25, 2.490e-37, 1.550e-37, 2.763e-37],
    [20.35, 0.000e+00, 0.000e+00, 1.262e-37],
]).T
    
TA2015 = {'energy':    (10**TA2015[0] * u.eV).to_value(u.GeV),
          'spectrum':  (TA2015[1] * u.eV**-1 * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**-1 * u.cm**-2 * u.sr**-1 * u.s**-1),
          'lower_err': (TA2015[2] * u.eV**-1 * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**-1 * u.cm**-2 * u.sr**-1 * u.s**-1),
          'upper_err': (TA2015[3] * u.eV**-1 * u.m**-2 * u.sr**-1 * u.s**-1).to_value(u.GeV**-1 * u.cm**-2 * u.sr**-1 * u.s**-1),
         }

TA2015['spectrum']  = TA2015['spectrum'] * TA2015['energy']**3
TA2015['lower_err'] = TA2015['lower_err'] * TA2015['energy']**3
TA2015['upper_err'] = TA2015['upper_err'] * TA2015['energy']**3

# ------------------------------------------------------------------
# IceCube cosmogenic neutrino limits TeVPA 2016 and ICRC 2017 
# ------------------------------------------------------------------

# IClimit2016 = np.loadtxt('../data/icecube_sensitivity.csv',delimiter=',').T

# IClimit2016 = {'energy': IClimit2016[0] * u.GeV,
#                'limit':  IClimit2016[1] * u.GeV**-1 * u.cm**-2 * u.s**-1 * u.sr**-1,
#               }
# IClimit2016['limit'] = IClimit2016['limit'] * IClimit2016['energy']**1

# IClimit2016 = convert_to_namedtuple(IClimit2016, name='IClimit2016')

IClimit2017 = np.loadtxt(path.join(datadir,'icecubelimit2017.csv'),delimiter=',').T

IClimit2017 = {'energy': IClimit2017[0] * u.GeV,
               'limit':  IClimit2017[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
              }

IClimit2017GRB = np.loadtxt(path.join(datadir,'icecubelimit2017GRB.csv'),delimiter=',').T

IClimit2017GRB = {'energy': IClimit2017GRB[0] * u.GeV,
                  'limit':  IClimit2017GRB[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
                 }

IClimit9year = np.array([
    [5.0205e+6, 1.1406e-8],
    [7.9640e+6, 1.2646e-8],
    [1.9757e+7, 1.8582e-8],
    [5.0069e+7, 2.1385e-8],
    [1.2692e+8, 2.0683e-8],
    [3.1512e+8, 1.7787e-8],
    [7.8755e+8, 1.9808e-8],
    [1.9811e+9, 3.0650e-8],
    [5.0192e+9, 4.2568e-8],
    [1.2891e+10, 7.4426e-8],
    [3.1532e+10, 1.1846e-7],
    [7.7088e+10, 2.6075e-7],
]).T

IClimit9year = {'energy': IClimit9year[0] * u.GeV,
                'limit':  IClimit9year[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
                }

GRAND200K = np.loadtxt(path.join(datadir,'Grand200K.csv'),delimiter=',').T

GRAND200K = {'energy': GRAND200K[0] * u.GeV,
             'limit':  GRAND200K[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
            }

GRAND10K = np.loadtxt(path.join(datadir,'Grand10K.csv'),delimiter=',').T

GRAND10K = {'energy': GRAND10K[0] * u.GeV,
            'limit':  GRAND10K[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
           }


ARA = np.loadtxt(path.join(datadir,'ARA.csv'),delimiter=',').T

ARA = {'energy': ARA[0] * u.GeV,
       'limit':  ARA[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
      }


ARIANNA = np.loadtxt(path.join(datadir,'Arianna.csv'),delimiter=',').T

ARIANNA = {'energy': ARIANNA[0] * u.GeV,
           'limit':  ARIANNA[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
          }


Poemma = np.loadtxt(path.join(datadir,'data_Poemma.csv'),delimiter=',').T

Poemma = {'energy': Poemma[0] * u.GeV,
          'limit':  Poemma[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
         }


HESE = np.loadtxt(path.join(datadir,'neudata_icecubeICRC2017_981.txt')).T

HESE = {'energy': HESE[0] * u.GeV,
        'flux':   HESE[1] * 3 * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
        'lower_err': HESE[2] * 3 * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
        'upper_err': HESE[3] * 3 * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
       }


###############################################################################
# GRAND, 3 yr
###############################################################################

# Neutrino energy
# [GeV]
lst_nu_energy = np.array(
[48192296.5, 67644231.1, 94947581.6, 133271428.0,
 187063990.0, 262568931.0, 368550053.0, 517308507.0,
 726110577.0, 1019191760.0, 1430569790.0, 2007992980.0,
 2818482440.0, 3956111070.0, 5552922590.0, 7794257720.0,
 10940266600.0, 15356104100.0, 21554313200.0, 30254315500.0,
 42465913900.0, 59606499400.0, 83665567300.0, 117435636000.0,
 164836371000.0, 231369543000.0, 324757606000.0, 455840043000.0,
 639831498000.0, 898087721000.0, 1260584320000.0, 1769396010000.0,
 2483580190000.0, 3486031680000.0, 4893104280000.0, 6868115880000.0,
 9640304610000.0, 13531436400000.0, 18993151900000.0, 26659388600000.0]
)

# GRAND10k sensitivity, all-flavor, aggressive antenna threshold
# [GeV cm^{-2} s^{-1} sr^{-1}]
lst_sens_grand10k = np.array(
[8.41513361e-08, 7.38147706e-08, 5.69225180e-08, 3.46647934e-08,
 1.95651137e-08, 1.40651565e-08, 1.25782087e-08, 1.24621707e-08,
 1.31123151e-08, 1.45812119e-08, 1.65528260e-08, 1.91930521e-08,
 2.31554429e-08, 2.87477813e-08, 3.55164030e-08, 4.42563884e-08,
 5.63965197e-08, 7.45183330e-08, 1.01159657e-07, 1.39040439e-07,
 1.98526677e-07, 2.61742251e-07, 3.40870828e-07, 4.82745531e-07,
 6.55876763e-07, 9.07706655e-07, 1.67125879e-06, 1.76142511e-05,
 2.55022320e-04, 1.88371074e-03, 6.71431813e-03, 1.14286198e-02,
 1.14294614e-02, 1.72447830e-02, 7.48579143e-02, 3.31883351e-01,
 8.57786094e-01, 1.24824516e+00, 1.42294586e+00, 1.80135089e+00,]
)

# --- GRAND200k, all-flavor, aggressive antenna threshold
# [GeV cm^{-2} s^{-1} sr^{-1}]
lst_sens_grand200k = np.array(
[4.26219753e-09, 3.58147708e-09, 2.75670137e-09, 1.85254042e-09,
 1.13825106e-09, 7.70141315e-10, 6.51758930e-10, 6.35878242e-10,
 6.69261628e-10, 7.37439217e-10, 8.38784832e-10, 9.81688683e-10,
 1.18493794e-09, 1.45699379e-09, 1.80867621e-09, 2.26948852e-09,
 2.91952068e-09, 3.86790849e-09, 5.24530715e-09, 7.31211288e-09,
 9.98848945e-09, 1.33523293e-08, 1.80893102e-08, 2.46582187e-08,
 3.41054825e-08, 5.39140368e-08, 3.36553610e-07, 4.57179717e-06,
 3.59391218e-05, 1.47550853e-04, 3.33777479e-04, 4.92873322e-04,
 6.68381070e-04, 1.72553598e-03, 7.06643413e-03, 2.10754560e-02,
 4.06319101e-02, 5.88162853e-02, 7.45423652e-02, 8.83700084e-02,]
)

GRAND10K_new = {'energy': lst_nu_energy* u.GeV,
                'limit':  lst_sens_grand10k * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
               }
GRAND200K_new = {'energy': lst_nu_energy* u.GeV,
                 'limit':  lst_sens_grand200k * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
                }
###############################################################################
# POEMMA, 3 yr
###############################################################################

# Source: Presentation by Krizmanic at UHECR 2018 (solid black line)
# All-flavor, 5 years (conversion to 3 years occurs below)

arr_poemma_raw = np.array(
[[1.45008e+7, 1.33615e-6],
[1.50703e+7, 9.41392e-7],
[1.58198e+7, 6.63302e-7],
[1.67636e+7, 4.07279e-7],
[1.75934e+7, 2.72956e-7],
[1.78451e+7, 2.26258e-7],
[1.95011e+7, 1.65556e-7],
[2.18402e+7, 1.08250e-7],
[2.38657e+7, 7.82229e-8],
[2.58248e+7, 5.94231e-8],
[2.82221e+7, 4.37535e-8],
[3.21143e+7, 3.51729e-8],
[3.61823e+7, 2.88094e-8],
[3.99574e+7, 2.35945e-8],
[4.41240e+7, 1.90833e-8],
[5.02230e+7, 1.63315e-8],
[5.66017e+7, 1.43299e-8],
[6.97920e+7, 1.20406e-8],
[8.69502e+7, 1.09066e-8],
[1.06165e+8, 9.57406e-9],
[1.32258e+8, 8.56449e-9],
[1.68102e+8, 7.71031e-9],
[2.05322e+8, 7.34184e-9],
[2.55877e+8, 7.12422e-9],
[3.15721e+8, 6.99973e-9],
[4.17896e+8, 7.09869e-9],
[5.26160e+8, 7.28771e-9],
[7.14227e+8, 7.72270e-9],
[9.13042e+8, 8.28400e-9],
[1.16143e+9, 8.99775e-9],
[1.44819e+9, 9.89500e-9],
[1.78776e+9, 1.08811e-8],
[2.14160e+9, 1.18890e-8],
[2.83645e+9, 1.39233e-8],
[3.64550e+9, 1.62014e-8],
[4.73272e+9, 1.90906e-8],
[5.90299e+9, 2.24902e-8],
[7.89906e+9, 2.80407e-8],
[1.02568e+10, 3.45207e-8],
[1.31852e+10, 4.22308e-8],
[1.65308e+10, 5.16558e-8],
[2.17921e+10, 6.52101e-8],
[2.74587e+10, 7.97659e-8],
[3.67487e+10, 1.02613e-7],
[4.49295e+10, 1.22395e-7],
[5.71837e+10, 1.50662e-7]]
)
POEMMA_new = {'energy': arr_poemma_raw.T[0]* u.GeV,
              'limit':  5. / 3. * arr_poemma_raw.T[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
             }
# # [GeV]
# arr_poemma_energy_3yr = [x[0] for x in arr_poemma_raw]

# # [GeV cm^-2 s^-1 sr^-1]
# arr_poemma_sens_3yr = [x[1]/3.*5. for x in arr_poemma_raw]


###############################################################################
# ARA-37, 3 years
###############################################################################

# All-flavor
# Source: Fig. 25 in 1507.08991

arr_ara37_raw = np.array(
[[15.945, 2.2695e-7],
[16.017, 1.7610e-7],
[16.086, 1.3532e-7],
[16.151, 1.0398e-7],
[16.219, 8.0683e-8],
[16.288, 6.1997e-8],
[16.356, 4.8106e-8],
[16.432, 3.8437e-8],
[16.527, 3.1933e-8],
[16.623, 2.6790e-8],
[16.716, 2.2475e-8],
[16.812, 1.8855e-8],
[16.911, 1.6288e-8],
[17.017, 1.4630e-8],
[17.123, 1.3141e-8],
[17.229, 1.1804e-8],
[17.336, 1.0603e-8],
[17.449, 1.0197e-8],
[17.562, 9.9029e-9],
[17.675, 9.5239e-9],
[17.788, 9.1593e-9],
[17.901, 9.2491e-9],
[18.014, 9.3398e-9],
[18.127, 9.3398e-9],
[18.240, 9.4314e-9],
[18.353, 9.8068e-9],
[18.462, 1.0197e-8],
[18.575, 1.0603e-8],
[18.688, 1.1025e-8],
[18.798, 1.1920e-8],
[18.908, 1.3141e-8],
[19.017, 1.4348e-8],
[19.123, 1.5664e-8],
[19.229, 1.7439e-8],
[19.336, 1.9605e-8],
[19.442, 2.2040e-8],
[19.545, 2.4778e-8],
[19.651, 2.7856e-8],
[19.753, 3.1933e-8],
[19.856, 3.6251e-8],
[19.962, 4.1557e-8],
[20.065, 4.7177e-8]])

ARA_new = {'energy': 10**(arr_ara37_raw.T[0] - 9.)* u.GeV,
           'limit':  arr_ara37_raw.T[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
          }

# # [GeV]
# arr_ara37_energy_3yr = [pow(10, x[0]-9.0) for x in arr_ara37_raw]

# # [GeV cm^-2 s^-1 sr^-1]
# arr_ara37_sens_3yr = [x[1] for x in arr_ara37_raw]


###############################################################################
# ARIANNA, 3 years
###############################################################################

# All-flavor, 5 years (conversion to 3 years below)
# Source: Fig. 5.14 in Christopher Persichilli's 2017 thesis
# https://arianna.ps.uci.edu/sites/default/files/Persichilli_Thesis.pdf

arr_arianna_raw = np.array(
[[3.4571e+6, 1.3433e-7],
[4.4057e+6, 1.0656e-7],
[5.6148e+6, 8.5116e-8],
[7.1554e+6, 6.7522e-8],
[9.1192e+6, 5.3934e-8],
[1.1932e+7, 4.3981e-8],
[1.6169e+7, 3.6618e-8],
[2.1911e+7, 3.0488e-8],
[2.9435e+7, 2.5557e-8],
[4.1683e+7, 2.2483e-8],
[5.9036e+7, 2.0190e-8],
[8.4342e+7, 1.8008e-8],
[1.2050e+8, 1.6062e-8],
[1.6915e+8, 1.4129e-8],
[2.3745e+8, 1.2429e-8],
[3.3629e+8, 1.1086e-8],
[4.8916e+8, 1.0590e-8],
[7.1773e+8, 1.0117e-8],
[1.0350e+9, 9.7306e-9],
[1.5068e+9, 1.0516e-8],
[2.1746e+9, 1.1286e-8],
[3.1659e+9, 1.2114e-8],
[4.5702e+9, 1.3455e-8],
[6.5400e+9, 1.4944e-8],
[9.3590e+9, 1.6597e-8],
[1.3278e+10, 1.8686e-8],
[1.8677e+10, 2.1328e-8],
[2.6731e+10, 2.4180e-8],
[3.7274e+10, 2.7786e-8],
[5.1982e+10, 3.2372e-8],
[7.2496e+10, 3.7974e-8],
[1.0110e+11, 4.4240e-8],
[1.3856e+11, 5.1890e-8],
[1.9326e+11, 6.1288e-8],
[2.6718e+11, 7.1889e-8],
[3.6622e+11, 8.5484e-8],
[4.9761e+11, 1.0164e-7],
[6.8209e+11, 1.2170e-7],
[9.2686e+11, 1.4570e-7]])

ARIANNA_new = {'energy': arr_arianna_raw.T[0]* u.GeV,
               'limit':  5. / 3. * arr_arianna_raw.T[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
              }
# # [GeV]
# arr_arianna_energy_3yr = [x[0] for x in arr_arianna_raw]

# # [GeV cm^-2 s^-1 sr^-1]
# arr_arianna_sens_3yr = [x[1]/3.*5. for x in arr_arianna_raw]

ice_cube_limit_new = np.array(([
    (6.199999125,-7.698484687),
    (6.299999496,-8.162876678),
    (6.400000617,-8.11395291),
    (6.500000321,-8.063634144),
    (6.599999814,-8.004841781),
    (6.699999798,-7.944960162),
    (6.799999763,-7.924197388),
    (6.899999872,-7.899315263),
    (7.299999496,-7.730561153),
    (7.699999798,-7.670680637),
    (8.100001583,-7.683379711),
    (8.500000321,-7.748746801),
    (8.899999872,-7.703060304),
    (9.299999496,-7.512907553),
    (9.699999798,-7.370926525),
    (10.10000158,-7.134626026),
    (10.50000032,-6.926516638),
    (10.89999987,-6.576523031),
        ]))
IClimit9year_new = {'energy': 10**ice_cube_limit_new.T[0] * u.GeV,
                'limit':  10**ice_cube_limit_new.T[1] * u.GeV**1 * u.cm**-2 * u.s**-1 * u.sr**-1,
                }