import numpy as np
import matplotlib.pyplot as plt

def drawK(ax):
    ax.set_xlim(1.0, 1.1)
    x = np.linspace(1.0, 1.1, 300)
    k = calcK(x)
    ax.plot(x, k, color='k', zorder=0)
    ax.hlines(y=0.0, xmin=1.0, xmax=1.1, color='k', zorder=0)
    ax.scatter(1.0561, 0, c='red', zorder=1, s=50)
    ax.set_xlabel(r'$k$', fontsize=25)
    ax.set_ylabel(r'$v_g$', fontsize=25)

def calcK(x):
    a = 0.1
    l = 1.0
    A = -270*(a**2)*x + 48*a*(-8+11*x)*l - 256*(-1+x)*(l**2)
    B = 3*np.sqrt(3)*( 405*(a**2)*x + 64*(2+x)*(l**2) - 192*a*(l + 2*x*l) )
    return A / B
