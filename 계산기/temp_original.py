import sys


class Cal:
    def __init__(self):
        self.result = 0

    # 입력 받는 함수
    def input(self):
        input1 = input("입력 : ")  # '1 + 2 =' 을 입력(예시)
        self.result = input1
        # print(self.result)
    # 계산 함수

    def calculate(self):
        try:
            result = []
            for i in self.result:
                #(0 if i == '' else(0 if i == '=' else(result.append('+') if i == '+' \
                # else(result.append('-') if i == '-' else(result.append('/') if i == '/' \
                # else(result.append('(') if i == '(' else(result.append(')') if i == ')' \
                # else(result.append(i) if i.isdigit() == True else(0)))))))))
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
            print()
            print("*"*30)
            print('계산식 : ' + result + '=', end='')
            print(eval(result))
            print("*"*30)
            print()

        except SyntaxError:
            print("계산 기호가 아닌 문자를 입력하였습니다.")

    def start(self):
        print('='*30)
        print("계산기를 실행합니다.")
        print('='*30)

    def end(self):
        print("계산기를 종료합니다.")
        sys.exit(0)


def retry():
    Cal1 = Cal()
    while(True):
        input1 = input("다시 사용하시겠읍니까?(Y/N) : ")
        if input1 == 'Y' or input1 == 'y':
            print("네~ 다시 띄워드렸습니다.")
            break
        elif input1 == 'N' or input1 == 'n':
            Cal1.end()
        else:
            print("다른 문자를 입력하였습니다.")
            continue


while(True):
    Cal1 = Cal()

    Cal1.start()

    Cal1.input()

    Cal1.calculate()

    retry()
