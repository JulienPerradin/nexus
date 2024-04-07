import numpy as np
import matplotlib.pyplot as plt
import os
import sys

dir = sys.argv[1]

files = [
    'average_cluster_size.dat',
    'biggest_cluster_size.dat',
    'correlation_length.dat',
    'order_parameter.dat',
    'percolation_probability.dat',
    'spanning_cluster_size.dat',
]
for file in files:
    filename = file
    readed_data = {}

    if file != 'order_parameter.dat' and file != 'percolation_probability.dat':
        for subdir, dirs, files in os.walk(dir):
            dirs.sort()
            for file in files:
                if file == filename:
                    with open(os.path.join(subdir,file),'r') as i:
                        for l_index,line in enumerate(i):
                            if l_index == 0:
                                continue
                            else:
                                parts = line.split()
                                if parts[-1] not in readed_data:
                                    readed_data[parts[-1]] = []
                                readed_data[parts[-1]].append([float(parts[0]),float(parts[2])])
    else:
        for subdir, dirs, files in os.walk(dir):
            dirs.sort()
            for file in files:
                if file == filename:
                    with open(os.path.join(subdir,file),'r') as i:
                        for l_index,line in enumerate(i):
                            if l_index == 0:
                                continue
                            else:
                                parts = line.split()
                                if parts[-1] == '1D':
                                    if parts[-3] not in readed_data:
                                        readed_data[parts[-3]] = []
                                    readed_data[parts[-3]].append([float(parts[0]),float(parts[2])])


    # get the reference data:
    ref_files = {
        "average_cluster_size.dat" : '../../reference-check/sio2-1008at-11frames/AverageClusterSize.dat',
        "biggest_cluster_size.dat" : '../../reference-check/sio2-1008at-11frames/BiggestClusterSize.dat',
        "correlation_length.dat" : '../../reference-check/sio2-1008at-11frames/CorrelationLength.dat',
        "percolation_probability.dat" : '../../reference-check/sio2-1008at-11frames/PercolationProbability1D.dat',
        "order_parameter.dat" : '../../reference-check/sio2-1008at-11frames/Pinf.dat',
        "spanning_cluster_size.dat" : '../../reference-check/sio2-1008at-11frames/SpanningClusterSize.dat',
    }
    
    for k, v in ref_files.items():
        if k == filename:
            with open(v,'r') as i:
                for l_index,line in enumerate(i):
                    if l_index == 0:
                        ref_keys = line.split()[-3:]
                    else:
                        for l, this_k in enumerate(ref_keys):
                            parts = line.split()[-3:]
                            if this_k not in readed_data:
                                readed_data[this_k] = []
                            readed_data[this_k].append([float(parts[l])])
    
    
    # list here the keys to plot

    # keys = [
    #     ["SiO4-SiO4", "Si4-Si4", '4-4'],
    #     ["SiO4-SiO5", "Si4-Si5"],
    #     ["SiO5-SiO5", "Si5-Si5", '5-5'],
    #     ["SiO5-SiO6", "Si5-Si6"],
    #     ["SiO6-SiO6", "Si6-Si6", "6-6"],
    #     ["O2-O2", "O2-O3", "O3-O3"]
    # ]
    
    keys = [
        ["SiO4-SiO4", "Si4-Si4"],
        ["SiO4-SiO5", "Si4-Si5"],
        ["SiO5-SiO5", "Si5-Si5"],
        ["SiO5-SiO6", "Si5-Si6"],
        ["SiO6-SiO6", "Si6-Si6", "SiO6-SiO6-stishovite", "Si6-Si6-stishovite"],
        ["O2-O2", "O2-O3", "O3-O3"]
    ]
    
    # keys = [
    #     ["Si4-Si4", '4-4'],
    #     ["Si4-Si5"],
    #     ["Si5-Si5", '5-5'],
    #     ["Si5-Si6"],
    #     ["Si6-Si6", "6-6"],
    #     ["O2-O2", "O2-O3", "O3-O3"]
    # ]

    colours = ['black', 'red', 'blue', 'lime', 'orange', 'cyan', 'magenta', 'yellow', 'purple', 'pink']
    # plot data corresponding to the keys

    fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 9))
    for i, key in enumerate(keys):
        for j, k in enumerate(key):
            if k not in ref_keys:
                ax[i//3, i%3].errorbar(range(len(readed_data[k])), np.array(readed_data[k])[:,0], np.array(readed_data[k])[:,1], label=k, fmt='-o', mec="black", mfc=colours[j], color=colours[j])
                ax[i//3, i%3].fill_between(range(len(readed_data[k])), np.array(readed_data[k])[:,0]-np.array(readed_data[k])[:,1], np.array(readed_data[k])[:,0]+np.array(readed_data[k])[:,1], alpha=0.2, color=colours[j])
            else:
                ax[i//3, i%3].plot(range(len(readed_data[k])), np.array(readed_data[k])[:,0], '--', label=k, color=colours[j])
            
        ax[i//3, i%3].set_title(str(key).replace(',',' |').replace('[','').replace(']','').replace('\'',''))
        ax[i//3, i%3].set_xlabel('Pressure (GPa)')
        ax[i//3, i%3].set_ylabel('Correlation length (Å)')
        ax[i//3, i%3].legend(loc='best')
        if i == 5:
            ax[i//3, i%3].set_title('OSi2-OSi2 | OSi2-OSi3 | OSi3-OSi3')
    plt.suptitle(f"SiO2 1008at 11frames - {str(filename.split('.')[0]).replace('_',' ').title()}", fontsize=16)
    plt.tight_layout()
    plt.savefig(f"{dir}/{filename.split('.')[0]}.png")
    
    with open(f"{dir}/{filename.split('.')[0]}.txt", 'w') as o:
        o.write("# Pressure \t")
        for key in readed_data.keys():
            o.write(f"{key}\t")
        o.write("\n")
        for i in range(len(readed_data[key])):
            o.write(f"{i}\t")
            for key in readed_data.keys():
                o.write(f"{readed_data[key][i][0]}\t")
            o.write("\n")
            
    # plt.show()