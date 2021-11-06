# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:59:57 2021

@author: Jonathon
"""

#How do you find the missing number in a given integer array of 1 to 100

import random as rand
import math

def create_array(num):
    int_array = []
    for i in range(0,num):
        int_array.append(i)
    remove_int = rand.randint(0,num-1)
    int_array.remove(remove_int)
    return int_array

# Lets manually create a sort algorythm that checks in 50% intervals if high
# or low then checks again until it deturmines missing
# Binary search!

#int_array = [1,2,4,5,6,7]

def efficent_find(int_array):
    j = math.floor((len(int_array)+1)/2)
    step_size = math.floor(j/2)
    counter = 1
    found = []
    while len(found) == 0:
        print(j,"j",int_array[j],"intj")
        if (int_array[j] == j and int_array[j+1] != j+1):
            found.append(j+1)
        elif int_array[j] == j:
            j = j + math.floor(step_size/counter)
        elif int_array[j] != j:
            j = j - math.floor(step_size/counter)
        
        if counter < step_size:
            counter *= 2
        else:
            counter = step_size
            
    return found
    
print(efficent_find(create_array(2001)))