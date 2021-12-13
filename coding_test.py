weight = input('請輸入體重： ')
weight = float(weight)
height = input('請輸入身高： ')
height = float(height)
bmi = weight / (height * height / 100 * 100)
bmi = float(bmi)
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常範圍')
else:
    print('異常範圍')
 # bmi計算