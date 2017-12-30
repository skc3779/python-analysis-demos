# 숫자 시퀀스의 평균 계산하기

def getMean(numericValues):
    return sum(numericValues)/len(numericValues)

my_list2 = []

# 짧은 버전
try:
    print("Output #137: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("Oupput #137: (Error): {}".format(float('nan')))
    print("Oupput #137: (Error): {}".format(detail))


# 긴 버전
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("Oupput #138: (Error): {}".format(float('nan')))
    print("Oupput #138: (Error): {}".format(detail))
else:
    print("Oupput #138: (The mean is): {}".format(result))
finally:
    print("Oupput #138: (Finally): The finally block is executed every time")