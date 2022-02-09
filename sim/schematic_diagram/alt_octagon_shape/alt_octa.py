#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 12

from ng_swimmer_transition import drawNGSwimmerTransition

def main():
    fig, ax = plt.subplots(2, 2, figsize=(8, 12), tight_layout=False)
    fig.subplots_adjust(hspace=0.5, wspace=0.2, left=0.05, right=0.98,
            bottom=0.15, top=0.95)
    drawNGSwimmerTransition(ax[0][0])
    ax[0][0].set_title('(a)', loc='left')
    ax[0][1].set_title('(b)', loc='left')
    ax[1][0].set_title('(c)', loc='left')
    ax[1][1].set_title('(d)', loc='left')
    armSpaceSetting(ax[0][1])
    armSpaceSetting(ax[1][1])
    drawSquare(ax[0][1])
    drawOctagon(ax[1][1])
    drawArmExtensileVelocity(ax[1][0])
    plt.show()
    fig.savefig('alt_octagon.pdf')

def drawArmExtensileVelocity(ax):
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\dot{\ell}_0^*$', fontsize=20)
    ax.set_ylabel(r'$\dot{\ell}_1^*$', fontsize=20)
    ticks = [-1.0, 0.0, 1.0]
    ax.set_xticks(ticks)
    ax.set_xticklabels(np.vectorize(str)(ticks))
    ax.set_yticks(ticks)
    ax.set_yticklabels(np.vectorize(str)(ticks))

    v01 = np.array([1.0, 0.0])
    v02 = np.array([0.0, 1.0])
    v03 = np.array([-1.0, 0.0])
    v04 = np.array([0.0, -1.0])
    num0 = [r'$1$', r'$2$', r'$3$', r'$4$']
    beta = 1.3
    for i, v0 in enumerate([v01, v02, v03, v04]):
        ax.scatter(v0[0], v0[1], color='k', s=30)
        ax.text(beta*v0[0], beta*v0[1], num0[i], fontsize=15, 
                color='k', va='center', ha='center')
        circ = patches.Circle(xy=(beta*v0[0], beta*v0[1]+0.02),
                radius=0.15, fill=False, ec='k')
        ax.add_patch(circ)
    # ax.plot([v01[0], v02[0]], [v01[1], v02[1]], color='k', ls='--')
    # ax.plot([v02[0], v03[0]], [v02[1], v03[1]], color='k', ls='--')
    # ax.plot([v03[0], v04[0]], [v03[1], v04[1]], color='k', ls='--')
    # ax.plot([v04[0], v01[0]], [v04[1], v01[1]], color='k', ls='--')
    v11 = np.array([1.0, -1.0])
    v12 = np.array([1.0, 1.0])
    v13 = np.array([-1.0, 1.0])
    v14 = np.array([-1.0, -1.0])
    num1 = [r"$1'$", r"$2'$", r"$3'$", r"$4'$"]
    for i, v1 in enumerate([v11, v12, v13, v14]):
        ax.scatter(v1[0], v1[1], color='r', s=30)
        ax.text(beta*v1[0], beta*v1[1], num1[i], fontsize=15, 
                color='r', va='center', ha='center')
        circ = patches.Circle(xy=(beta*v1[0], beta*v1[1]+0.02),
                radius=0.15, fill=False, ec='r')
        ax.add_patch(circ)

def armSpaceSetting(ax):
    ax.set_xlim(0.8, 1.7)
    ax.set_ylim(0.8, 1.7)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$\ell_0^*$', fontsize=20)
    ax.set_ylabel(r'$\ell_1^*$', fontsize=20)

