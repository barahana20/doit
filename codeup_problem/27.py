items = input().split('.')

items.reverse()
print("%02d-%02d-%04d"%(int(items[0]), int(items[1]), int(items[2])))
