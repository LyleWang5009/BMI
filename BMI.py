weight = input('请输入你的体重(kg): ')
height = input('请输入你的身高(m): ')
weight = float(weight)
height = float(height)
BMI = weight / (height ** 2)
print('你的BMI值为', BMI)
if BMI < 18.5:
	print('体重过轻')
elif BMI >= 18.5 and BMI < 24:
	print('正常范围')
elif BMI >= 24 and BMI < 27:
	print('过重')
elif BMI >= 27 and BMI < 30:
	print('轻度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
else:
	print('重度肥胖')