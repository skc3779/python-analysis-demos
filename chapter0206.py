#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

#pandas를 사용해
#Purchase Date 가 ['1/20/14', '1/30/14'] 중 한 값을 포함하는 모든 행을 필터링 한다.
important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date']\
.isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)


## command line
## python3 chapter0206.py ./files/sample_data.csv ./files/pandas_data_0206.csv
