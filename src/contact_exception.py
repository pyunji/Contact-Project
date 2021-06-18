# contact_exception.py
import re
def valid_name(m: str):
    """이름을 validation하는 함수이다."""
    if not m:
        raise NoNameError()
    elif len(m)>10:
        raise TooLargeName()
def vaild_cellphone(m: str):
    """휴대폰 번호를 validation하는 함수이다."""
    CELLPHONE_RULE = re.compile('[0-9]{7,12}')
    if not m.isdigit():
        raise CellphoneError()
    elif not CELLPHONE_RULE.search(m):
        raise CellphoneError()
def valid_email(m: str):
    """이메일을 validation하는 함수이다."""
    EMAIL_RULE = re.compile('^[0-9a-zA-Z._-]+@[0-9a-zA-Z._-]+\.[0-9a-zA-Z._-]*\.*[0-9a-zA-Z._-]+$')
    if not EMAIL_RULE.search(m):
        raise EmailValid()
def valid_cls(m: str):
    """구분명을 validation하는 함수이다."""
    if not m:
        raise NoClsName()
    elif len(m)>20:
        raise TooLargeClsName()
class TooLargeName(Exception):
    """이름값에 길이 제한을 주는 예외이다."""
    def __str__(self):
        return "\n*이름을 10자 이내로 입력하세요."
class TooLargeClsName(Exception):
    """구분명에 길이제한을 주는 예외이다."""
    def __str__(self):
        return "\n*구분명을 20자 이내로 입력하세요."
class NoNameError(Exception):
    """공백이 들어올 때 발생하는 예외이다."""
    def __str__(self):
        return "\n*이름을 입력하세요. "
class CellphoneError(Exception):
    """전화번호에 숫자가 입력되지 않을 시 발생하는 예외이다."""
    def __str__(self):
        return f"\n*전화번호는 문자나 기호를 제외한 0부터 9까지의 숫자만 입력 가능합니다." \
               f"\n 연락처를 다시 확인하세요."
class EmailValid(Exception):
    """이메일에 정규식과 일치하지 않는 값이 들어올 시 발생하는 예외이다."""
    def __str__(self):
        return "\n*이메일주소를 다시 확인하세요."
class NoClsName(Exception):
    """공백이 들어올 때 발생하는 예외이다."""
    def __str__(self):
        return "\n*구분명을 입력하세요"

