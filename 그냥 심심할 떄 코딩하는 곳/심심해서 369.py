# 숫자에 3, 6, 9가 포함 될 떄 그 숫자를 출력하지 않고 "짝!"을 출력한다.
arr = []
for i in range(1, 101):
    arr.append(i)

for i in range(100):
    if arr[i]%10 == 3 or arr[i]%10 == 6 or arr[i]%10 == 9:
        arr[i] = '짝'
print(arr)