#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='', encoding='utf-8') as filereader:

	with open(output_file, 'w', newline='', encoding='utf-8') as filewriter:

		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filewriter.write(','.join(map(str,header_list))+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filewriter.write(','.join(map(str,row_list))+'\n')


# command line
# python chapter0106.py ./files/input_text.txt ./files/write2_text.txt

