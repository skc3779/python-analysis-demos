#!/usr/bin/env python3
import pandas as pd
import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

# Purchase Date 가 ['1/20/14', '1/30/14'] 중 한 값을 포함하는 모든 행을 필터링 한다.
important_dates = ['1/20/14', '1/30/14']
with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date = row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
                print(row_list)


## command line
## python3 chapter0205.py ./files/sample_data.csv ./files/pandas_data_0205.csv
