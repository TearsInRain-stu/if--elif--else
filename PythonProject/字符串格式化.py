dollars = 1000
name = "王大锤"
salary = 100

message = "我是" + name +",钱包有" + str(dollars) + "元,但是今天发放了工资" + str(float(salary)) + "元，目前钱包有" + str(dollars + salary) + "元."
print(message)

dollars1 = 1000
name1 = "王大锤"
salary1 = 100

message = "我是%s 钱包有%s元,但是今天发放了工资%s元，目前钱包有%s元."%(name1,dollars1,salary1,salary1 + dollars1)
print(message)
print("-"*20)

# 数字精度控制
"""
   .n 控制小数点精度，要求是数字，会进行小数的四舍五入
"""

num = 3.435
print("%3.6f" %num)
num2 = 3.4559
print("%.3f" %num2)

my_money = 120.5
your_money = 12
print("%3.2f" %my_money)
print("%6.2f" %your_money)