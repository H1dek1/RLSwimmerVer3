#!/usr/bin/env python3

import sys
import json
import numpy as np

def main():
    file_obj = open('optimals/withoutEnergy_phaseDiagram2.json', 'r')
    phase = json.load(file_obj)
    action_interval = sys.argv[1]
    max_length      = sys.argv[2]
    print('action interval:', action_interval)
    print('max length     :', max_length)
    print('strategy       :', phase[action_interval][max_length]['name'])
    print('displacement   :', phase[action_interval][max_length]['displacement'])


if __name__ == '__main__':
    main()
