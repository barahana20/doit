# 숫자에 3, 6, 9가 포함 될 떄 그 숫자를 출력하지 않고 "짝!"을 출력한다.
# arr = []
# for i in range(1, 101):
#     arr.append(i)

for i in range(1, 100, 1):
    a = i%10
    b = i//10
    if  a%3==0 and a!=0 or b%3==0 and b!=0:
        print('짝', end=' ')
    else:
        print(i, end=' ')