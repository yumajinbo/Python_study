while True:
    n=int(input('nの値:'))
    if sum>0:
        break

sum=0
i=1
while i <= n:
        sum+=i
        i+=1
print('合計が100000を超えるnは',n,'です')