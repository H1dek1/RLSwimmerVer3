#!/usr/bin/env python3
import numpy as np

def main():
    output_list = [2, 3, 4, 5, 6]
    max_layer = 6
    layers = np.arange(1, max_layer+1, 1)

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

    for output_type in output_list:
        # print('output_type =', output_type)
        idx = np.where(layers == output_type)[0][0]
        # print('index', idx)
        # print(n_sph_list[idx])
        # print(n_arm_list[idx])
        sph_pos = []
        for layer in initial_position_list[:idx+1]:
            for sph in layer:
                sph_pos.append(sph)

        # for pos in sph_pos:
        #     print(pos)
        np.savetxt(
                f'type_20{output_type}/num_states.txt',
                [n_sph_list[idx], n_arm_list[idx]],
                fmt='%d'
                )
        np.savetxt(
                f'type_20{output_type}/init_pos.txt',
                sph_pos,
                fmt='%.5f'
                )



if __name__ == '__main__':
    main()
