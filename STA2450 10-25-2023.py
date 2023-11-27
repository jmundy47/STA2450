# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:40:05 2023

@author: 19366
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import scipy

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
    return boot_stat

boot_stat(dat, 'median')
boot_stat(dat, 'variance')


# Module to change working directory
import os

os.chdir("C:/Users/19366/Documents/Baylor Assignments (Fall 2023)/Python Files")

# Data Import
dat2 = pd.read_csv("2017_Fuel_Economy_Data.csv")

x = pd.DataFrame(boot_stat(dat2['Combined Mileage (mpg)'], 'mean'))

# Generate a class for bootstrapped samples' CI
class BootCI():
    def __init__(self, data = None, n_boot = 1):
        self.stat = "mean"
        self.dat = data
        self.n_boot = n_boot
        self.boot_stat = []
        self.conf_level = 0.95 
        self.n = len(data)

        
    def assign_data(self, data):
        self.dat = data
        self.n = len(self.data)
        
    def set_n_boot(self, n_boot):
        self.n_boot = n_boot
        
    def sims_loop(self):
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(self.n, replace = True)
            if self.stat == 'median':
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == 'mean':
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == 'std':
                self.boot_stat.append(float(boot_sample.std()))
            else:
                raise TypeError("Invalid Statistic Name")
                
    def clear_sims_list(self):
        self.sims_list = []
        
boot1 = BootCI(data = x)
boot1.sims_loop()
boot1.boot_stat






