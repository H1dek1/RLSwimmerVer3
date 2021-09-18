#!/usr/bin/env python3

import numpy as np
import sys
import os
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm

def main():
    N = 1000
    fig, ax = plt.subplots(1,1, figsize=(8, 4.5))
    ax.set_title('Triangle model')
    ax.set_xlabel('Time Steps')
    ax.set_ylabel('Episode Reward')
    #ax.set_xlim(0, 2e+6)

    for id_dir, log_dir in enumerate(sys.argv[1:]):
        #print(logdir)
        #log_dir = sys.argv[1]
        path_list = glob.glob(log_dir+'*.csv')
        file_list = []
        for file_path in path_list:
            file_ = os.path.basename(file_path)
            file_list.append(file_)

        file_list.sort()
        print(file_list)

        steps_arr = []
        epirw_arr = []

        prev_sum_steps = 0

        for id_file, file_name in enumerate(file_list):
            data = np.loadtxt(log_dir+file_name, skiprows=1, delimiter=',')
            steps = data[:,1]
            episode_rewards = data[:,2]

            new_steps = []
            new_episode_rewards = []
            for step in steps:
                if step in new_steps:
                    continue
                indices = np.where(steps == step)
                tmp_sum = 0.0
                for i in indices[0]:
                    tmp_sum += episode_rewards[i]
                tmp_ave = tmp_sum / len(indices[0])
                #new_steps.append(step + id_file*one_file_steps)
                new_steps.append(step + prev_sum_steps)
                new_episode_rewards.append(tmp_ave)

            steps_arr += new_steps
            epirw_arr += new_episode_rewards
            prev_sum_steps += max(data[:,1])

        steps_arr = np.array(steps_arr)
        epirw_arr = np.array(epirw_arr)
        result = np.vstack([steps_arr, epirw_arr]).T
        result = result[np.argsort(result[:,0])]
        #print(result[:,0])

        """ Moving Average
        """
        sma = epirw_arr.copy()
        #print(epirw_arr)
        for i in tqdm(range(len(epirw_arr))):
            if i < int(N/2):
                sma[i] = sum(epirw_arr[:i+int(N/2)+1]) / int(i + N/2 + 1)
            elif len(sma)-int(N/2) < i:
                sma[i] = sum(epirw_arr[i-int(N/2):]) / int(len(sma)-i + N/2)
            else:
                sma[i] = sum(epirw_arr[i-int(N/2):i+int(N/2)+1]) / (N+1)

        ax.plot(result[:,0], result[:,1], color='C{}'.format(id_dir), label='{}'.format(log_dir))
        ax.plot(result[:,0], sma, color='C{}'.format(id_dir), label='{}'.format(log_dir))
    ax.legend()
    plt.show()
    fig.savefig('Test.png')

if __name__ == '__main__':
    main()
