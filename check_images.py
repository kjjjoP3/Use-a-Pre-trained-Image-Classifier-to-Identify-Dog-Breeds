#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py

# PROGRAMMER: ThanhBT29
# DATE CREATED: 06/09/2023
# REVISED DATE: 06/09/2023
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.

from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    # Đo thời gian bắt đầu thực thi chương trình
    start_time = time()

    # Nhận các tham số dòng lệnh do người dùng nhập
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)

    # Tạo nhãn cho ảnh từ tên file và lưu vào dictionary `results`
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

    # Sử dụng mô hình CNN để phân loại ảnh và cập nhật kết quả vào `results`
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)

    # Điều chỉnh kết quả để xác định các ảnh là chó hay không
    adjust_results4_isadog(results, in_arg.dogfile)
    check_classifying_labels_as_dogs(results)

    # Tính toán các số liệu thống kê từ kết quả
    results_stats = calculates_results_stats(results)
    check_calculating_results(results, results_stats)

    # In kết quả cuối cùng và các thông tin liên quan
    print_results(results, results_stats, in_arg.arch, True, True)

    # Tính tổng thời gian thực thi và hiển thị
    total_runtime = time() - start_time
    runtime_h, runtime_m, runtime_s = int(total_runtime // 3600), int((total_runtime % 3600) // 60), int(total_runtime % 60)
    print(f"\n** Total Elapsed Runtime: {runtime_h}:{runtime_m}:{runtime_s}")

# Gọi hàm `main` để chạy chương trình
if __name__ == "__main__":
    main()
