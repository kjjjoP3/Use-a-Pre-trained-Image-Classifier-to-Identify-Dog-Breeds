#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

#  3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with ": 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and updates the results dictionary.
    
    Parameters:
      images_dir - Path to folder of images (string)
      results_dic - Dictionary with image filenames as keys and a list as values:
                    index 0: pet image label (string)
                    index 1: classifier label (string, added by this function)
                    index 2: match indicator (int, 1 if match, 0 otherwise)
      model - CNN model architecture to use (string: 'resnet', 'alexnet', 'vgg')
      
    Returns:
      None - results_dic is updated in place.
    """
    for filename in results_dic:
        # Full image path
        image_path = f"{images_dir}/{filename}"
        
        # Get classifier label using the classifier function
        classifier_result = classifier(image_path, model)
        
        # Process classifier result to standardize: lowercasing and stripping
        model_label = classifier_result.lower().strip()
        
        # Extract pet label for comparison
        pet_label = results_dic[filename][0]
        
        # Determine if the pet label matches the classifier label
        match = 1 if pet_label in model_label else 0
        
        # Update the results dictionary
        results_dic[filename].extend([model_label, match])