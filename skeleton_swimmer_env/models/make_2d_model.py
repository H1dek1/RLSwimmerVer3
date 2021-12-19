#!/usr/bin/env python3
import numpy as np

def main():
    max_layer = 6
    layers = np.arange(1, max_layer+1, 1)
    print(layers)

    n_sph_list = [1]
    n_arm_list = [0]
    initial_position_list = [
            [np.zeros(3)]
            ]

    for i, layer in enumerate(layers[1:]):
        n_sph_list.append( n_sph_list[-1] + layer )
        n_arm_list.append(
                n_arm_list[-1]
                + 2*(layer-1)
                + (layer - 1)
                )
        initial_position = [
                initial_position_list[i][0] + np.array([np.cos(-np.pi/6), np.sin(-np.pi/6), 0.0])
                ]
        for former_pos in initial_position_list[i]:
            new_pos = former_pos + np.array([np.cos(np.pi/6), np.sin(np.pi/6), 0.0])
            initial_position.append(new_pos)

        initial_position_list.append(initial_position)

    # initial_position_list = np.array(initial_position_list)
    print(n_sph_list)
    print(n_arm_list)
    for layer in initial_position_list:
        print('*'*20)
        for sph in layer:
            print(sph)


if __name__ == '__main__':
    main()
