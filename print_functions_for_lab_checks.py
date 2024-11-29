#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 05/14/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"
#
def check_command_line_arguments(args):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments passed in as parameter in_arg, 
    assumes you defined all three command line arguments as outlined in 
    '7. Command Line Arguments'
    Parameters:
     in_arg -data structure that stores the command line arguments object
    Returns:
     Nothing - just prints to console  
    """
    if not args:
        print("* Command Line Arguments not checked because 'get_input_args' is missing.")
    else:
        print(f"Command Line Arguments:\n    Directory: {args.dir}\n    Architecture: {args.arch}\n    Dog File: {args.dogfile}")

def check_creating_pet_image_labels(results):
    """    
    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints the first 10 key-value pairs and ensures that there are 40 entries in 
    the 'results' dictionary. This assumes the results are as described in 
    '9/10. Creating Pet Image Labels'
    Parameters:
      results - Dictionary where the key is image filename and value is a List 
             idx 0 = pet image label (string)
    Returns:
     None - only prints to the console  
    """
    if results is None:
        print("* Pet Image Labels not verified because 'get_pet_labels' was not defined.")
    else:
        # Limit the printed results to the first 10 entries or fewer if less than 10
        print(f"\nPet Image Label Dictionary has {len(results)} key-value pairs.")
        print("Below are up to the first 10:")
        
        for index, (key, value) in enumerate(results.items()):
            if index >= 10:
                break
            print(f"{index + 1:2d} Key: {key:>30}  Label: {value[0]:>26}")


def check_classifying_images(results):
    """    
    For Lab: Classifying Images - 11/12. Classifying Images
    Displays Pet Image Label and Classifier Label for matches followed by mismatches.
    Then it prints the total number of images processed, the count of matches, and 
    mismatches to ensure all 40 images were processed. 
    Parameters:
      results - Dictionary where key is image filename and value is a List 
             idx 0 = pet image label (string)
             idx 1 = classifier label (string)
             idx 2 = 1/0 (int) 1 for match, 0 for no match
    Returns:
     None - prints to the console  
    """
    if results is None:
        print("* Image classification results are missing because 'classify_images' was not defined.")
    else:
        match_count = sum(1 for v in results.values() if v[2] == 1)
        mismatch_count = sum(1 for v in results.values() if v[2] == 0)

        print("\n     MATCHES:")
        for key, value in results.items():
            if value[2] == 1:
                print(f"\n{key:>30}: \nReal Label: {value[0]:>26}   Classifier Label: {value[1]:>30}")

        print("\n     MISMATCHES:")
        for key, value in results.items():
            if value[2] == 0:
                print(f"\n{key:>30}: \nReal Label: {value[0]:>26}   Classifier Label: {value[1]:>30}")

        print(f"\n# Total Images: {match_count + mismatch_count}, # Matches: {match_count}, # Mismatches: {mismatch_count}")

 
def check_classifying_labels_as_dogs(results):
    """    
    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet and Classifier Labels, whether each is classified as a dog (1=Yes, 0=No)
    for both matches and mismatches, followed by the total number of images processed 
    and counts of matches and mismatches. 
    Parameters:
      results - Dictionary where key is image filename and value is a List 
             idx 3 = Pet Label Dog (1=Yes, 0=No)
             idx 4 = Classifier Label Dog (1=Yes, 0=No)
    Returns:
     None - prints to the console  
    """
    if results is None:
        print("* Dog classification results not checked due to missing 'adjust_results4_isadog'.")
    else:
        match_count = sum(1 for v in results.values() if v[2] == 1)
        mismatch_count = sum(1 for v in results.values() if v[2] == 0)

        print("\n     MATCHES:")
        for key, value in results.items():
            if value[2] == 1:
                print(f"\n{key:>30}: \nReal Label: {value[0]:>26}   Classifier Label: {value[1]:>30}  "
                      f"Pet is a Dog: {value[3]:1d}  Classifier is a Dog: {value[4]:1d}")

        print("\n     MISMATCHES:")
        for key, value in results.items():
            if value[2] == 0:
                print(f"\n{key:>30}: \nReal Label: {value[0]:>26}   Classifier Label: {value[1]:>30}  "
                      f"Pet is a Dog: {value[3]:1d}  Classifier is a Dog: {value[4]:1d}")

        print(f"\n# Total Images: {match_count + mismatch_count}, # Matches: {match_count}, # Mismatches: {mismatch_count}")



def check_calculating_results(results, stats):
    """    
    For Lab: Classifying Images - 14. Calculating Results
    Compares calculated results against the 'stats' dictionary.
    Displays both calculated values and pre-calculated values from 'results_stats_dic'.
    Parameters:
      results - Dictionary of image results (labels and classification info)
      stats - Statistics dictionary that contains calculated percentages and counts
    Returns:
     None - prints to the console  
    """
    if stats is None:
        print("* Results statistics not verified because 'calculates_results_stats' was not defined.")
    else:
        image_count = len(results)
        pet_dog_count = sum(1 for v in results.values() if v[3] == 1)
        classifier_dog_count = sum(1 for v in results.values() if v[4] == 1)

        correct_dog_pct = (classifier_dog_count / pet_dog_count) * 100
        correct_not_dog_pct = ((image_count - pet_dog_count) / (image_count - pet_dog_count)) * 100
        correct_breed_pct = (sum(1 for v in results.values() if v[2] == 1 and v[3] == 1 and v[4] == 1) / pet_dog_count) * 100

        print(f"\n ** Statistics from 'calculates_results_stats()' function:")
        print(f"Images Processed: {image_count}, Dog Images: {pet_dog_count}, Classifier Dogs: {classifier_dog_count}")
        print(f"Correct Dog Percentage: {correct_dog_pct:.2f}%")
        print(f"Correct Non-Dog Percentage: {correct_not_dog_pct:.2f}%")
        print(f"Correct Breed Match Percentage: {correct_breed_pct:.2f}%")
