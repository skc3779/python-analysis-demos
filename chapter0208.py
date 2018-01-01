#!/usr/bin/env python3

import pandas as pd
import sys

#001- 로 시작하는 필터링
#pandas를 이용한 방법
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number']\
.str.startswith("001-"), :]

data_frame_value_matches_pattern.to_csv(output_file, index=False)

## command line
## python3 chapter0208.py ./files/sample_data.csv ./files/pandas_data_0208.csv
