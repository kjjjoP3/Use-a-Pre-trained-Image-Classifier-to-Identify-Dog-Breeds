#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function get_pet_labels that creates the pet labels from the image's
#          filename. This function inputs: 
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
from os import listdir

#       EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with for the get_pet_labels function 
#       Please be certain to replace None in the return statement with 
#       results_dic dictionary that you create with this function
# 
def get_pet_labels(image_dir):
    """
    Generates a dictionary of pet labels (results_dic) based on the filenames 
    of the image files. These labels are used to assess the accuracy of the labels 
    returned by the classifier function, as the filenames contain the true identity 
    of the pet in the image. The pet labels are formatted in lowercase with no leading 
    or trailing spaces.
    
    Example:
      filename = 'Boston_terrier_02259.jpg' => Pet label = 'boston terrier'
    
    Parameters:
     image_dir - Full path to the directory containing images to be classified (string)
    
    Returns:
      results_dic - Dictionary where:
        - Key: Image filename (string)
        - Value: List containing:
          - Index 0: Pet image label (string)
    """
    # Retrieve list of files from the directory
    in_files = listdir(image_dir)
    
    # Create an empty dictionary to store the pet labels
    results_dic = dict()
   
    # Loop through each file in the directory to extract the pet label from the filename
    for file_name in in_files:
       
       # Skip files that start with '.' (e.g., system files)
       if not file_name.startswith("."):
           
           # Initialize an empty string to hold the pet label
           pet_label = ""

           # Extract pet label by splitting the filename and selecting the breed name part
           # Assuming the label is the first part of the filename (before any numbers or extension)
           # Remove any non-alphabetic characters and convert to lowercase
           pet_label = ' '.join([word.lower() for word in file_name.split('_')[:-1] if word.isalpha()])
           
           # If the filename is not in the results_dic, add it with the pet label
           if file_name not in results_dic:
              results_dic[file_name] = [pet_label]
           else:
               print(f"** Warning: Duplicate file found: {file_name}")
 
    # Return the results dictionary with pet labels
    return results_dic