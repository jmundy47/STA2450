
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import scipy
import numpy as np


# Module to change working directory
import os

os.chdir("C:/Users/19366/Documents/Baylor Assignments (Fall 2023)/Python Files")

# Data Import
dat2 = pd.read_csv("2017_Fuel_Economy_Data.csv")
y = dat2['Combined Mileage (mpg)']
x = pd.DataFrame(boot_stat(dat2['Combined Mileage (mpg)'], 'mean'))

# Generate a class for bootstrapped samples' CI
#%%
class Boot():
    def __init__(self, data = None, stat = "mean"):
        self.stat = stat
        self.dat = data
        self.boot_stat = []
        self.n_boot = len(self.boot_stat)
        self.conf_level = 0.95 
        self.n = len(data)

    def assign_data(self, data):
        self.dat = data
        self.n = len(data)
        
    def clear_stat_list(self):
        self.boot_stat = []
        
    def set_statistic(self, statistic):
        self.stat = statistic
        self.clear_stat_list()
        
    def sims_loop(self, boots):
        for i in range(boots):
            self.n_boot =+ 1
            boot_sample = self.dat.sample(self.n, replace = True)
            if self.stat == 'median':
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == 'mean':
                self.boot_stat.append(float(boot_sample.mean()))
                
            elif self.stat == 'std':
                self.boot_stat.append(float(boot_sample.std()))
            else:
                raise TypeError("Invalid Statistic Name")
                
    def plot_boot(self):
        df = pd.DataFrame({self.stat: self.boot_stat})
        plot = (
        ggplot(data = df, mapping = aes(x = self.stat)) + 
         geom_histogram()
         )
        return(plot)
        
    def CI(self):
        conf = (100 - self.conf_level*100)/2
        if self.n_boot == 0:
            print("No Boots Performed")
        else: 
            return(np.percentile(self.boot_stat, [conf, 100-conf]))

#%%
boot1 = Boot(data = x, stat = "mean")
boot1.sims_loop(100)
boot1.boot_stat
boot1.plot_boot()
boot1.CI()

#%%
boot2 = Boot(data = y, stat = "std")
boot2.sims_loop(10000)
boot2.boot_stat
boot2.plot_boot()
boot2.CI()
