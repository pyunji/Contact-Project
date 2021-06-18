# contact_model.py
import cx_Oracle as cxo
import contact_dto as cd
class Exe:
    """sql문을 받아 execute하는 클래스이다."""
    def __init__(self, path="ora_user/1234@localhost:1521/xe"):
        """
        기본 경로를 초기화 한 후 사용자가 원하는 경로를 입력받을 수 있께 하였다.

        :param path: 오라클 db 로그인 경로
        """
        self.path = path
    def exe_fa(self, sql):
        """sql문을 입력받아 fetchall을 실행하는 함수이다.
        fetchall 결과를 return한다."""
        conn = cxo.connect(self.path)
        csr = conn.cursor()
        csr.execute(sql)
        data = csr.fetchall()
        csr.close()
        conn.close()
        return data
    def exe_fo(self, sql):
        """
        sql문을 받아 fetchone을 실행하는 함수이다.
        :param sql: fetchone을 실행할 sql문
        :return: tuple 형태의 fetchone결과
        """
        conn = cxo.connect(self.path)
        csr = conn.cursor()
        csr.execute(sql)
        data = csr.fetchone()
        csr.close()
        conn.close()
        return data

    def exe_data(self, sql, data=tuple()):
        """
        insert나 update, delete시 sql문에 대입할 data를 입력받아 실행하는 함수이다.
        :param sql: sql문
        :param data: sql문에 대입할 데이터
        """
        conn = cxo.connect(self.path)
        csr = conn.cursor()
        csr.execute(sql, data)
        csr.close()
        conn.commit()
        conn.close()

class DB(Exe):
    """Exe 클래스를 상속받으며, DB에 접근하는 클래스이다."""
    def return_cls_name(self, cls_num: int) -> object:
        """
        구분번호를 입력받아 구분명을 return하는 함수이다.
        :param cls_num: 구분번호
        :return: 구분명
        """
        sql = f"""
            select cls_name
            from cls
            where cls_num = {cls_num}
        """
        cls_name = self.exe_fo(sql)
        return cls_name[0]

    def return_cls_num(self, cls_name: str) -> int:
        """
        구분명을 입력받아 구분번호를 return해주는 함수이다.
        cls테이블에 존재하지 않는 구분명의 경우
        cls테이블에 insert 후 새로 생성된 구분번호를 return 한다.
        :param cls_name: 구분명
        :return: 구분번호
        """
        sql = f"""select cls_num
            from cls
            where cls_name = '{cls_name}'"""
        cls_num = self.exe_fo(sql)
        if not cls_num:
            sql = """insert into cls
                values (:1, :2)"""
            data = (self.generate_id('cls_num','cls'), cls_name)
            self.exe_data(sql, data)
            return data[0]
        return cls_num[0]

    def add_mem(self, dto):
        """
        view에서 생성된 dto를 db에 추가하는 함수이다.
        :param dto: view에서 사용자에게 입력받은 연락처
        """
        data = (self.generate_id('con_seq','contact'),
                dto.get_name(),
                dto.get_phone_num(),
                dto.get_email(),
                self.return_cls_num(dto.get_cls_name()))
        sql = 'insert into contact values(:1,:2,:3,:4,:5)'
        self.exe_data(sql, data)

    def generate_id(self, con_seq_or_cls_num: str, contact_or_cls: str) -> int:
        """
        cls나 contact의 id를 생성하는 함수이다.
        :param con_seq_or_cls_num: con_seq를 생성할 지 cls_num을 생성할 지 정한다.
        :param contact_or_cls: contact테이블과 cls테이블 중 선택한다.
        :return: pk에 부응하는 id 생성
        """
        sql = f"""
            select nvl(max({con_seq_or_cls_num}), 0)
            from {contact_or_cls}
        """
        _id: tuple = self.exe_fo(sql)
        return _id[0]+1

    def return_dto_from_db(self, data) -> list:
        """
        db에서 받아온 데이터를 dto에 세팅 후 dto로 이루어진 list에 저장하는 함수이다.
        :param data: db에서 받은 전체연락처
        :return: 전체 연락처를 dto에 세팅 후 list에 추가한 값
        """
        dto_list = []
        for con in data:
            dto = cd.ContactDTO()
            dto.set_con_seq(con[0])
            dto.set_name(con[1])
            dto.set_phone_num(con[2])
            dto.set_email(con[3])
            dto.set_cls_num(con[4])
            dto.set_cls_name(self.return_cls_name(con[4]))
            dto_list.append(dto)
        return dto_list

    def find_repeat_mem(self, name_input: str) -> list:
        """
        수정하거나 삭제할 회원의 이름을 입력받아 해당 회원의 dto를 list에 추가하는 함수이다
        :param name_input: 수정하거나 삭제할 회원의 이름
        :return: name_input과 일치하는 모든 연락처
        """
        sql = f"""
            select * 
            from contact
            where name = '{name_input}'
        """
        data = self.exe_fa(sql)
        repeat_mem_list = self.return_dto_from_db(data)
        return repeat_mem_list

    def update_mem(self, repeat_mem_list: list, repeat_mem_input_num: str, update_dto):
        """

        :param repeat_mem_list: 중복되는 이름을 가진 연락처
        :param repeat_mem_input_num: 사용자에게 입력받은 수정할 연락처의 인덱스
        :param update_dto: 사용자에게 입력받은 새로 수정할 연락처
        """
        '''사용자에게 repeat_mem_list를 보여준 후 수정할 회원의 index를 입력받아 db에 업데이트 하는 함수이다.'''
        num = int(repeat_mem_input_num)-1
        update_mem_dto = repeat_mem_list[num]
        data = (update_dto.get_name(),
                update_dto.get_phone_num(),
                update_dto.get_email(),
                self.return_cls_num(update_dto.get_cls_name()),
                update_mem_dto.get_con_seq()
                )
        sql = """
            update contact
            set name = :1
                , phone_num = :2
                , email = :3
                , cls_num = :4
            where con_seq = :5   
        """
        self.exe_data(sql,data)

    def delete_mem(self, repeat_mem_list ,repeat_mem_input_num):
        """
        사용자에게 repeat_mem_list를 보여준 후 삭제할 회원의 index를 입력받아 db에 업데이트 하는 함수이다.
        :param repeat_mem_list: 중복되는 이름을 가진 연락처
        :param repeat_mem_input_num: 사용자에게 입력받은 삭제할 연락처의 인덱스
        """
        num = int(repeat_mem_input_num)-1
        delete_mem_dto = repeat_mem_list[num]
        data = (delete_mem_dto.get_con_seq(),)
        sql = """delete from contact
            where con_seq = :1 """
        self.exe_data(sql,data)
    def get_memlist(self) -> list:
        """
        저장된 전체 연락처를 return하는 함수이다.
        :return: 전체 연락처를 담은 list
        """
        sql = """
            select *
            from contact
        """
        dto_list = self.return_dto_from_db(self.exe_fa(sql))
        return dto_list
    def delete_unused_cls(self):
        """프로그램 종료시 contact 테이블에 참조되지 않은 구분은 삭제하는 함수이다."""
        sql = """
            DELETE FROM cls
            WHERE cls.cls_num in (
		        select cls.cls_num
		        from contact, cls
		        where contact.cls_num(+) = cls.cls_num
	            group by cls.cls_num
		        having count(contact.cls_num) = 0
		        )
        """
        self.exe_data(sql)


