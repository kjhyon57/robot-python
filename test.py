import random

# 3 6 9ㅇㅇ


# 사용자는 input() 함수를 통해 해당 숫자 혹은 3. 6. 9 가 들어가는 곳에서는 "짝"을 입력해야 함.

def user_input():
  return input("사용자 차례: ")

def check_369(number):
  number = str(number)
  clap_count = 0
  for i in range(len(number)):
    if number[i] == "3" or number[i] == "6" or number[i] == "9":
      clap_count += 1

  return clap_count

def check_correct(now_number, answer):
  clap = check_369(now_number)
  if clap:
    if answer == '짝'*clap:
      print("")
      return True

    else:
      return False
  else:
    return now_number == answer

def change_computer_answer(number):
  clap = check_369(number)
  if clap:
    return "짝"*clap
  else:
    return number

print("시작")
user_turn = True
for now_number in range(1,100):
  now_number = str(now_number)
  if user_turn:
    user_answer = user_input()
    if not check_correct(now_number, user_answer):
      print("패배")
      break
    user_turn = False
  else:
    computer_answer = change_computer_answer(now_number)
    print("컴퓨터 차례 : ", computer_answer)
    user_turn = True