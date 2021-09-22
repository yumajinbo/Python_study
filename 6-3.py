start=int(input('開始:1'))
end=int(input('終了:100'))
step=int(input('増分:1'))

for count in range(start,end,step):
    print(count,end='')
    print()