def drawSquare(ax):
    ax.set_xlabel(r'$\ell_0$', fontsize=30)
    ax.set_ylabel(r'$\ell_1$', fontsize=30)
    ticks = [1.0, 1.3]
    ax.set_xticks(ticks)
    # ax.set_xticklabels(['$1.0$\n$(\ell^{\min*})$', '$1.3$\n$(\ell^{\max*})$'])
    ax.set_yticks(ticks)
    # ax.set_yticklabels(['$1.0$\n$(\ell^{\min*})$', '$1.3$\n$(\ell^{\max*})$'])
    ax.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
    A = np.array([1.0, 1.0])
    B = np.array([1.3, 1.0])
    C = np.array([1.3, 1.3])
    D = np.array([1.0, 1.3])
    for pos in [A, B, C, D]:
        ax.scatter(pos[0], pos[1], color='k', s=20)
    vector2d(ax, A, B)
    vector2d(ax, B, C)
    vector2d(ax, C, D)
    vector2d(ax, D, A)
    numbering(ax, A, B, r'$1$')
    numbering(ax, B, C, r'$2$')
    numbering(ax, C, D, r'$3$')
    numbering(ax, D, A, r'$4$')
    ax.text(A[0]-0.02, A[1]-0.02, r'$A$', fontsize=20, ha='right', va='top')
    ax.text(B[0]-0.02, B[1]-0.02, r'$B$', fontsize=20, ha='right', va='top')
    ax.text(C[0]-0.02, C[1]-0.02, r'$C$', fontsize=20, ha='right', va='top')
    ax.text(D[0]-0.02, D[1]-0.02, r'$D$', fontsize=20, ha='right', va='top')
    
    ax.vlines(x=[1.0, 1.3], ymin=0.0, ymax=1.0, ls='--', lw=0.5, color='k')
    ax.hlines(y=[1.0, 1.3], xmin=0.0, xmax=1.0, ls='--', lw=0.5, color='k')


def drawOctagon(ax):
    ticks = [1.0, 1.3, 1.5]
    ax.set_xticks(ticks)
    ax.set_xticklabels(['$1.0$\n$(\ell^{\min*})$', '$1.3$', '$1.5$\n$(\ell^{\max*})$'])
    ax.set_yticks(ticks)
    ax.set_yticklabels(['$1.0$\n$(\ell^{\min*})$', '$1.3$', '$1.5$\n$(\ell^{\max*})$'])
    A = np.array([1.0, 1.0])
    B = np.array([1.3, 1.0])
    C = np.array([1.3, 1.3])
    D = np.array([1.0, 1.3])
    for pos in [A, B, C, D]:
        ax.scatter(pos[0], pos[1], color='k', s=20)
    ax.text(A[0]-0.02, A[1]-0.02, r'$\mathscr{A}$', fontsize=15, ha='right', va='top')
    ax.text(B[0]-0.02, B[1]-0.02, r'$\mathscr{B}$', fontsize=15, ha='right', va='top')
    ax.text(C[0]-0.02, C[1]-0.02, r'$\mathscr{C}$', fontsize=15, ha='right', va='top')
    ax.text(D[0]-0.02, D[1]-0.02, r'$\mathscr{D}$', fontsize=15, ha='right', va='top')
    
    ax.vlines(x=[1.0, 1.3, 1.5], ymin=0.0, ymax=1.5, ls='--', lw=0.5, color='k')
    ax.hlines(y=[1.0, 1.3, 1.5], xmin=0.0, xmax=1.5, ls='--', lw=0.5, color='k')

    A2 = np.array([1.2, 1.0])
    B2 = np.array([1.5, 1.2])
    C2 = np.array([1.5, 1.3])
    C3 = np.array([1.3, 1.5])
    C4 = np.array([1.2, 1.5])
    D2 = np.array([1.0, 1.2])
    vector2d(ax, A2, B, color='red')
    ax.plot([B[0], B2[0]], [B[1], B2[1]], color='red')
    vector2d(ax, B2, C2, color='red')
    ax.plot([C2[0], C3[0]], [C2[1], C3[1]], color='red')
    vector2d(ax, C3, C4, color='red')
    ax.plot([C4[0], D[0]], [C4[1], D[1]], color='red')
    vector2d(ax, D, D2, color='red')
    ax.plot([D2[0], A2[0]], [D2[1], A2[1]], color='red')
    numbering(ax, B, B2,  r"$2'$", color='red')
    numbering(ax, C2, C3, r"$3'$", color='red')
    numbering(ax, C4, D,  r"$4'$", color='red')
    numbering(ax, D2, A2, r"$1'$", color='red')

def vector2d(ax, start, target, color='k'):
    vec = target - start
    coef = 1.8
    ax.quiver(start[0], start[1], vec[0], vec[1], angles='xy', scale_units='xy', scale=1, headwidth=coef*3, headlength=coef*5, headaxislength=coef*4.5, color=color)

def numbering(ax, pos0, pos1, n, color='k'):
    vec = pos1 - pos0
    vec /= np.linalg.norm(vec)
    center = (pos0 + pos1) / 2
    pos = center + 0.08*np.array([vec[1], -vec[0]])
    ax.text(pos[0], pos[1], n, fontsize=20, va='center', ha='center', color=color)
    circ = patches.Circle(xy=(pos[0]+0.003, pos[1]+0.005), radius=0.04, fill=False, ec=color)
    ax.add_patch(circ)


if __name__ == '__main__':
    main()
