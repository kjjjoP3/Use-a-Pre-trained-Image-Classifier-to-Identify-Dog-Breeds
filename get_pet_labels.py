#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os

#  2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Builds a dictionary of pet labels (results_dic) based on the filenames 
    of the image files. The filenames contain the true identity of the pet 
    in the image, which is used to check the accuracy of the classifier's labels. 
    Ensure that pet labels are in lowercase and without leading or trailing spaces.
    (Example: filename = 'Boston_terrier_02259.jpg' -> Pet label = 'boston terrier')
    
    Parameters:
     image_dir - The full path to the folder containing images to be classified (string)
    
    Returns:
      results_dic - A dictionary where:
        - Key: Image filename (string)
        - Value: List containing the pet label (string) at index 0
    """
    # Initialize the results dictionary
    results_dic = {}

    # Check if the given directory exists
    if not os.path.isdir(image_dir):
        print(f"Directory '{image_dir}' not found!")
        return results_dic

    # Iterate over each file in the directory
    for filename in os.listdir(image_dir):
        if not filename.startswith('.'):  # Skip hidden files (e.g., .DS_Store)

            # Split the filename from its extension
            file_name, file_extension = os.path.splitext(filename)

            # Only process image files (jpg, jpeg, png, gif)
            if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                
                # Convert the filename to lowercase and replace underscores with spaces
                pet_label = ' '.join([word.lower() for word in file_name.split('_') if word.isalpha()])

                # Store the filename and its corresponding pet label in the dictionary
                results_dic[filename] = [pet_label]

    return results_dic