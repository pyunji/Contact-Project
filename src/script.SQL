create table cls (
		cls_num 	number	 					primary key
	, cls_name 	varchar2(10 char) not null unique
	);

create table contact (
		con_seq 	number						primary key
	,	name 			varchar2(5 char) 	not null
	, phone_num varchar2(11) 			not null
	, email 		varchar2(40) 			not null
	, cls_num 	number
	, constraints contact_cls_num_fk
		foreign key (cls_num)
		references cls(cls_num)
	);

drop table cls;
drop table contact;

select * from cls;
select * from contact;