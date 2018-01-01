#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)

## command line
## python3 chapter0201.py ./files/sample_data.csv ./files/pandas_data.csv