#!/usr/bin/env python3
#!/usr/bin/env python3
import csv
import sys

# 선택된 컬럼만 필터링 하기
input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            row_list_output = []
            for index_value in my_columns:
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)
            print(row_list_output)

## command line
## python3 chapter0209.py ./files/sample_data.csv ./files/pandas_data_0209.csv
