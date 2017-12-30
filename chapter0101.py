my_tuple = {'x','y','z'}
print("Output #93: {}".format(my_tuple))

# 할당 연산자(=)의 왼편에 튜풀을 풀기.
one, two, tree = my_tuple
print("Oupput #97 : {0} {1} {2}".format(one, two, tree))

# 중괄호를 이용하여 딕셔너리 생성하기
a_dict = {'one':1, 'two':2, 'tree':3}
print("Output #102: {}".format(a_dict))

# 키를 사용하여 딕셔너리 내 특정 값에 접근하기
print("Output #106: {}".format(a_dict['two']))

# copy() 함수를 이용하여 딕셔너리 사본 만들기
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))


# keys(), values(), items()를 사용하여
# 딕셔너리의 키, 값, 키-값 싸에 접근하기
print("Output #109 : {}".format(a_dict.keys()))
print("Output #110 : {}".format(a_dict.values()))
print("Output #111 : {}".format(a_dict.items()))

# 집합 축약을 이용하여 리스트의 고유한 튜플 집합을 고르기
my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]

set_of_tuple1 = {x for x in my_data}
print("Output #131 (set comprehension): {}".format(set_of_tuple1))

set_of_tuple2 = set(my_data)
print("Output #132 (set function): {}".format(set_of_tuple2))
