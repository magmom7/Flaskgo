-- 임시로 만든 test 결과 확인
-- 참조 때문에 cascade 넣어서 드랍하였음
drop table Users CASCADE CONSTRAINTS;
drop table Board;
drop sequence seq_user;
drop sequence seq_board;
create sequence seq_user;
create sequence seq_board;

create table Users(
    User_id number(3) primary key,
    User_name nvarchar2(20) not null,
    User_secret number(20),
    User_interest nvarchar2(20) constraint ck_user_interest check (User_interest in ('front', 'back', 'analysis'))
);

insert into Users values(seq_user.nextval, '유지현', 13,'front');
insert into Users values(seq_user.nextval, '이성규', 15,'back');
insert into Users values(seq_user.nextval, '장동기', 17,'analysis');
insert into Users values(seq_user.nextval, '장동기', 17,'as'); -- 이건 안들어감 

-- insert into Users values(seq_user.nextval, 'jihyeon', 13,'front');
-- insert into Users values(seq_user.nextval, 'seongkyu', 15,'back');
-- insert into Users values(seq_user.nextval, 'donkey', 17,'analysis');
-- insert into Users values(seq_user.nextval, 'donkey', 17,'as'); -- 이건 안들어감 


create table Board(
    Idx number(3) primary key,
    Title varchar2(30),
    Content varchar2(300),
    Input_date varchar2(30),
    User_id number(3) references Users(User_id)
);

insert into Board values(seq_board.nextval, '제목', '내용..........', sysdate, 1);







-- 아래는 오라클 한글 설정 관련인데 안먹힘
select * from v$nls_parameters;
SELECT * FROM sys.props$ where name='NLS_LANGUAGE';
select name, value$ from SYS.props$


update sys.props$ set value$='UTF8' where name = 'NLS_CHARACTERSET';
update sys.props$ set value$='KO16MSWIN949' where name='NLS_CHARACTERSET';  
update sys.props$ set value$='KO16MSWIN949' where  name='NLS_NCHAR_CHARACTERSET';
update sys.props$ set value$='KOREAN_KOREA.KO16MSWIN949' where name='NLS_LANGUAGE';

commit;

SHUTDOWN IMMEDIATE;

STARTUP MOUNT;

ALTER SYSTEM ENABLE RESTRICTED SESSION;

ALTER SYSTEM SET JOB_QUEUE_PROCESSES=0;

ALTER SYSTEM SET AQ_TM_PROCESSES=0;

ALTER DATABASE OPEN;

ALTER DATABASE CHARACTER SET INTERNAL_USE KO16MSWIN949;

SHUTDOWN IMMEDIATE;

STARTUP;



출처: https://rumblefish.tistory.com/66 [RumbleFish]

