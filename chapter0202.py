#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# csv 모듈을 이용한 파싱 처리.

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        for row_list in filereader:
            filewriter.writerow(row_list)
            print(row_list)




## command line
## python3 chapter0202.py ./files/sample_data.csv ./files/pandas_data.csv