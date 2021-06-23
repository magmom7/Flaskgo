#User table의 crud 로직을 전달하는 클래스 
import cx_Oracle
from dto import UserDTO, BoardDTO
import json
import collections # 데이터를 어떤 구조로 관리할 것인가를 의미하는 자료구조를 지원하는 library


class UserDAO:
    # 사번으로 직원명, 급여를 검색해서 반환
    def userinsert(self, dto): #만약 속성값이 30개가 넘는다면 관리하기 힘드므로,,, DTO 객체 통으로 받음
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            print("===1==")
            try:
                print("===1212==")
                cur.execute("insert into users values(:user_id, :user_name, :user_pw, :user_interset)", user_id=dto.getId(), user_name=dto.getName(), user_pw=dto.getPw(), user_interset=dto.getInterest())
                conn.commit()
                print("===2==")
            
            except Exception as e: 
                print(e) 

        except Exception as e: 
            print(e) 
                
        finally:
            cur.close()
            conn.close()
        print("===3==")

    def userall(self):
        data=[]
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from users") 
                rows = cur.fetchall()
                # json 포멧으로 가공 : empno, ename, sal key - json배열
                # 다양한 방법 : 저장하는 순서를 유지하는 구조의 dict 클래스
                v = [] # v변수에 python 구조의 dict 구조로 저장 -> data 변수로 json 포멧으로 변환
                for row in rows:
                    d = collections.OrderedDict()# 저장하는 순서인지하는
                    d['user_id'] = row[0]
                    d['user_name']= row[1]
                    d['user_secret'] = row[2]
                    d['user_interest'] = row[3]
                    v.append(d)
                
                data = json.dumps(v, ensure_ascii=False) #json 포멧으로 완벽하게 
                # print("*"*30)
                # print(type(data)) # <class 'str'>
                # print("*"*30)
            except Exception as e: # 예외..
                print(e) # print e

        except Exception as e: 
            print(e)

        finally:
            cur.close() # 자원 반환
            conn.close()

        return data

    def getIndex(self):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select max(user_id) from users") 
                row = cur.fetchone()
                if row[0] is None:
                    data = 0
                else:
                    data = row[0]
                # print(row)
                # print(type(row))
                # print(row[0])
                # print(type(row[0]))
         
            except Exception as e: # 예외..
                print(e) # print e

        except Exception as e: 
            print(e)

        finally:
            cur.close() # 자원 반환
            conn.close()
        # print("--",data)
        return data


class BoardDAO:
    
    def textinsert(self, dto): #만약 속성값이 30개가 넘는다면 관리하기 힘드므로,,, DTO 객체 통으로 받음
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
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

    def boardall(self, uid):
        data=[]
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from board order by idx asc") 
                
                rows = cur.fetchall()
                
                # json 포멧으로 가공 : empno, ename, sal key - json배열
                # 다양한 방법 : 저장하는 순서를 유지하는 구조의 dict 클래스
                v = [] # v변수에 python 구조의 dict 구조로 저장 -> data 변수로 json 포멧으로 변환
                for row in rows:
                    d = collections.OrderedDict()# 저장하는 순서인지하는
                    d['idx'] = row[0]
                    d['title']= row[1]
                    d['content'] = row[2]
                    d['date'] = row[3]
                    d['id'] = row[4]
                    v.append(d)
                
                data = json.dumps(v, ensure_ascii=False) #json 포멧으로 완벽하게
                print(data) 
                # print("*"*30)
                # print(type(data)) # <class 'str'>
                # print("*"*30)
            except Exception as e: # 예외..
                print(e) # print e
        except Exception as e: 
            print(e)
        finally:
            cur.close() # 자원 반환
            conn.close()

        return data

    def getTextIndex(self):
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
                # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                # print(row)
                # print(type(row))
                # print(row[0])
                # print(type(row[0]))
            except Exception as e: # 예외..
                print(e) # print e

        except Exception as e: 
            print(e)

        finally:
            cur.close() # 자원 반환
            conn.close()
        # print(data)
        return data
# if __name__ == "__main__":
#      dao = EmpDAO()
# #     dto = EmpDTO(2, 't', 20)
#      dao.empall()
