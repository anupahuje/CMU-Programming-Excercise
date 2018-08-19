#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:43:15 2018

@author: Anup
"""

from intervaltree import Interval, IntervalTree
import copy
import pandas as pd

def get_coverage(t):
    t_copy = copy.deepcopy(t)
    t_copy.merge_overlaps()
    coverage = 0 
    for item in t_copy.items():
        coverage += item.length()
    return coverage

def get_cvg_affect(ovlp_interval_set_tree, i):
    if len(ovlp_interval_set_tree) == 1:
        return i.length()
    else:
        set_coverage = get_coverage(ovlp_interval_set_tree)
        ovlp_interval_set_tree.remove(i)
        set_coverage_after = get_coverage(ovlp_interval_set_tree)
        return set_coverage-set_coverage_after

def get_ovlp_interval_tree(df, interval):
    range_f = interval[0]
    range_l = interval[1]
    df_ins = df[(df['start'] > range_f) & (df['end'] <= range_l) | (df['start'] >= range_f) & (df['end'] < range_l)]
    if len (df_ins) != 0:
        return None
    df_env = df[(df['start'] == range_f) & (df['end'] == range_l)]
    #df_env['overlap']='env'
    df_left = df[(df['start'] < range_f) & (df['end'] < range_l) & (df['end'] > range_f)]
    #df_left['overlap']='left'
    df_right = df[(df['start'] > range_f) & (df['start'] < range_l) & (df['end'] > range_l)]
    #df_right['overlap']='right'
    df_flit = pd.concat([df_env,df_left,df_right])

    interval_list_temp = df_flit.values.tolist()
    interval_list_temp = [tuple(l) for l in interval_list_temp]
    t = IntervalTree(Interval(*iv) for iv in interval_list_temp)
    return t

def get_max_coverage(df):
    coverage_list = []
    interval_list = []
    total_coverage = 0
    
    interval_list = df.values.tolist()
    interval_list = [tuple(l) for l in interval_list]
    t = IntervalTree(Interval(*iv) for iv in interval_list)

    total_coverage = get_coverage(t)
    length = len(interval_list)
    for idx, inter in enumerate(interval_list):
#        if idx % 10 == 0: 
        print "#########"
        print (idx*100.0/length),"%"
        print "#########"
        i = Interval(*inter)
#        ovlp_interval_set = t.search(i)
        ovlp_interval_tree = get_ovlp_interval_tree(df, inter)
        if ovlp_interval_tree == None:
            return total_coverage
        cvg_affect = get_cvg_affect(ovlp_interval_tree, i)
        coverage_list.append(total_coverage-cvg_affect)
    return max(coverage_list)

if __name__ == "__main__":
    for z in range(1,11):
#        z = 5
        df = pd.read_csv("./Data/"+str(z)+".in", sep=" ",skiprows=1, header=None)
        df.columns = ['start', 'end']
        val = get_max_coverage(df)
        with open("./Data/output/"+str(z)+".out", 'a') as the_file:
            the_file.write(str(val))
    