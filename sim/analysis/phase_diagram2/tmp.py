#!/usr/bin/env python3

import numpy as np
import json

def main():
    wrapper = open('./data/without_energy/b.json', 'r')
    strategy = json.load(wrapper)
    beats = np.vectorize(str)(np.arange(1, 20, 1))
    print(beats)
    strategy.pop('name')
    for beat in beats:
        print(strategy[beat]['0.95']['1.05'])


if __name__ == '__main__':
    main()
