#!/usr/bin/env python3
import csv
import glob
import os
import sys

#여러개의 데이터 합치기
input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
		with open(output_file, 'a', newline='', encoding="utf-8") as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row)

## command line
## python3 chapter0218.py ./files/ ./files/pandas_data_0218.csv