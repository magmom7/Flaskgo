-- 임시로 만든 test 결과 확인

drop table Users CASCADE CONSTRAINT; 
drop table Board;
drop sequence seq_user;
drop sequence seq_board;
create sequence seq_user;
create sequence seq_board;

create table Users(
    User_id number(3) primary key,
    User_name varchar2(20) not null,
    User_secret number(20),
    User_interest varchar2(20) constraint ck_user_interest check (User_interest in ('front', 'back', 'analysis'))
);

insert into Users values(seq_user.nextval, '유지현', 13,'front');
insert into Users values(seq_user.nextval, '이성규', 15,'back');
insert into Users values(seq_user.nextval, '장동기', 17,'analysis');
insert into Users values(seq_user.nextval, '장동기', 17,'as');

insert into Users values(seq_user.nextval, 'jihyeon', 13,'front');
insert into Users values(seq_user.nextval, 'seongkyu', 15,'back');
insert into Users values(seq_user.nextval, 'donkey', 17,'analysis');
insert into Users values(seq_user.nextval, 'donkey', 17,'as'); -- 이건 안들어감 


create table Board(
    Idx number(3) primary key,
    Title varchar2(30),
    Content varchar2(300),
    Input_date varchar2(30),
    User_id number(3) references Users(User_id)
);

insert into Board values(seq_board.nextval, '제목', '내용..........', sysdate, 1);

insert into Board values(seq_board.nextval, 'Title', 'content..........', sysdate, 1);