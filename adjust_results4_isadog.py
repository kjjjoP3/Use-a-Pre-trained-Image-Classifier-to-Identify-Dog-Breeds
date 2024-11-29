#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
#  4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Cập nhật từ điển kết quả để xác định liệu nhãn hình ảnh có phải là chó hay không,
    và liệu nhãn của trình phân loại có xác định đúng là chó hay không. Điều này
    giúp kiểm tra khả năng phân loại đúng hình ảnh là chó ngay cả khi sai giống.

    Tham số:
      results_dic - Từ điển với 'key' là tên tệp hình ảnh và 'value' là danh sách:
                    index 0 = nhãn của hình ảnh (chuỗi)
                    index 1 = nhãn của trình phân loại (chuỗi)
                    index 2 = 1/0 (int), 1 = khớp nhãn, 0 = không khớp
                ------ Chỉ số 3 & 4 sẽ được thêm bởi hàm này ------
                 MỚI - index 3 = 1/0 (int), 1 = nhãn hình ảnh là chó,
                            0 = nhãn hình ảnh không phải chó.
                 MỚI - index 4 = 1/0 (int), 1 = trình phân loại xác định là chó,
                            0 = trình phân loại xác định không phải chó.
     dogfile - Tệp văn bản chứa tên của các giống chó, mỗi dòng một tên, tất cả
               đều viết thường. (chuỗi - tên tệp)
    Trả về:
           Không trả về - `results_dic` được cập nhật trực tiếp.
    """
    # Tạo tập hợp chứa các tên giống chó hợp lệ từ tệp
    dog_names_set = set()
    with open(dogfile, 'r') as file:
        for dog_name in file:
            dog_names_set.add(dog_name.strip().lower())

    # Duyệt qua từng mục trong results_dic và thêm các thông tin mới
    for key, values in results_dic.items():
        # Kiểm tra nhãn của hình ảnh có phải là chó không
        pet_is_dog = 1 if values[0] in dog_names_set else 0
        # Kiểm tra nhãn của trình phân loại có phải là chó không
        classifier_is_dog = 1 if values[1] in dog_names_set else 0
        # Cập nhật kết quả vào từ điển
        values.extend([pet_is_dog, classifier_is_dog])
