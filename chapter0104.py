import sys
import glob
import os

# command line
# python chapter0104.py ./files

# 다수의 파일 읽기

print("Output #141:")
inputPath = sys.argv[1]

for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
    with open(input_file, 'rt', newline='', encoding='utf-8') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))