<<<<<<< Updated upstream
def user_input():
  return input("사용자 차례: ")
# 사용자로부터 입력을 받는 함수를 정의합니다.
# 사용자에게 입력을 요청하고, 입력된 값을 반환합니다.

def check_369(number):
  number = str(number)
  clap_count = 0
  for i in range(len(number)):
    if number[i] == "3" or number[i] == "6" or number[i] == "9":
      clap_count += 1
=======




# 사용자로부터 입력을 받는 함수를 정의합니다.
# 사용자에게 입력을 요청하고, 입력된 값을 반환합니다.



>>>>>>> Stashed changes
# 주어진 숫자에 3, 6, 9가 포함되어 있는지 확인하는 함수를 정의합니다.
# 숫자를 문자열로 변환합니다.
# 박수 횟수를 저장할 변수를 초기화합니다.
# 숫자의 각 자릿수를 순회합니다.
# 현재 자릿수가 3, 6, 9 중 하나인지 확인합니다.
# 조건에 맞다면 박수 횟수를 증가시킵니다.
# 최종 박수 횟수를 반환합니다.

<<<<<<< Updated upstream
  return clap_count
=======




>>>>>>> Stashed changes
# 사용자의 답변과 현재 숫자가 일치하는지 확인하는 함수를 정의합니다.
# 현재 숫자에 3, 6, 9가 포함된 횟수를 계산합니다.
# 3, 6, 9가 포함된 경우
# 사용자의 답변이 '짝'을 박수 횟수만큼 반복한 것과 일치하는지 확인합니다.
# 3, 6, 9가 포함되지 않은 경우, 사용자의 답변과 현재 숫자가 일치하는지 확인합니다.

<<<<<<< Updated upstream
def check_correct(now_number, answer):
  clap = check_369(now_number)
  if clap:
    if answer == '짝'*clap:
      print("")
      return True
=======

>>>>>>> Stashed changes
# 컴퓨터의 답변을 생성하는 함수를 정의합니다.
# 현재 숫자에 3, 6, 9가 포함된 횟수를 계산합니다.
# 3, 6, 9가 포함된 경우
# '짝'을 박수 횟수만큼 반복한 문자열을 반환합니다.
# 3, 6, 9가 포함되지 않은 경우, 현재 숫자를 그대로 반환합니다.


# 게임 시작을 알리는 메시지를 출력합니다.
# 사용자의 차례인지 여부를 나타내는 변수를 초기화합니다.

<<<<<<< Updated upstream
def change_computer_answer(number):
  clab = check_369(number)
  if clab:

print("시작")
user_turn = True
for now_number in range(28,100):
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
    user_turn = True# 28부터 99까지의 숫자를 순회합니다.
=======

# 28부터 99까지의 숫자를 순회합니다.
>>>>>>> Stashed changes
# 현재 숫자를 문자열로 변환합니다.
# 사용자의 차례인 경우
# 사용자로부터 답변을 입력받습니다.
# 사용자의 답변이 올바른지 확인합니다.
# 답변이 틀렸다면 패배 메시지를 출력하고 게임을 종료합니다.
# 다음 차례는 컴퓨터의 차례로 설정합니다.
# 컴퓨터의 답변을 생성합니다.
# 컴퓨터의 답변을 출력합니다.
# 다음 차례는 사용자의 차례로 설정합니다.