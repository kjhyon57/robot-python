# 3 6 9 게임

'''
1씩 숫자가 증가하는데 해당 차례의 숫자에 3, 6, 9 가 없으면 숫자를 입력하고,
숫자에 3, 6, 9 가 있으면 그 갯수만큼 "짝"을 입력해야 함.
'''
# 사용자가 숫자를 입력하는 메소드 정의
def user_input():
    return input("사용자 차례: ")

# (사용자던, 컴퓨터이던) 차례숫자에 369가 들어가 있는지, 갯수가 몇개인지 확인하는 메소드 정의
def check_369(number):
    clap = check_369(number)
    if clap:

# (사용자던, 컴퓨터이던)차례숫자와 입력숫자의 동일여부 확인하는 메소드 정의

 
# 컴퓨터 차례숫자에 입력할 숫자 또는 짝 숫자를 부여하는 메소드 정의


#게임 시작 및 숫자를 하나씩 증가하며 사용자와 컴퓨터가 입력숫자를 부여하는 프로그램 작성 
print("시작")
user_turn = True
#사용자가 숫자를 입력하게 하고 차례숫자와 입력숫자를 비교한 확인결과를 반환하는 프로그램
for number in (1, 100)
    number = str(number)
    if user_turn:
        answer = user_input()
        if not check_correct(number, answer):
            print("패배")
            break
        else:
            user_turn = False
#컴퓨터 입력숫자를 표시하는 프로그램
    else:
        computer_answer = check_computer_answer(number)
        print("컴퓨터 차례: ", computer_answer)
        user_turn = True