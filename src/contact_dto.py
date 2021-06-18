# contact_dto.py
class ContactDTO():
    """연락처의 이름과 휴대폰번호, 이메일, 구분명, 구분이름, id를 get, set하는 class이다."""
    def __init__(self,name='',phone_num='',email='',cls_name='',cls_num = 0,con_seq=0):
        self._name = name
        self._phone_num = phone_num
        self._email = email
        self._cls_num = cls_num
        self._cls_name = cls_name
        self._con_seq = con_seq

    def set_name(self, name):    #setter
        self._name = name
    def set_phone_num(self,phone_num):
        self._phone_num = phone_num
    def set_email(self,email):
        self._email = email
    def set_cls_num(self,cls_num):
        self._cls_num = cls_num
    def set_cls_name(self,cls_name):
        self._cls_name = cls_name
    def set_con_seq(self,con_seq):
        self._con_seq = con_seq

    def get_name(self):     #getter
        return self._name
    def get_phone_num(self):
        return self._phone_num
    def get_email(self):
        return self._email
    def get_cls_num(self):
        return self._cls_num
    def get_cls_name(self):
        return self._cls_name
    def get_con_seq(self):
        return self._con_seq
