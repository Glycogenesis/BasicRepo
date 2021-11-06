# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:36:14 2021

Jane Street Puzzle
Robot Swimming Trials
# https://www.janestreet.com/puzzles/robot-swimming-trials-index/
3N competitors roll a dice 1-N
we don't care about who wins with a draw as we will never draw when we
use 1/N constant strategy
we need to find p() of rolling an incomplete set of 1- N from 3N dice rolls
"""

import random as rand

# Start off with N = 2 as the simplest case (N = 1 is a trivial 3 way tie)
# N = Number of races, 3N contestants (dice)

"""
rolling function uses randint(1,N) - this is the choice of which race to place
your entire fuel on, cannot be 0 as there is no 0th race, goes up to and including N
i goes from range 0 -> 3N, this is because the range function does not include 3N,
therefoe 0->3N includes 3N values (competitors / robots)
When we move this from 0->1 starting we are representing that our robot is not going
to follow this strategy, this will increase the chance of there being a not full set
"""

def rolling(N):
    roll_list = [rand.randint(1,N) for i in range(1,3*N)] # list comprehension
    return roll_list

def check_list(int_list,N): # check a list, return true if unique items in list != N  
    if len(set(int_list)) == N: # True means non nash eq strat wins
        return False
    else:
        return True

def add_list(bol,outcome_list): # appends 1 for wins, 0 for losses
    if bol == True:
        outcome_list.append(1)
    else:
        outcome_list.append(0)
    return outcome_list

def main(N,iterations):
    i = 0
    out_list = []
    while i < iterations:
        roll = rolling(N)
        outcome = check_list(roll,N)
        out_list = add_list(outcome, out_list)
        i += 1
        #print(roll,outcome,out_list)
    win_chance = sum(out_list)/len(out_list)
    print("Estimate of the win chance with N = 8")
    print(win_chance)
    return

main(8,100000)
