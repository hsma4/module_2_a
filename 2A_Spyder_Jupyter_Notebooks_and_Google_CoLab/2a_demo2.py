#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:47:44 2021

@author: dan
"""


import matplotlib.pyplot as plt
import random

exponential_distribution_mean = 5.0
normal_distribution_mean = 25.0
normal_distribution_st_dev = 5.0
list_of_sampled_numbers = []

print ("Please select a distribution and number of random number samples.")
selected_distribution = input("E : Exponential, N = Normal : ")
samples = int(input("How many generations? : "))

if selected_distribution == "E":
    for s in range(samples):
        sampled_number = random.expovariate(1.0 / 
                                            exponential_distribution_mean)
        
        list_of_sampled_numbers.append(sampled_number)
elif selected_distribution == "N":
    for s in range(samples):
        sampled_number = random.normalvariate(normal_distribution_mean, 
                                              normal_distribution_st_dev)
        list_of_sampled_numbers.append(sampled_number)
else:
    print ("Invalid distribution selected")
    
if selected_distribution == "E" or selected_distribution == "N":
    figure_1, ax = plt.subplots()
    
    ax.hist(list_of_sampled_numbers, 100)
    
    figure_1.show()

