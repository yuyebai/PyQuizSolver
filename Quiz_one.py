#python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np
result = random.randint(10,20)
res = np.random.randn(5)
ret = random. random()
print("正整数",result)
print("5个随机小数",res)
print("0-1个随机小数",ret)