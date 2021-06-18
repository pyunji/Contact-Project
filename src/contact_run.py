# contact_run.py
import contact_controller as ctr
"""
=====================================================================
=====================================================================
연락처에 연동할 오라클 계정을 path에 입력하세요.
default 연결계정은 "ora_user/1234@localhost:1521/xe"입니다. 
=====================================================================
* path의 형식은 "사용자/암호@호스트:포트/SID"으로 입력하세요.
* 연결할 계정의 DB에는 반드시 contact테이블과 cls테이블이 
 생성되어있어야 합니다.
 
* 새로 contact테이블과 cls를 만드는 경우의 가이드라인은 다음과 같습니다.
    create table cls (
        cls_num  number	 primary key
      , cls_name varchar2(10 char) not null unique
    );
    create table contact (
        con_seq  number  primary key
      , name  varchar2(5 char)  not null
      , phone_num  varchar2(11)  not null
      , email  varchar2(40)  not null
      , cls_num  number
      , constraints  contact_cls_num_fk
      foreign key (cls_num)
      references  cls(cls_num)
    );
=====================================================================
=====================================================================

"""
path = "ora_user/1234@localhost:1521/xe"    #path를 지정하세요.
running = ctr.Running(path)
running.run()