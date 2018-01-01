#!/usr/bin/env python3
import pandas as pd
import sys

#pandas를 활용
#열의 헤더를 사용하여 특정 열을 선택하는 방법
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

data_frame_column_by_name.to_csv(output_file, index=False)

## command line
## python3 chapter0212.py ./files/sample_data.csv ./files/pandas_data_0212.csv
