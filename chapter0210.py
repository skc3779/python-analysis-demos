#!/usr/bin/env python3
import pandas as pd
import sys

# 선택된 컬럼만 필터링 하기
# pandas를 활용
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]

data_frame_column_by_index.to_csv(output_file, index=False)

## command line
## python3 chapter0210.py ./files/sample_data.csv ./files/pandas_data_0210.csv
