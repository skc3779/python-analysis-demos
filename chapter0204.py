#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

# loc() 함수를 이용해 Supplier  Name 열의 값에 Z가 포함되거나 Cost열의 값이 600 보다 큰 모든 행을 필터링
# 조건으로 지정한다.
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)


## command line
## python3 chapter0204.py ./files/sample_data.csv ./files/pandas_data_0204.csv
