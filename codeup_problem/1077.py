i = int(input())
result = 0
for idx in range(i+1):
    if idx % 2 == 0:
        result += idx

print(result)
