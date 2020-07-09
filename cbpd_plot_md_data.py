#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:26:54 2019

@author: asmunroh
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['svg.fonttype'] = 'none'





data_folders = [ '<folder containing *.dat data files>',
                 '<folder containing *.dat data files>',
                 '<folder containing *.dat data files>']


tag = [ '_no_ptm.dat', '_ptm-1.dat', '_ptm-2.dat' ]


data_dist = []
for i in tag:
    data_dist.append(np.loadtxt('md_data'+i, usecols=2))
    


fig1 = plt.figure(figsize=(4,4))
ax1 = fig1.add_subplot(111)
ax1.violinplot(data_dist,showmedians=True)
#ax1.set_title('Distribution of M1-M3 distance over 500 ns MD-simulation')
ax1.set_ylabel('M1-M3 distance (Å)')
ax1.set_xticks([1,2,3])
ax1.set_xticklabels(['no-PTM','PTM-1','PTM-2'])
 
plt.savefig('MD_fig_Dist.svg', dpi=600)




data_rog = []
for i in tag:
    data_rog.append(np.loadtxt('RoG'+i, usecols=1))
    

fig2 = plt.figure(figsize=(4,4))
ax2 = fig2.add_subplot(111)
ax2.violinplot(data_rog,showmedians=True)
#ax2.set_title('Distribution of CbpD radius of gyration over 500 ns MD-simulation')
ax2.set_ylabel('Radius of gyration (Å)')
ax2.set_xticks([1,2,3])
ax2.set_xticklabels(['no-PTM','PTM-1','PTM-2'])

 
plt.savefig('MD_fig_RoG.svg', dpi=600)

