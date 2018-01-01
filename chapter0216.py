#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', \
'Part Number', 'Cost', 'Purchase Date', 'User Name']
data_frame = pd.read_csv(input_file, header=None, names=header_list)

data_frame.to_csv(output_file, index=False)
## command line
## python3 chapter0216.py ./files/sample_data_noheader.csv ./files/pandas_data_0216.csv
