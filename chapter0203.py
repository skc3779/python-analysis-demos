#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			cost = str(row_list[3]).strip('$').replace(',', '')
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				filewriter.writerow(row_list)
				print(row_list)


## command line
## python3 chapter0203.py ./files/sample_data.csv ./files/pandas_data_0203.csv