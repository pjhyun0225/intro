# echo.py
from password import is_valid_password

while True:
    password = input("비밀번호를 입력하세요 (! 입력 시 종료): ")

    if password == '!':
        print("프로그램을 종료합니다.")
        break

    if is_valid_password(password):
        print("사용 가능한 비밀번호입니다.")
    else:
        print("비밀번호 조건을 만족하지 않습니다.")
