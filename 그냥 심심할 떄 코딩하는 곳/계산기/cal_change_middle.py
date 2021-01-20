import sys


class Cal:
    def __init__(self, x=0, y=0, symbol=''):
        self.x = x
        self.y = y
        self.symbol = symbol

    def calculate(self):
        if (self.symbol ==)

        except SyntaxError:
            print("계산 기호가 아닌 문자를 입력하였습니다.")

    def start(self):
        print('='*30)
        print("계산기를 실행합니다.")
        print('='*30)

    def end(self):
        print("계산기를 종료합니다.")
        sys.exit(0)

    def print(self):  # 두두등장
        print(f'{x} {symbol} {y} = 두둥')


while(True):  # 풀어드렸습니다~

    while(True):
        input1 = input("다시 사용하시겠읍니까?(Y/N) : ")  # 간단하게 수정해드리겠읍니다
        if input1 == 'Y' or 'y':
            print("네~ 다시 띄워드렸습니다.")
            break
        elif input1 == 'N' or 'n':
            Cal1.end()
        else:
            print("다른 문자를 입력하였습니다.")
            continue

    cal1 = Cal(1, 2, '-')
    cal1.start()
    cal1.print()
    cal.end()
