# 첫 줄에 합
# 둘째 줄에 차,
# 셋째 줄에 곱,
# 넷째 줄에 몫,
# 다섯째 줄에 나머지,
# 여섯째 줄에 나눈 값을 순서대로 출력한다.
# (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)

i = input().split(' ')

add = eval(i[0] +"+"+ i[1])
sub = eval(i[0] +"-"+ i[1])
mul = eval(i[0] +"*"+ i[1])
div_share = eval(i[0] +"//"+ i[1])
div_remainder = eval(i[0] +"%"+ i[1])
div_div = eval(i[0] +"/"+ i[1])

print(add)
print(sub)
print(mul)
print(div_share)
print(div_remainder)
print("%.2f"%div_div)