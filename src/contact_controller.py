# contact_controller.py
from contact_model import DB as model
import contact_view as view
import contact_exception as err

class Running:
    """
    contact_model.py의 DB 클래스를 불러와 사용.
    """
    def __init__(self, path="ora_user/1234@localhost:1521/xe"):
        self.model = model(path)
    def run(self):
        flag = True
        while(flag):
            input = view.menu_input()
            if input == '1':
                self.add()
            elif input == '2':
                self.memlist()
            elif input == '3':
                self.modify()
            elif input == '4':
                self.delete()
            elif input == '5':
                self.exit()
                flag = False
            else:
                print("*유효하지 않은 입력입니다. 1부터 5까지의 숫자만 입력하세요.")

    def add(self):
        """view의 input값과 model의 함수를 조립하여 add하는 함수이다."""
        dto = view.add_member('등록')
        try:
            err.valid_name(dto.get_name())
            err.vaild_cellphone(dto.get_phone_num())
            err.valid_email(dto.get_email())
            err.valid_cls(dto.get_cls_name())
            self.model.add_mem(dto)
        except err.NoNameError as e:
            print(e)
        except err.CellphoneError as e:
            print(e)
        except err.EmailValid as e:
            print(e)
        except err.NoClsName as e:
            print(e)
    def memlist(self):
        """view의 input값과 model의 함수를 조립하여 멤버의 list를 불러오는 함수이다."""
        view.memlist(self.model.get_memlist())
    def modify(self):
        """view의 input값과 model의 함수를 조립하여 modify하는 함수이다."""

        name = view.mod_or_del('수정')
        repeat_mem_list = self.model.find_repeat_mem(name)
        if repeat_mem_list:
            repeat_mem_input_num = view.repeat_memlist('수정', repeat_mem_list)
            dto = view.add_member('수정')
            try:
                err.valid_name(dto.get_name())
                err.vaild_cellphone(dto.get_phone_num())
                err.valid_email(dto.get_email())
                err.valid_cls(dto.get_cls_name())
                self.model.update_mem(repeat_mem_list, repeat_mem_input_num, dto)
            except err.NoNameError as e:
                print(e)
            except err.CellphoneError as e:
                print(e)
            except err.EmailValid as e:
                print(e)
            except err.NoClsName as e:
                print(e)
            except IndexError:
                print("*잘못된 번호를 입력하였습니다.")
        else:
            print("*해당하는 회원의 정보가 없습니다.")

    def delete(self):
        """view의 input값과 model의 함수를 조립하여 delete하는 함수이다."""
        name = view.mod_or_del('삭제')
        repeat_mem_list = self.model.find_repeat_mem(name)
        if repeat_mem_list:
            try:
                repeat_mem_input_num = view.repeat_memlist('삭제', repeat_mem_list)
                self.model.delete_mem(repeat_mem_list, repeat_mem_input_num)
            except IndexError:
                print("*잘못된 번호를 입력하였습니다.")
        else:
            print("*해당하는 회원의 정보가 없습니다.")

    def exit(self):
        """종료시 사용되지 않은 cls 요소들을 cls 테이블에서 제거하고 종료하는 함수이다."""
        self.model.delete_unused_cls()
        print("종료되었습니다.")
