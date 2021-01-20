import sys
import time


class Cal:
    def __init__(self):
        self.result = 0

    # 입력 받는 함수
    def input(self):
        input1 = input("입력 : ")  # '1 + 2 =' 을 입력(예시)
        self.result = input1
        # print(self.result)
    # 계산 함수
    def time_check(self):
        return time.strftime('%Y/%B/%d %H:%M:%S')
    def calculate(self):
        cal1 = Cal()
        f = open("cal_log.txt", 'a')
        try:
            result = []
            for i in self.result:
                if i == ' ':
                    pass
                elif i == '=':
                    pass
                elif i == '+':
                    result.append('+')
                elif i == '-':
                    result.append('-')
                elif i == '*':
                    result.append('*')
                elif i == '/':
                    result.append('/')
                elif i == '(':
                    result.append('(')
                elif i == ')':
                    result.append(')')
                elif i.isdigit() == True:
                    result.append(i)
                else:
                    raise SyntaxError

                
            result = ''.join(result)
            cal1.memo_save('[' + str(cal1.time_check()) + '] ' \
                + result + '=' + str(eval(result))) # 메모장에 계산한 내역 저장

            print()
            print("*"*30)
            print('계산식 : ' + result + '=', end='')
            print(eval(result))
            print("*"*30)
            print()
            f.write('\n') 

        except SyntaxError:
            f.write('[' + str(cal1.time_check()) + '] ')
            f.write(" !! 잘못된 값을 입력한 경우 보이지 않습니다 !! \n")
            print("계산 기호가 아닌 문자를 입력하였습니다.")
    
    # 메모장에 로그 저장
    def memo_save(self, *argvs):
        output = []
        f = open("cal_log.txt", 'a')
        for i in argvs:
            if i == '(':
                pass
            elif i == ')':
                pass
            elif i == ',':
                pass
            elif i == '\'':
                pass
            else: output.append(i)
        
        output_paste = ''.join(output)
        f.write(f'{output_paste}')
        
        f.close()

    def start(self):
        print('='*30)
        print("계산기를 실행합니다.")
        print('='*30)

    def end(self):
        print("계산기를 종료합니다.")
        sys.exit(0)


    def retry(self):
        while(True):
            input1 = input("다시 사용하시겠읍니까?(Y/N) : ")
            if input1 == 'Y' or input1 == 'y':
                print("네~ 다시 띄워드렸습니다.")
                break
            elif input1 == 'N' or input1 == 'n':
                print("계산기를 종료합니다.")
                sys.exit(0)
            else:
                print('please input y or n')
                continue

    

while(True):

    cal1 = Cal()
    
    cal1.start()

    cal1.input()

    cal1.calculate()

    cal1.retry()
