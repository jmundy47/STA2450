# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:40:05 2023

@author: 19366
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

dat = pd.DataFrame({'handspan': [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5, 21.5, 
                                 18, 18, 20.5, 20, 20.3, 21.5, 19, 20.4, 22.7, 22.9, 
                                 17, 23, 23.8, 22, 21.5, 21.5]})

boot_means = []
for i in range(10000):
    boot_sample = dat.sample(26, replace = True)
    boot_means.append(float(boot_sample.mean()))


boot_means_df = pd.DataFrame({'means' : boot_means})

(
ggplot(boot_means_df, aes(x = 'means')) +
geom_histogram()
)

boot_medians = []
for i in range(10000):
    boot_sample = dat.sample(26, replace = True)
    boot_medians.append(float(boot_sample.median()))

boot_medians_df = pd.DataFrame({'medians' : boot_medians})

(
ggplot(boot_medians_df, aes(x = 'medians')) +
geom_histogram()
 )

# generalized function

def boot_stat(data, stat, n_boot = 10000):
    boot_stat = []
    for i in range(n_boot):
        boot_sample = data.sample(len(data), replace = True)
        if stat == 'median':
            boot_stat.append(float(boot_sample.median()))
        elif stat == 'mean':
            boot_stat.append(float(boot_sample.mean()))
        elif stat == 'std':
            boot_stat.append(float(boot_sample.std()))
        else:
            raise TypeError("Invalid Statistic Name")
    return pd.DataFrame(boot_stat)

boot_stat(dat, 'median')
boot_stat(dat, 'variance')


# Module to change working directory
import os

os.chdir("C:/Users/19366/Documents/Baylor Assignments (Fall 2023)/Python Files")

# Data Import
dat2 = pd.read_csv("2017_Fuel_Economy_Data.csv")

x = pd.DataFrame(boot_stat(dat2['Combined Mileage (mpg)'], 'mean'))

<<<<<<< HEAD
# Generate a class for bootstrapped samples' CI
class BootCI():
    def __init__(self):
        self.stat = "mean"
        self.dat = None
        self.n_boot = 0
        self.boot_stat = None
        self.conf_level = 0.95 
        
        
=======

>>>>>>> bf48d768018d55eaf8a472a088dc52418d2c68f5

















