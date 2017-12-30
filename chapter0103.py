import sys
import glob
import os

# command line
# python chapter0103.py ./files/input_text.txt

# READ A FILE
# Read a single text file
input_file = sys.argv[1]

## Read a text file (older method) ##
print("Output #141:")
filereader = open(input_file, 'rt', newline='', encoding='utf-8')

for row in filereader:
    print("{}".format(row.strip()))
filereader.close()


## 텍스트 파일읽기 (새 방식) ##
print("Output #141:")
with open(input_file, 'rt', newline='', encoding='utf-8') as filereader:
    for row in filereader:
        print("{}".format(row.split()))

