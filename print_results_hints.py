#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function print_results that prints the results statistics from the
#          results statistics dictionary (results_stats_dic). It should also
#          allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
#  6: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with ": 6" for the print_results function.
#       Specifically edit and add code below within the the print_results function. 
#       Notice that this function doesn't return anything because it prints 
#       a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    """
    # Print a header for the results summary
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))

    # Print the number of Not-Dog images
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Print out all statistics that are percentages
    print("\nStatistics (percentages):")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):  # Only print percentage statistics
            print("{:20}: {:5.1f}%".format(key, value))

    # Check if we need to print incorrectly classified dogs
    if print_incorrect_dogs and (results_stats_dic['n_images'] != 
        (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']))):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        for key, value in results_dic.items():
            # Check for misclassified dogs (either as dogs or non-dogs)
            if (value[3] == 1 and value[4] == 0) or (value[3] == 0 and value[4] == 1):
                print(f"Pet Image Label: {value[0]:>20}, Classifier Label: {value[1]:>20}")

    # Check if we need to print incorrectly classified breeds
    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nINCORRECT Dog Breed Assignments:")

        for key, value in results_dic.items():
            # Check if the breed was misclassified
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print(f"Real: {value[0]:>26}   Classifier: {value[1]:>30}")