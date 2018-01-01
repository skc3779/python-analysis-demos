#!/usr/bin/env python3
import csv
import sys

# 열 헤더를 추가하기
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ['Supplier Name', 'Invoice Number', \
                       'Part Number', 'Cost', 'Purchase Date', 'User Name']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow (row)

## command line
## python3 chapter0215.py ./files/sample_data_noheader.csv ./files/pandas_data_0215.csv
