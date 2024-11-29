#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
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
from get_pet_labels import get_pet_labels
import os

#       Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    The classifier labels should be formatted to match pet image labels:
    converted to lowercase and stripped of any leading or trailing spaces.
    
    Parameters: 
      images_dir - Full path to the folder of images to be classified (string).
      results_dic - Dictionary with image filename as the key and a list as value:
                    - index 0: pet image label (string)
                    - index 1: classifier label (string, added by this function)
                    - index 2: 1/0 indicating if the labels match (int)
      model - CNN model architecture used by the classifier function ('resnet', 'alexnet', 'vgg')
      
    Returns:
      None - The results_dic is updated in place. 
    """
    # Retrieve pet labels for each image in the directory
    filenames = get_pet_labels(images_dir)
    
    print("------------------< PREDICT >---------------------")
    
    # Loop through each image and its corresponding pet label
    for image_filename, values in filenames.items():
        # Construct the full image path
        img_path = os.path.join(images_dir, image_filename)
        
        # Get the pet label from results_dic (defaulting to None if not found)
        pet_label = results_dic.get(image_filename, [None])[0]
        
        # Classify the image and standardize the classifier label
        classifier_label = classifier(img_path, model)
        classifier_label = classifier_label.lower().strip()
        
        # Compare the pet label with the classifier label
        if pet_label in classifier_label:
            results_dic[image_filename].extend([classifier_label, 1])
        else:
            results_dic[image_filename].extend([classifier_label, 0])
        
        # Print the updated results dictionary (optional debugging step)
        print(results_dic)
    
    print("---------------------< END PREDICT >-------------------------") 