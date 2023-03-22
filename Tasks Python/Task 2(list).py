my_list = [1,2,3,4,5,6,7,8,9,0]
print(my_list)
print(my_list[-2])
del my_list[8]
my_list.append('Python')
print(my_list)
# elem = my_list[9]
# print(elem[1::2])
print(my_list[-1][1::2])
import random
print(random.choice(my_list))