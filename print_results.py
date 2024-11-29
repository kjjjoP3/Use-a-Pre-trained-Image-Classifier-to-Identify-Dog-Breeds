#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
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
#  6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints a summary of classification results, and optionally prints incorrectly
    classified dog images and breeds based on user input.
    
    Parameters:
      results_dic - Dictionary containing image filenames as keys and lists as values.
                    List format: [pet label, classifier label, is correct (0 or 1), is dog (0 or 1), classifier dog (0 or 1)]
      results_stats_dic - Dictionary of statistics, where keys are statistic names and values are the results.
      model - CNN model architecture (e.g., 'resnet', 'alexnet', 'vgg').
      print_incorrect_dogs - Boolean flag to indicate whether to print misclassified dog images.
      print_incorrect_breed - Boolean flag to indicate whether to print misclassified dog breeds.
    
    Returns:
      None - Prints results directly to the console.
    """
    # Display the overall results for the classification run
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    print(f"{'N Images':<20}: {results_stats_dic['n_images']:>3d}")
    print(f"{'N Dog Images':<20}: {results_stats_dic['n_dogs_img']:>3d}")
    
    # Display the count of images that are not dogs
    print(f"{'N Not-Dog Images':<20}: {results_stats_dic['n_notdogs_img']:>3d}")
    print("")

    # Print the percentages for each key in the results_stats_dic that starts with 'p'
    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            print(f"{key:<20}: {value:.2f}%")

    # If incorrect dog classification is to be printed
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        
        # Loop through the results and print incorrectly classified dogs
        for key in results_dic:
            # Check for misclassifications where pet is a dog but classified as not a dog or vice versa
            if (results_dic[key][3] == 1 and results_dic[key][4] == 0) or (results_dic[key][3] == 0 and results_dic[key][4] == 1):
                print(f"Real: {results_dic[key][0]:>30}   Classifier Label: {results_dic[key][1]:>30}")
    
    # If incorrect breed classification is to be printed
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        
        # Loop through results and print incorrectly classified dog breeds
        for key in results_dic:
            # Check if the dog was correctly classified as a dog but its breed was misclassified
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print(f"Real: {results_dic[key][0]:>26}   Classifier Label: {results_dic[key][1]:>30}")