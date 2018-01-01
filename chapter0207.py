#!/usr/bin/env python3
import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#?P<my_pattern_group>라는 메타문자는  <my_pattern_group>이라는 그룹에 포함되어 있는
#하위 문자열을 찾아내 필요한 경우에 화면에 출력하거나 파일에 기록할 수 있게 해준다.
#우리가 찾는 ^001-.* 이다 캐릿(^)은 문자열이 시작하는 경우 패턴만 검색하는 특수 문자다.
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
                print(row_list)

## command line
## python3 chapter0207.py ./files/sample_data.csv ./files/pandas_data_0207.csv
