#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats_hints.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function calculates_results_stats that calculates the statistics
#          of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
#  5: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with ": 5" for the calculates_results_stats 
#       function. Please be certain to replace None in the return statement with
#       the results_stats_dic dictionary that you create with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the classification results based on the classifier's performance. 
    Returns a dictionary containing both counts and percentages of various metrics.
    Parameters:
        results_dic - Dictionary with key as image filename and value as a List:
            idx 0 = pet image label (string)
            idx 1 = classifier label (string)
            idx 2 = 1/0 (int)  where 1 = match between pet image and classifier labels, 0 otherwise
            idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog, 0 otherwise
            idx 4 = 1/0 (int)  where 1 = classifier identifies as dog, 0 otherwise
    Returns:
        results_stats_dic - Dictionary containing the calculated statistics
    """
    results_stats_dic = {}

    # Initialize counters for required metrics
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    # Traverse results_dic to compute counts
    for key, values in results_dic.items():
        # Increment matching labels counter
        if values[2] == 1:
            results_stats_dic['n_match'] += 1

        # Count correctly classified dog breeds
        if values[3] == 1 and values[2] == 1:
            results_stats_dic['n_correct_breed'] += 1

        # Increment dog-related counters
        if values[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if values[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            # Increment non-dog related counter
            if values[4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1

    # Total images processed
    results_stats_dic['n_images'] = len(results_dic)

    # Compute non-dog images count
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0 if results_stats_dic['n_dogs_img'] > 0 else 0.0
