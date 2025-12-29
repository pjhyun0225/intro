# password.py
import re

def is_valid_password(password: str) -> bool:
    """
    비밀번호 규칙:
    1. 최소 6자
    2. 알파벳 1개 이상
    3. 숫자 1개 이상
    4. 특수문자 1개 이상
    """

    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{6,}$'
    return bool(re.match(pattern, password))
