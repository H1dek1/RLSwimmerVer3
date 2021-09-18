#!/usr/bin/env python3

import numpy as np
import pandas as pd
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
        path_list = glob.glob(log_dir+'*.csv')
        file_list = []
        for file_path in path_list:
            file_ = os.path.basename(file_path)
            file_list.append(file_)

        file_list.sort()
        print(f'{len(file_list)} files found.')

        steps_arr = []
        epirw_arr = []
        df_total = pd.DataFrame(columns={'Step', 'Value'})

        total_steps = 0

        for id_file, file_name in enumerate(file_list):
            df_i = pd.read_csv(log_dir+file_name)[['Step', 'Value']]
            df_i['Step'] = df_i['Step'] + total_steps
            total_steps = df_i['Step'].iloc[-1]
            
            df_total = pd.concat([df_total, df_i])
            

        print(df_total.size)
        ax.plot(df_total['Step'], df_total['Value'], label=log_dir)


        """ Moving Average
        """
        #sma = epirw_arr.copy()
        ##print(epirw_arr)
        #for i in tqdm(range(len(epirw_arr))):
        #    if i < int(N/2):
        #        sma[i] = sum(epirw_arr[:i+int(N/2)+1]) / int(i + N/2 + 1)
        #    elif len(sma)-int(N/2) < i:
        #        sma[i] = sum(epirw_arr[i-int(N/2):]) / int(len(sma)-i + N/2)
        #    else:
        #        sma[i] = sum(epirw_arr[i-int(N/2):i+int(N/2)+1]) / (N+1)

        #ax.plot(result[:,0], result[:,1], color='C{}'.format(id_dir), label='{}'.format(log_dir))
        #ax.plot(result[:,0], sma, color='C{}'.format(id_dir), label='{}'.format(log_dir))
    ax.legend()
    plt.show()
    fig.savefig('Test.png')

if __name__ == '__main__':
    main()
