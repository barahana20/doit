i = input()

i_hex = hex(int(i))

list_i_hex = list(i_hex)

print(''.join(list_i_hex[2:]))