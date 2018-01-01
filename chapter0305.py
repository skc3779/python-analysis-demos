#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# Sale Amount열의 값이 1400.00 보다 큰 모든 행을 원한다는 뜻.

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
data_frame_value_meets_condition = \
	data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_13_output', index=False)
writer.save()

## command line
## python3 chapter0304.py ./files/sales_2013.xlsx ./files/pandas_data_0304.xls
