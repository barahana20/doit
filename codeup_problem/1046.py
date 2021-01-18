i = input().split(' ')
result = 0

for idx in i:
    result += int(idx)
print(result)
print("%.1f"%(result/3))