import numpy as np
import matplotlib.pyplot as plt

def drawK(ax):
    ax.set_xlim(1.0, 1.1)
    x = np.linspace(1.0, 1.1, 300)
    k = calcK(x)
    ax.plot(x, k, color='k', zorder=0)
    ax.hlines(y=0.0, xmin=1.0, xmax=1.1, color='k', zorder=0)
    ax.scatter(1.0245, 0, c='red', zorder=1, s=50)
    ax.set_xlabel(r'$k$', fontsize=25)
    ax.set_ylabel(r'$v_g$', fontsize=25)

def calcK(x):
    a = 0.1
    l = 1.0
    A = (-81*(a**2) + 552*a*l - 128*(l**2))
    B = (-480*a*l - 64*(l**2))
    C = 192*(l**2)
    denominator = 4608 * np.sqrt(3) * (a**2) * (x**2) * (l**2)
    return (A*(x**2) + B*x + C) / denominator
