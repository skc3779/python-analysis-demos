#!/usr/bin/env python3
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# pandas를 활용
# 불필요한 머리말과 꼬리말 정보가 포함된 데이터 처리하기

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))

data_frame.to_csv(output_file, index=False)

## command line
## python3 chapter0214.py ./files/sample_data_unnecessary.csv ./files/pandas_data_0214.csv
