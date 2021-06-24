# User table의 crud 로직을 전달하는 클래스 
import cx_Oracle
from dto import UserDTO, BoardDTO
import json
import collections # 데이터를 어떤 구조로 관리할 것인가를 의미하는 자료구조를 지원하는 library



class UserDAO:
    def userinsert(self, dto): 
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                cur.execute("insert into users values(:user_id, :user_name, :user_pw, :user_interset)", user_id=dto.getId(), user_name=dto.getName(), user_pw=dto.getPw(), user_interset=dto.getInterest())
                conn.commit()

            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e) 
                
        finally:
            cur.close()
            conn.close()

    def userone(self, username, userpw):
        flag = False
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                print(username)
                print(userpw)
                cur.execute("select * from users where user_name = :username and user_secret =: userpw", username = username, userpw = userpw) 
                row = cur.fetchone()

                if row:
                    flag = True
                # print("-"*30)
                # print(row)
                # print("-"*30)
                
                # data = collections.OrderedDict()
                # data['user_id'] = row[0]
                # data['user_name']= row[1]
                # data['user_secret'] = row[2]
                # data['user_interest'] = row[3]

            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e)

        finally:
            cur.close() 
            conn.close()

        return flag

    def userall(self):
        data=[]
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from users where ") 
                rows = cur.fetchall()
    
                v = [] 
                for row in rows:
                    d = collections.OrderedDict()
                    d['user_id'] = row[0]
                    d['user_name']= row[1]
                    d['user_secret'] = row[2]
                    d['user_interest'] = row[3]
                    v.append(d)
                
                data = json.dumps(v, ensure_ascii=False) 
           
            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e)

        finally:
            cur.close() 
            conn.close()

        return data

    def getIndex(self):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                cur.execute("select max(user_id) from users") 
                row = cur.fetchone()
                if row[0] is None:
                    data = 0
                else:
                    data = row[0]
         
            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e)

        finally:
            cur.close() 
            conn.close()
        
        return data


class BoardDAO:
    
    def textinsert(self, dto): #만약 속성값이 30개가 넘는다면 관리하기 힘드므로,,, DTO 객체 통으로 받음
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                print("in")
                cur.execute("insert into board values(:text_idx, :title, :content, :input_date, :user_id)", text_idx =dto.getIdx(), title=dto.getTitle(), content=dto.getContent(), input_date=dto.getInputDate(), user_id=dto.getId())
                conn.commit()
            
            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e) 
                
        finally:
            cur.close()
            conn.close()
        

    def getuserID(self, name):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            # conn = cx_Oracle.connect("scott/tiger@localhost/xe")
            cur = conn.cursor()
            try:
                cur.execute("select user_id from users where user_name = :getname", getname=name)
                # print("ininiin")
                row = cur.fetchone()
                # print("---row---", row)
                #data = '{"ename":"smith", "sal":800.0}'
                return row
            
            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e) 
                
        finally:
            cur.close()
            conn.close()

    def boardall(self):
        data=[]
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select idx, title, content, input_date, user_name from board,users where board.user_id = users.user_id  order by idx asc") 
                
                rows = cur.fetchall()
                
                v = [] 
                for row in rows:
                    d = collections.OrderedDict()
                    d['idx'] = row[0]
                    d['title']= row[1]
                    d['content'] = row[2]
                    d['date'] = row[3]
                    d['name'] = row[4]
                    v.append(d)
                
                data = json.dumps(v, ensure_ascii=False) 
                print(data) 
               
            except Exception as e: 
                print(e) 
        except Exception as e: 
            print(e)
        finally:
            cur.close()
            conn.close()

        return data

    def getTextIndex(self):
        data=''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select max(idx) from board") 
                row = cur.fetchone()
                if row[0] is None:
                    data = 0
                else:
                    data = row[0]

            except Exception as e: # 예외..
                print(e) # print e

        except Exception as e: 
            print(e)

        finally:
            cur.close() # 자원 반환
            conn.close()
        
        return data

    def boardmy(self, uid):
        data=[]
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try: 
                cur.execute("select idx, title, content, input_date, user_name from board,users where board.user_id = users.user_id and board.user_id = :id order by idx asc", id = uid) 
                rows = cur.fetchall()
               
                v = [] 
                for row in rows:
                    d = collections.OrderedDict()
                    d['idx'] = row[0]
                    d['title']= row[1]
                    d['content'] = row[2]
                    d['date'] = row[3]
                    d['name'] = row[4]
                    v.append(d)
                
                data = json.dumps(v, ensure_ascii=False) 
                print(data) 
               
            except Exception as e: 
                print(e) 
        except Exception as e: 
            print(e)
        finally:
            cur.close()
            conn.close()

        return data
    
# if __name__ == "__main__":
#      dao = EmpDAO()
# #     dto = EmpDTO(2, 't', 20)
#      dao.empall()
