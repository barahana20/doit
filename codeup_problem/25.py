items = input()

items_list = list(items)
result = []
for i in range(5):
    result.append(int(items_list[i])*(10**(4-i)))

for i in range(5):
    print('['+str(result[i])+']')
