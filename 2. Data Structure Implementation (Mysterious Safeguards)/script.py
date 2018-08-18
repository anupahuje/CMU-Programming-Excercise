#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:43:15 2018

@author: Anup
"""

from intervaltree import Interval, IntervalTree
import copy

def get_coverage(t):
    t_copy = copy.deepcopy(t)
    t_copy.merge_overlaps()
    coverage = 0 
    for item in t_copy.items():
        coverage += item.length()
    return coverage

def get_cvg_affect(ovlp_interval_set, i):
    ovlp_interval_set_tree = IntervalTree(ovlp_interval_set)
    if len(ovlp_interval_set_tree) == 1:
        return i.length()
    else:
        set_coverage = get_coverage(ovlp_interval_set_tree)
        ovlp_interval_set_tree.remove(i)
        set_coverage_after = get_coverage(ovlp_interval_set_tree)
        return set_coverage-set_coverage_after

def get_max_coverage(input_file):
    coverage_list = []
    interval_list = []
    total_coverage = 0
    for idx, val in enumerate(input_file):
        if idx != 0:
            inp = tuple([int(x) for x in val.split(' ')])
            interval_list.append(inp)
    t = IntervalTree(Interval(*iv) for iv in interval_list)
    total_coverage = get_coverage(t)
    
    for idx, inter in enumerate(interval_list):
        i = Interval(*inter)
        ovlp_interval_set = t.search(i)
        cvg_affect = get_cvg_affect(ovlp_interval_set, i)
        coverage_list.append(total_coverage-cvg_affect)
    return max(coverage_list)

if __name__ == "__main__":
    for z in range(1,11):
        path = "./Data/"+str(z)+".in"
        input_file = open(path, 'r')
        val = get_max_coverage(input_file)
        with open("./Data/output/"+str(z)+".out", 'a') as the_file:
            the_file.write(str(val))
    