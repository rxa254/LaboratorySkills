import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from cycler import cycler

import numpy as np

def set_plot_params():
    '''
    this function sets up the default plot settings via the matplotlib rcParams interface.
    Much cleaner than putting this in each notebook or defining settings for each plot.
    ** Maybe make this a mplstyle instead so that we can just use plt.style.use('fubar') **
    '''
    plt.rcParams.update({'text.usetex': False,
                     'lines.linewidth': 4,
                     'font.family': 'serif',
                     'font.serif': 'Georgia',
                     'font.size': 22,
                     'xtick.direction': 'in',
                     'ytick.direction': 'in',
                     'xtick.labelsize': 'medium',
                     'ytick.labelsize': 'medium',
                     'axes.labelsize': 'medium',
                     'axes.titlesize': 'medium',
                     'axes.grid.axis': 'both',
                     'axes.grid.which': 'both',
                     'axes.grid': True,
                     'grid.color': 'xkcd:poop brown',
                     'grid.alpha': 0.35,
                     'lines.markersize': 12,
                     'legend.borderpad': 0.2,
                     'legend.fancybox': True,
                     'legend.fontsize': 'small',
                     'legend.framealpha': 0.8,
                     'legend.handletextpad': 0.5,
                     'legend.labelspacing': 0.33,
                     'legend.loc': 'best',
                     'figure.figsize': ((12, 8)),
                     'savefig.dpi': 140,
                     'savefig.bbox': 'tight',
                     'pdf.compression': 9})
    

def multZPG(P, C, A):
    # multiply them together by concatenating the zeros and poles
    pos = np.hstack((P.poles, C.poles, A.poles))
    zos = np.hstack((P.zeros, C.zeros, A.zeros))
    G = P.gain * C.gain * A.gain
    return sig.ZerosPolesGain(zos, pos, G)


    
