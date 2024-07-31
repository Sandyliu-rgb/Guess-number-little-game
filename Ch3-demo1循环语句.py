# """
# 演示while循环的基础应用
# """
# i = 0
# while i < 100:
#     print("sitar vv, I Love You.")
#     i += 1
# print("有情人，终成眷属")
#
# # 求1-100的和
# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)

"""
设置一个1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
-无限次机会，知道猜中为止
-每一次猜不中，会提示大了或者小了
-猜完数字后，提示猜了几次
"""

import random
num = random.randint(1, 100)
# 定义一个变量，记录总共猜测多少次
count = 0

# 通过一个bool类型的变量， 做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("Please input the number you guess"))
    count += 1
    if guess_num == num:
        print("right!")
        # 设置False就是一个终止循环的条件
        flag = False
    else:
        compare = "guess larger" if (guess_num > num) else "guess smaller"
        print(compare)
print(f"You do {count} guess totally")

