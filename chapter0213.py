#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 불필요한 머리말과 꼬리말 정보가 포함된 데이터 처리하기
row_counter = 0
with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1

## command line
## python3 chapter0213.py ./files/sample_data_unnecessary.csv ./files/pandas_data_0213.csv
