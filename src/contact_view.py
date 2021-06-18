# contact_view.py
import contact_dto as cd

def menu_input():
    '''main menu를 사용자에게 보여준 후 번호를 입력받아 return해주는 함수이다.'''
    prompt = """
        ======================================
        다음 메뉴의 번호 중 하나를 선택하세요.
        ======================================
        1. 회원 추가
        2. 회원 목록 보기
        3. 회원 정보 수정하기
        4. 회원 삭제
        5. 종료
        """
    menu_input = input(prompt)
    return menu_input


def add_member(aom: str):
    '''사용자에게 등록할 회원의 연락처를 입력받아 dto에 setting한다.
    이 dto는 return된다.'''
    print(f"{aom}할 회원의 정보를 입력하세요.")
    dto = cd.ContactDTO()
    name = input('이름 : ').strip()
    dto.set_name(name)
    phone_num = input('전화번호 : ').strip()
    dto.set_phone_num(phone_num)
    email = input('e-mail : ').strip()
    dto.set_email(email)
    cls_name = input('구분 : ').strip()
    dto.set_cls_name(cls_name)
    return dto

def memlist(dto_list):
    '''model의 get_memlist()함수와 같이 쓰이는 함수이다.
    get_memlist()의 return값인 전체연락처 dto가 들어있는 list를 받아
    사용자에게 출력한다.'''
    print(f"총 {len(dto_list)}명의 회원이 검색되었습니다.")
    for dto in dto_list:
        print(f'회원정보 : 이름 = {dto.get_name()}, '
              f'전화번호 = {dto.get_phone_num()}, '
              f'e-mail = {dto.get_email()}, '
              f'구분 = {dto.get_cls_name()}')

def mod_or_del(mod_or_del: str) -> str:
    '''수정이나 삭제할 회원의 이름을 사용자에게 입력받아 return해주는 함수이다.'''
    name_input = input(f'{mod_or_del}할 회원의 이름을 입력하세요 : ')
    return name_input

def repeat_memlist(mod_or_del: str, repeat_mem_list: list) -> str:
    '''model에서 repeat_mem_list() 함수의 return값을 받아 index와 연락처를 보여주는 함수이다.
    사용자에게 수정이나 삭제할 회원의 번호를 입력받아 return한다.'''
    for i, dto in enumerate(repeat_mem_list):
        print(f'{i+1}. '
              f'회원정보 : 이름 = {dto.get_name()}, '
              f'전화번호 = {dto.get_phone_num()}, '
              f'e-mail = {dto.get_email()}, '
              f'구분 = {dto.get_cls_name()}')
    repeat_mem_input_num: str = input(f'{mod_or_del}할 회원의 번호를 입력하세요 : ')
    return repeat_mem_input_num

def update_mem():
    '''add_member(aom) 함수와 동일한 함수이다. '''
    update_dto = add_member('수정')
    return update_dto
