print("BMI値を求めます")
cm=float(input("身長(cm):"))
weight=float(input("体重(Kg):"))
height=cm/100
bmi=weight/(height*height)
print("BMI値=",bmi)