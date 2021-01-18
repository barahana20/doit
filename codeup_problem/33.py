i = input()

i_hex = hex(int(i))

list_i_hex = list(i_hex)
glue_list_i_hex= ''.join(list_i_hex[2:])
glue_list_i_hex_upper = glue_list_i_hex.upper()
print(glue_list_i_hex_upper)