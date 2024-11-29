#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                   
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

#       Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    """
    Retrieves and processes the three command line arguments that the user provides 
    when running the program from the terminal. This function utilizes Python's 
    argparse module to define and manage the command line arguments. If the user 
    does not supply some or all of these arguments, the function will use default 
    values for the missing ones.
    
    Command Line Arguments:
      1. --dir: Directory containing the images (default 'pet_images')
      2. --arch: CNN model architecture to use (default 'vgg'; options: 'vgg', 'alexnet', 'resnet')
      3. --dogfile: File containing the list of dog names (default 'dognames.txt')
    
    This function returns an ArgumentParser object containing the parsed arguments.

    Parameters:
     None - This function uses argparse to collect and store the command line arguments.
    
    Returns:
     parser.parse_args() - Returns a Namespace object that contains the parsed command line arguments.  
    """
    # Initialize ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add command line arguments
    parser.add_argument('--dir', type=str, default='pet_images', 
                        help='Directory path where pet images are located')
    parser.add_argument('--arch', type=str, choices=['vgg', 'alexnet', 'resnet'], 
                        default='vgg', help='The CNN model architecture to use for classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='Path to the file containing a list of dog names')

    # Parse and return the arguments
    return parser.parse_args()

